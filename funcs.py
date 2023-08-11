import random
import csv
import requests
import time
import serial
from pyfirmata import Arduino, util
from inspect import signature

def design_train(mov_1, mov_2):
    total_array = []
    for i in range(mov_1):
        total_array.append("f")
    for i in range(mov_2):
        total_array.append("e")
    total_array = random.sample(total_array, len(total_array))
    return total_array

def set_weights(training):
    training_len = len(training)
    individual_weight = 100/training_len
    return individual_weight

def chanelAPIKEY(chanelID):

    # Configura tu API Key de ThingSpeak
    api_key = "5N6GVZV6GF8QKQSY"

    # ID del canal del que deseas obtener la clave de API
    channel_id = str(chanelID)

    # URL para obtener los detalles del canal
    url = f"https://api.thingspeak.com/channels/{channel_id}.json"

    # Configura los parámetros de la solicitud GET
    params = {"api_key": api_key}

    # Realiza la solicitud GET a la API de ThingSpeak
    response = requests.get(url, params=params)

    # Verifica el estado de la respuesta
    if response.status_code == 200:
        # Analiza la respuesta JSON
        channel_details = response.json()

        # Obtén la clave de API del canal
        api_key = channel_details["api_keys"][0]["api_key"]

        # Muestra la clave de API del canal
        #print(f"API Key del Canal: {api_key}")
    else:
        pass
        #print("Error al obtener los detalles del canal. Código de estado:", response.status_code)
    return api_key

def chanelID(UID):
    # Configura tu API Key de ThingSpeak
    api_key = "5N6GVZV6GF8QKQSY"

# URL para obtener la lista de canales
    url = f"https://api.thingspeak.com/channels.json?api_key={api_key}"

# Realiza la solicitud GET a la API de ThingSpeak
    response = requests.get(url)

# Verifica el estado de la respuesta
    if response.status_code == 200:
    # Analiza la respuesta JSON
        channels = response.json()

    # Muestra los detalles de cada canal
        for canal in channels:
            if canal["name"] == str(UID):
               ChanelID= canal["id"]
    else:
     pass
     #print("Error al obtener la lista de canales. Código de estado:", response.status_code)
    try:
        return ChanelID
    except:
        return "failed"

def NChanel(UID,UName):
    # Configuración de la cuenta de ThingSpeak
    API_KEY = "5N6GVZV6GF8QKQSY"
    CHECK_URL = "https://api.thingspeak.com/channels.json"

    # Nombre y descripción del canal que deseas crear
    nombre_canal = str(UID)
    descripcion_canal = str(UName)

    # Realizar la solicitud GET para obtener todos los canales existentes
    params = {"api_key": API_KEY}
    response = requests.get(CHECK_URL, params=params)

    # Verificar el estado de la respuesta
    if response.status_code == 200:
        canales_existentes = response.json()
        
        # Verificar si el nombre del canal ya existe en la lista de canales existentes
        canales_con_mismo_nombre = [canal for canal in canales_existentes if canal["name"] == nombre_canal]
        
        if len(canales_con_mismo_nombre) > 0:
            pass
            #print("Ya existe un canal con el mismo nombre.")
        else:
            # Realizar la creación del canal
            CREATE_URL = "https://api.thingspeak.com/channels.json"
            data = {
                "api_key": API_KEY,
                "name": nombre_canal,
                "description": descripcion_canal,
                "public": False,  # Configurar public como False para evitar gráficas automáticas
                "field1": "Total Flexiones",
                "field2": "Total Extensiones",
                "field3": "Ángulo",
                "field4": "Fuerzas",
                "field5": "Nivel Cumplimiento",
                "field6": "Cantidad Flexiones",
                "field7": "Cantidad Extensiones",
            }
            response = requests.post(CREATE_URL, json=data)

            # Verificar el estado de la respuesta
            if response.status_code == 200:
                canal_creado = response.json()
                canal_id = canal_creado["id"]
            else:
                pass
                #print("Error al crear el canal:", response.text)
    else:
        pass
        #print("Error al obtener la lista de canales:", response.text)

