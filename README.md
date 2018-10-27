# ecommerce

### Endpoints:


##### Produtos

```
https://apiecommerce-trello.herokuapp.com/api/v1/produtos/

https://apiecommerce-trello.herokuapp.com/api/v1/produtos/{uuid}
```

##### Pedidos

```
https://apiecommerce-trello.herokuapp.com/api/v1/pedidos

https://apiecommerce-trello.herokuapp.com/api/v1/pedidos/{1}
```

##### Categorias

```
https://apiecommerce-trello.herokuapp.com/api/v1/categorias/
```


### Algumas diretrizes

Primeiro é precisso criar as categorias, 
logo pode se criar produtos e depois os pedidos poderam ser feitos.



### Como rodar o projeto

``` git clone https://github.com/eltonjncorreia/ecommerce.git ```

``` cd ecommerce ```

``` python -m venv .venv ```

``` source .venv/bin/activate ```

``` pip install -r requirements-dev.txt ```


### Configure as instâncias

``` cp contrib/env-sample .env ```

``` python contrib/gerar_secret_key.py ```

``` Colocar a secret key no arquivo .env recem criado ```

``` python manage.py test ```

### Crie um super usuario para ter acesso a API

``` python manage.py migrate ```

``` python manage.py createsuperuser ```

``` python manage.py runserver```


```
## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configuraçoes para o heroku
3. Define uma SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

``` console
heroku apps:create minhainstancia
heroku config:push
heroku config:set SECRET_KEY
heroku config:set DEBUG=False

git push heroku master --force
```
