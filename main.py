from machine import Pin
import network
from time import sleep as delay
import urequests as rq

led = Pin(2, Pin.OUT)
led.value(1)
#-------------------------------- Funcoes Auxiliares --------------------------------
#-----> Conecta Wifi <-----
def conectaWifi():
    wifi = network.WLAN(network.STA_IF)
    print("\n\n--> Ativando...\n")
    wifi.active(True)
    while(not wifi.active()):
        pass
    print("--> Interface Ativada!\n\n")
    print("--> Conectando...\n")
    wifi.connect("Habitat", "InovacaoH@bitat")
    while not wifi.isconnected():
        pass
    led.value(0)
    print(f"--> Conectado! ====< IP: {wifi.ifconfig()[0]} >====\n\n")
    
    titulo = "EduardoTeste"
    print(f"Título Do Projeto: {titulo}\n\n")

conectaWifi()

#-----> Constantes E Variáveis <-----
cont = 0
http_readers = {'content-type': 'application/json'}
link = 'https://api.thingspeak.com/update?api_key=EF3NDQ76RR3XII4Y'

while True:
    delay(20)
    cont += 1
    writeCloud = {'field1':45, 'field2': 56}
    rq.post(
        link,
        json = writeCloud,
        headers = http_readers
        )
    print(f"{cont} Enviado!\n")
    
    
    


    
