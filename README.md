# Detecção de Objetos Com Opencv e Flask
<p align="left">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

Este é o resultado do trabalho de aprendizagem da turma de Análise e Desenvolvimento de sistemas da Faculdade Pitágoras Unidade Ribeirão das Neves do 2º e 3º Período do ano de 2022, projeto realizado para fins de aprendizagem e demonstração dos conhecimentos adquiridos em suas aulas.


>_*O nosso sucesso depende da nossa capacidade de aprender e não de saber tudo.*_
>_Autor desconhecido_


## Objetivo do Projeto

Este projeto tem o objetivo de detectar objetos e renderizar este processo em uma página Web em tempo real e com uma sinalização do que foi
detectado, inicialmente o projeto foi adaptado para detectar pessoas e faces. 

## Ferramentas/compatibilidade para executar o projeto

Para executar este projeto é importante que tenha o python instalado caso não tenha acesse este [link](https://www.python.org/downloads/), siga as instruções para baixar e instalar, lembre de configurar o path para usar o comando py, será necessário também um editor de sua preferência, aqui listamos o [VScode]() e também o [Notepad++](https://notepad-plus-plus.org/downloads/v8.4/).

|Descrição | Versão  | Supported          |
| -------  | ------- | ------------------ |
| Python   | 3.x     | :white_check_mark: |
| VScode   | 1.66    | :white_check_mark: |
| Notepad++| 8.x     | :white_check_mark: |

## Linguagens e ferramentas utilizadas

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
8. Para rodar o projeto de o seguinte comando
```javascript
py main.py
```
9. Se tudo estiver de acordo você deverá acessar a interface gráfica do projeto acessando a url local

> `http://localhost:5000/`

## Tutor

| [<img src="https://avatars.githubusercontent.com/u/104536088?s=400&u=8bf78f1d1e84628a3a633ca7198a7b7df9e59354&v=4" width=115><br><sub><b>Tutor</b> Rodrigo Martins</sub>](https://github.com/rodrigoamartins806) |
| :---: | 
## Alunos

|[<img src="https://avatars.githubusercontent.com/u/104659132?v=4" width=115><br><sub>Gabriela Aguiar</sub>](https://github.com/gabrielacaguiar0) |  [<img src="https://avatars.githubusercontent.com/u/94916027?v=4" width=115><br><sub>Bruno Souza</sub>](https://github.com/BRRNN) | [<img src="https://avatars.githubusercontent.com/u/104659590?v=4" width=115><br><sub>Yuri Coelho</sub>](https://github.com/Yurimouracoelho) |[<img src="https://avatars.githubusercontent.com/u/104659147?v=4" width=115><br><sub>Matheus Junior</sub>](https://github.com/MatheusJunio1378) |[<img src="https://avatars.githubusercontent.com/u/104658562?v=4" width=115><br><sub>Tatielle Carolina</sub>](https://github.com/Tatielle24) |
| :---: | :---: | :---: |:---: |:---: |