# Mapa das minas - API

O jeito mais simples de rodar o projeto é utilizando o Docker,
para isso tenha certeza de que está com ele instalado e atualizado.

- Rode o seguinte comando:

```
docker-compose up
```

A aplicação estará rodando na porta 8000.

Caso você opte por rodar a aplicação diretamente na sua máquina,
você deverá ter o python 3.6.6 instalado e também recomendamos o
uso do pipenv.

- Para rodar a aplicação utilize o seguinte o comando:

```
python manage.py runserver
```

Se você está em uma máquina linux temos uma série de comandos make
para facilitar.

- Para instalar o pipenv e as dependências do projeto:

```
make install
```

- Para rodar a aplicação com docker:

```
make up
```

- Para parar a aplicação rodando com docker:

```
make down
```

- Para entrar no django shell:

```
make shell
```

- Para rodar a aplicação na sua máquina:

```
make run
```
