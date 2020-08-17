## Django Amazon Web Services (DjAWS)

Este proyecto de ejemplo integra el framework Django con sevicios de AWS y es complemento a los tutoriales que
ire creando en mi blog personal

## Uso
### Requerimientos
* Python +3.6
* Django 3.x
* Pipenv

### Instalacion de dependencias
* sudo apt update
* sudo apt install python3.6
* sudo apt install python3-pip
* pip install pipenv


### Inicialización del proyecto

#### Configuracion
* Crear el archivo .env y configurarlo de acuerdo al ambiente
```
cd djaws/
cp -a .env.example .env
```

* Crear el archivo de configuracion de django segun ambiente de despliegue
```
cd djaws/settings/
cp -a local_settings.py.example local.py
```

* Generar **SECRET_KEY_** desde la consola de django y remplazar en .env
```
python manage.py shell --settings=management.settings.local
```

```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

#### Instalar requerimientos
```
pipenv install
```

#### Iniciar proyecto
* Ejecutar migraciones
```
python manage.py migrate --settings=management.settings.local
```
* Agregar data de prueba si existe
```
python manage.py loaddata fixtures/db.json --settings=management.settings.local
```
* Ejecutar servidor de prueba
```
python manage.py runserver --settings=management.settings.local
```

* Si el proyecto se ejecuta en modo desarrollo ('runserver') en el archivo local.py se debe comentar las lineas
```
# STATICFILES_DIRS = []
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

### Test
* Cumplimiento de la guía de estilo de python
```
flake8 .
```
