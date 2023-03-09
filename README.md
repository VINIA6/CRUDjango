# CRUD - Django

Em um cenário de desenvolvimento notamos que teríamos que gerenciar varias versões de pacotes e do próprio Python na maquina, o que poderia rapidamente se transformar em uma grande confusão de versões entre projetos, um verdadeiro caos. Por isso utilizamos o método de criação de um ambiente virtual, veja abaixo os comandos para criar o ambiente virtual e baixar as dependencias do projeto.

Criação de ambiente virtual:

      py -m venv venv
      
Instalação das dependências:

      pip install -r requirements.txt
      
Com o ambiente configurado, podemos rodar o projeto:

      py manage.py runserver


A aplicação consiste em uma experiência de aprendizado com o framework Django, utilizando seus principais recursos de migrations, views e models. A aplicação simula a construção de um software de lista de compras, para aplicarmos o conceito de CRUD (Create, Read, Update, Delete), na ferramenta manipulamos o banco de dados SQLite.
