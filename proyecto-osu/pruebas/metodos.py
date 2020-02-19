import requests 
import urllib
import json

def crear_usuario(apellido, contrasena, correo, nickname, nombre, telefono):
        URL = "http://35.223.30.40:5000/usuario/create"

        data = {'apellido':apellido.strip(),
                'contrasena':contrasena.strip(),
                'correo':correo.strip(),
                'nickname':nickname.strip(),
                'nombre':nombre.strip(),
                'telefono':telefono.strip(),

        }

        r = requests.post(url = URL, data = data) 
        print(r.status_code, r.reason)

def login(correo, contrasena):
        URL = "http://35.223.30.40:5000/usuario/login"

        data = {'contrasena':contrasena,
                'correo': correo
        }

        r = requests.post(url = URL, data = data)
        data = r.json()
        return data

def subir_imagen(id_usuario,nombre_imagen, ruta):
        URL = "http://35.223.30.40:5000/imagenes/upload"

        file = {'upload':open(str(ruta), 'rb')}
        data = {'fileName': nombre_imagen,
                'userName': id_usuario}

        r = requests.post(url = URL, files = file, data = data) 
        print(r.status_code, r.reason)

def descargar_imagenes(id_usuario, ruta):
        URL = "http://35.223.30.40:5000/imagenes"

        params = {'idUsuario': id_usuario}
        r = requests.get(url = URL, params = params)    
        data = r.json()
        urls = data
        for url in urls:
                urllib.request.urlretrieve(url['url'], ruta + '/' + url['name'])
        print('Imagenes descargadas en ' + ruta)

def subir_audio(id_usuario,nombre_audio, ruta):
        URL = "http://35.223.30.40:5000/audios/upload"

        file = {'upload':open(str(ruta), 'rb')}
        data = {'fileName': nombre_audio,
                'userName': id_usuario}

        r = requests.post(url = URL, files = file, data = data) 
        print(r.status_code, r.reason)

def descargar_audio(id_usuario, ruta):
        URL = "http://35.223.30.40:5000/audios"

        params = {'idUsuario': id_usuario}
        r = requests.get(url = URL, params = params)    
        data = r.json()
        urls = data
        for url in urls:
                urllib.request.urlretrieve(url['url'], ruta + '/' + url['name'])
        print('Audios descargados en ' + ruta)

def subir_cancion(artista,nombre_cancion, nombre_archivo, ruta):
        URL = "http://35.223.30.40:5000/canciones/upload"

        file = {'upload':open(str(ruta), 'rb')}
        data = {'fileName': nombre_archivo,
                'artist' : artista,
                'songName' : nombre_cancion}

        r = requests.post(url = URL, files = file, data = data) 
        print(r.status_code, r.reason)

def descargar_canciones(ruta):
        URL = "http://35.223.30.40:5000/canciones"

        r = requests.get(url = URL)    
        data = r.json()
        urls = data
        for url in urls:
                urllib.request.urlretrieve(url['url'], ruta + '/' + url['name'])
                url['path'] = ruta + '/' + url['name']
        
        return urls

def subir_puntuacion_phantom(idUsuario, partidasJugadas, puntuacionActual, puntuacionMaxima):
        URL = "http://35.223.30.40:5000/puntuaciones/phantom"

        data = {'idUsuario':idUsuario,
                'partidasJugadas':partidasJugadas,
                'puntuacionActual':puntuacionActual,
                'puntuacionMaxima':puntuacionMaxima
        }

        r = requests.post(url = URL, data = data) 
        print(r.status_code, r.reason)

def get_puntuacion_usuario_phantom(idUsuario):
        URL = "http://35.223.30.40:5000/puntuaciones/phantom"

        parameters = {
                'idUsuario':idUsuario
        }

        r = requests.get(url = URL, params=parameters)    
        data = r.json()
        if len(data):
                return data[0]
        else:
                return {}

def get_puntuacion_phantom():
        URL = "http://35.223.30.40:5000/puntuaciones/phantom/all"

        r = requests.get(url = URL)    
        data = r.json()
        return data

def subir_puntuacion_pythomers(idUsuario, partidasJugadas, puntuacionActual, puntuacionMaxima):
        URL = "http://35.223.30.40:5000/puntuaciones/pythomers"

        data = {'idUsuario':idUsuario,
                'partidasJugadas':partidasJugadas,
                'puntuacionActual':puntuacionActual,
                'puntuacionMaxima':puntuacionMaxima
        }

        r = requests.post(url = URL, data = data) 
        print(r.status_code, r.reason)

