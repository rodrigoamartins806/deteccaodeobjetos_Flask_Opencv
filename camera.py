from time import sleep
import cv2

import pusher
from environs import Env

env = Env()
env.read_env()

#crie uma conta no site do pusher e preencha aqui os dados da sua conta
pusher_client = pusher.Pusher(
  app_id= env("app_id"),
  key= env("key"),
  secret= env("secret"),
  cluster= env("cluster"),
  ssl= env("ssl")
)


#treinamento para detecção de face
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
#treinamento para detecçao de corpo
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

ds_factor=0.6

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
        
    
    def get_frame(self):
        success, image = self.video.read()
        image=cv2.resize(image,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
        print(bodies)
        
        #desenha sobre o contorno do corpo
        for (x,y,w,h) in bodies:
            contbody =  str(bodies.shape[0])
            cv2.rectangle(image,(x,y),(x+w,y+h),(242, 149, 71),2)
            cv2.putText(image, "Corpo: "+contbody, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (242, 149, 71), 2, cv2.LINE_AA)

            #so envia notificação caso seja detectado
            if int(contbody) >= 1:
                pusher_client.trigger('my-channel', 'corpo', {'message': str(contbody)})
            break

        face_rects=face_cascade.detectMultiScale(gray,1.3,5)

        #desenha sobre o rosto
        for (x,y,w,h) in face_rects:
            contface =  str(face_rects.shape[0]) 
            cv2.rectangle(image,(x,y),(x+w,y+h),(164, 38, 223 ),2) 
            cv2.putText(image, "Rosto: "+contface, (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (164, 38, 223 ), 2, cv2.LINE_AA)    

            #so envia notificação caso seja detectado
            if int(contface) >= 1:
                pusher_client.trigger('my-channel', 'rosto', {'message': str(contface)})
            break     

        ret, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()