def UploadDataF(apikey,flexion,extension):
 # ThingSpeak API endpoint for individual update
    UPDATE_URL = "https://api.thingspeak.com/update.json"

    # API key of your ThingSpeak channel
    API_KEY = apikey

    field_data = {
            "api_key": API_KEY,

            "field6": flexion,  # Field 6 column
            "field7": extension,  # Field 7 column
        }

    # Perform the individual update request
    response = requests.post(UPDATE_URL, data=field_data)

    # Check the response status
    if response.status_code == 200:
        pass
        #print("Data imported successfully.")
    else:
        pass
        #print("Error importing data:", response.text)

def UploadDataU(apikey,cumplimiento,tflexion,textension):
 # ThingSpeak API endpoint for individual update
    UPDATE_URL = "https://api.thingspeak.com/update.json"

    # API key of your ThingSpeak channel
    API_KEY = apikey

    field_data = {
            "api_key": API_KEY,
            "field5": cumplimiento,  # Field 6 column
            "field1": tflexion,  # Field 6 column
            "field2": textension,  # Field 7 column
        }

    # Perform the individual update request
    response = requests.post(UPDATE_URL, data=field_data)

    # Check the response status
    if response.status_code == 200:
        pass
        #print("Data imported successfully.")
    else:
        pass
        #print("Error importing data:", response.text)

def UploadCSV(apikey,path):
  # ThingSpeak API endpoint for individual update
    UPDATE_URL = "https://api.thingspeak.com/update.json"

    # API key of your ThingSpeak channel
    API_KEY = apikey

    # Path to the CSV file
    csv_file_path = path

    # Read the CSV file
    with open(csv_file_path, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        
        #rows.remove(rows[0])

    # Iterate through the rows of the CSV file
    for row in rows:
        # Prepare the data for individual update
        field_data = {
            "api_key": API_KEY,
            "created_at": row[0],  # Timestamp column
            "field3": row[1],  # Field 3 column
            "field4": row[2],  # Field 4 column

        }

        # Perform the individual update request
        response = requests.post(UPDATE_URL, data=field_data)

        # Check the response status
        if response.status_code == 200:
            print("Data imported successfully.")
        else:
            print("Error importing data:", response.text)
        time.sleep(16)

def dataread(apikey,chanelID,field):
    # URL del canal de ThingSpeak y API Key
    url = 'https://api.thingspeak.com/channels/CHANNEL_ID/fields/FIELD_ID/last.txt'
    api_key = apikey

    # Construir la URL completa
    url = url.replace('CHANNEL_ID', chanelID).replace('FIELD_ID', field) + '?api_key=' + api_key

    # Realizar la solicitud GET a ThingSpeak
    response = requests.get(url)

    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        # Guardar el valor del campo en una variable
        field_value = response.text.strip()
        #print('El valor del campo es:', field_value)
    else:
        pass
        #print('Error al realizar la solicitud:', response.status_code)
    return(field_value)

def data(COM,calibV,calibA):
    #print("start")
    slope = 0.0904
    # Configurar el puerto serie
    puerto = serial.Serial(COM, 9600)  # Reemplaza 'COMX' por el puerto adecuado
    puerto.timeout = 1
    #print("mid1")
    # Enviar comando al controlador Teensy para solicitar datos del pin analógico
    puerto.write(b'R')  # 'R' es un ejemplo de comando, puedes cambiarlo según tu configuración
    #print("mid1")
        # Leer la respuesta del controlador
    respuesta = puerto.readline().strip().decode('utf-8')
    #print("mid1")
        # Procesar la respuesta
    if respuesta:
        value = int(respuesta)
        #print(f"Valor analógico: {value}")
        time.sleep(0)

    # Imprimir el valor leído
    angle= -slope*(value-calibV)-calibA
    print('Angulo:', angle)
    #print('Valor analógico:', value)
    if angle > 0:
        angle = angle * 500/159
    elif angle < 0:
        angle = angle * 100/34
    else:
        angle = 0
    return angle


