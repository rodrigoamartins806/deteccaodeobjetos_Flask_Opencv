# Detecção de Objetos Com Opencv e Flask

Este e o resultado do trabalho de aprendizagem da turma de Analise e Desenvolvimento de sistemas da Faculdade Pitagoras de Ribeirão das Neves


## Objetivo do Projeto

Este projeto tem o objetivo de detectar objetos e reinderizar este processo em uma pagina Web em tempo real e com uma sinalização do que foi 
detectado, estamos utilizando os seguintes recursos neste projeto.

>`Flask`
>`pusher`
>`opencv`

## Executando o projeto

Para executar o projeto e contribuir siga os seguintes passos.

1. Crie uma conta no site https://pusher.com/  entre em channels e cria a sua conta e pegue as credenciais
2. clone este projeto em sua maquina git clone https://github.com/rodrigoamartins806/deteccaodeobjetos_Flask_Opencv.git
3. Altere as variaveis abaixo no arquivo **_camera.py_** 
> `pusher_client = pusher.Pusher(
  app_id= ,
  key= ,
  secret= ,
  cluster= ,
  ssl= 
)`
4. No arquivo **_templates/index.html_** altere as informações abaixo com as suas credenciais do Pusher
> `     Pusher.logToConsole = true;
 
     var pusher = new Pusher('<ID>', {
       cluster: '<Cluster>'
     });`