def get_puntuacion_usuario_pythomers(idUsuario):
        URL = "http://35.223.30.40:5000/puntuaciones/pythomers"

        parameters = {
                'idUsuario':idUsuario
        }

        r = requests.get(url = URL, params=parameters)    
        data = r.json()
        if len(data):
                return data[0]
        else:
                return {}

def get_puntuacion_pythomers():
        URL = "http://35.223.30.40:5000/puntuaciones/pythomers/all"

        r = requests.get(url = URL)    
        data = r.json()
        return data

def subir_puntuacion_jj(idUsuario, partidasJugadas, puntuacionMaxima):
        URL = "http://35.223.30.40:5000/puntuaciones/jj"

        data = {'idUsuario':idUsuario,
                'partidasJugadas':partidasJugadas,
                'puntuacionMaxima':puntuacionMaxima
        }

        r = requests.post(url = URL, data = data) 
        print(r.status_code, r.reason)

def get_puntuacion_usuario_jj(idUsuario):
        URL = "http://35.223.30.40:5000/puntuaciones/jj"

        parameters = {
                'idUsuario':idUsuario
        }

        r = requests.get(url = URL, params=parameters)    
        data = r.json()
        if len(data):
                return data[0]
        else:
                return {}

def get_puntuacion_jj():
        URL = "http://35.223.30.40:5000/puntuaciones/jj/all"

        r = requests.get(url = URL)    
        data = r.json()
        return data

def subir_puntuacion_aa(cantidadAlimento, idUsuario, partidasJugadas, puntuacionActual, puntuacionMaxima):
        URL = "http://35.223.30.40:5000/puntuaciones/aa"

        data = {'cantidadAlimento':cantidadAlimento,
                'idUsuario':idUsuario,
                'partidasJugadas':partidasJugadas,
                'puntuacionActual':puntuacionActual,
                'puntuacionMaxima':puntuacionMaxima
        }

        r = requests.post(url = URL, data = data) 
        print(r.status_code, r.reason)

def get_puntuacion_usuario_aa(idUsuario):
        URL = "http://35.223.30.40:5000/puntuaciones/aa"

        parameters = {
                'idUsuario':idUsuario
        }

        r = requests.get(url = URL, params=parameters)    
        data = r.json()
        if len(data):
                return data[0]
        else:
                return {}

def get_puntuacion_aa():
        URL = "http://35.223.30.40:5000/puntuaciones/aa/all"

        r = requests.get(url = URL)    
        data = r.json()
        return data

def subir_puntuacion_b612(idCancion, idUsuario, partidasJugadas, puntuacionActual, puntuacionMaxima):
        URL = "http://35.223.30.40:5000/puntuaciones/b612"

        data = {'idCancion':idCancion,
                'idUsuario':idUsuario,
                'partidasJugadas':partidasJugadas,
                'puntuacionActual':puntuacionActual,
                'puntuacionMaxima':puntuacionMaxima
        }

        r = requests.post(url = URL, data = data) 
        print(r.status_code, r.reason)

def get_puntuacion_usuario_b612(idCancion, idUsuario):
        URL = "http://35.223.30.40:5000/puntuaciones/b612"

        parameters = {
                'idCancion':idCancion,
                'idUsuario':idUsuario
        }

        r = requests.get(url = URL, params=parameters)    
        data = r.json()
        if len(data):
                return data[0]
        else:
                return {}

def get_puntuacion_b612():
        URL = "http://35.223.30.40:5000/puntuaciones/b612/all"

        r = requests.get(url = URL)    
        data = r.json()
        return data

def subir_mensaje(idEmsior, idReceptor, texto, timestamp):
        URL = "http://35.223.30.40:5000/mensajes"

        data = {'idUsuarioEmisor':idEmsior,
                'idUsuarioReceptor':idReceptor,
                'texto':texto,
                'timestamp':timestamp
        }

        r = requests.post(url = URL, data = data) 
        print(r.status_code, r.reason)

def get_mensajes(idEmsior, idReceptor):
        URL = "http://35.223.30.40:5000/mensajes/all"

        parameters = {
                'idUsuarioEmisor':idEmsior,
                'idUsuarioReceptor':idReceptor
        }

        r = requests.get(url = URL, params=parameters)    
        data = r.json()
        if len(data):
                return data[0]
        else:
                return {}