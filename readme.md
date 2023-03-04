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
    env\Scripts\activate
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
     python manage.py runserver 
```