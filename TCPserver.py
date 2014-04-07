#!/usr/bin/env python
 
#importamos el modulo socket
import socket
import threading, queue
import os

#instanciamos un objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("abre socket")
#Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
#Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
s.bind(("", 1111))
 
#Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
#El numero de conexiones entrantes que vamos a aceptar
s.listen(5)

#maximum number thread
maxThread=350
maxQueue=50

def servConv():
    
    while True:
        soc = q.get(True)     
        dirc = soc.recv(1536).decode()    
        nombre = "/tmp/" + dirc
        f = open(nombre, "wb")
        soc.send("ok".encode())
        while True:
            #Recibimos el mensaje, con el metodo recv recibimos datos y como parametro 
            #la cantidad de bytes para recibir
            recibido = soc.recv(1536)       
            if len(recibido)==1:
                if recibido.decode() == "z":
                    break
            f.write(recibido)
            #Devolvemos el mensaje al cliente
            soc.send("ok".encode())
    
        f.close()

        #llamar script conv.py
        split = dirc.split(".")
        convert = "/tmp/"+split[0]+".mp4"
        os.system('python ~/convMain.py '+nombre+" "+convert)
    
        folder=str(split[0]+".mp4").encode()
        soc.send(folder)
        fn = open(convert, "rb")
        env= soc.recv(1536).decode()
        if env=="rc":         
            for linea in fn:
                soc.send(linea)
                soc.recv(1536).decode()
        fn.close()
        soc.send("z".encode())
        print(soc.recv(1536).decode())
        os.system('python ~/streamMain.py '+convert)    
        soc.close()
        print("Archivo: " + nombre + " convertido y enviado")
        q.task_done()

q=queue.Queue(maxQueue)

for i in range(maxThread):
    t=threading.Thread(target=servConv)
    t.daemon=True
    t.start()

while True:
    cn,addr = s.accept()
    q.put(cn,True)
   
print("Adios.")
 
#Cerramos la instancia del socket cliente y servidor
s.close()

exit()
