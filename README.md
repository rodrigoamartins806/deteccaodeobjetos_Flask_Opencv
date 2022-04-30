# Detecção de Objetos Com Opencv e Flask
<p align="left">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

Este é o resultado do trabalho de aprendizagem da turma de Análise e Desenvolvimento de sistemas da Faculdade Pitágoras de Ribeirão das Neves 


## Objetivo do Projeto

Este projeto tem o objetivo de detectar objetos e reinderizar este processo em uma pagina Web em tempo real e com uma sinalização do que foi 
detectado, inicialmente o projeto foi adaptado para detectar pessoas e faces.


## Ferramentas utilizadas

<a href="https://www.python.org/" target="_blank"> <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" alt="java" width="40" height="40"/> </a> 

<a href="https://flask.palletsprojects.com/en/2.1.x/" target="_blank"> <img src="https://github.com/devicons/devicon/blob/master/icons/flask/flask-original.svg" alt="Flask" width="40" height="40"/> </a> <a href="https://opencv.org/" target="_blank"> <img src="https://github.com/devicons/devicon/blob/master/icons/opencv/opencv-original.svg" alt="firebase" width="40" height="40"/> </a>

###


## Executando o projeto

Para executar o projeto e contribuir siga os seguintes passos.

1. Crie uma conta no site https://pusher.com/  entre em channels e cria a sua conta e pegue as credenciais
2. clone este projeto em sua maquina 
```javascript
git clone https://github.com/rodrigoamartins806/deteccaodeobjetos_Flask_Opencv.git
```
3. Altere as variaveis abaixo no arquivo **_camera.py_** 
```javascript
pusher_client = pusher.Pusher(
  app_id= ,
  key= ,
  secret= ,
  cluster= ,
  ssl= 
)
```
4. No arquivo **_templates/index.html_** altere as informações abaixo com as suas credenciais do Pusher
```javascript
    Pusher.logToConsole = true;
     var pusher = new Pusher('<Key>', {
       cluster: '<Cluster>'
    });
```
5. Crie um ambiente virtual 
6. Ative o seu Ambiente virtual
7. Instale as dependencias do projeto com o seguinte comando
```javascript
pip install -r .\requirements.txt
```


## Tutor

| [<img src="https://avatars.githubusercontent.com/u/104536088?s=400&u=8bf78f1d1e84628a3a633ca7198a7b7df9e59354&v=4" width=115><br><sub><b>Tutor</b> Rodrigo Martins</sub>](https://github.com/rodrigoamartins806) |
| :---: | 
## Alunos

|[<img src="https://avatars.githubusercontent.com/u/104659132?v=4" width=115><br><sub>Gabriela Aguiar</sub>](https://github.com/gabrielacaguiar0) |  [<img src="https://avatars.githubusercontent.com/u/94916027?v=4" width=115><br><sub>Bruno Souza</sub>](https://github.com/BRRNN) | [<img src="https://avatars.githubusercontent.com/u/104659590?v=4" width=115><br><sub>Yuri Coelho</sub>](https://github.com/Yurimouracoelho) |[<img src="https://avatars.githubusercontent.com/u/37315196?v=4" width=115><br><sub> Aluno 1</sub>](https://github.com/) |[<img src="https://avatars.githubusercontent.com/u/37315196?v=4" width=115><br><sub> Aluno 1</sub>](https://github.com/) |
| :---: | :---: | :---: |:---: |:---: |