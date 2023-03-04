# Instalacion 

- Crear ambiente virtual :
 ```sh
     python3 -m venv venv
```

- Activar ambiente virtual :
 ```sh
 linux
     source venv/bin/activate
windows 
    venv\Scripts\activate
```

- Crear ambiente virtual:
 ```sh
     python3 -m venv venv
```

- Instala las dependencias:

 ```sh
     pip install -r requirements.txt
```
- Ejecuta migraciones:
 ```sh
     python manage.py migrate
```
- Crear super usuario :
 ```sh
     python manage.py createsuperuser
```
- Correr el sevidor  :
 ```sh
 
 - crear un settings.py:
 ```sh
     bebe contener 
     DEBUG = True
    USERDB = 'usuario de la base de datos'
    DBPASSWORD = 'contraseña'
    ALLOWED_HOSTS = ['*']
     python manage.py runserver 
```
