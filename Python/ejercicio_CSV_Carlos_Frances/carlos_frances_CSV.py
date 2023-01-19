import csv, smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Se importan las librerias necesarias para trabajar con CSVs y correo

fila=[]

#Se crea un procedimiento que consiga leer la linea que nos interese del CSV para extraer los datos necesarios
with open('ejercicio-14-oct.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 3:
            fila=(str(row))
        else:
            line_count += 1
 
#Una vez tenemos la linea que nos interesa, creamos un array de cadenas gracias a un split y eliminamos los caracteres molestos           
fila=fila.replace("'","")
fila=fila.split(",")

#Asignamos una variable a cada campo necesario. en este caso queremos conocer el DESTINATARIO, DESCRIPCION DEL CORREO, Y CUERPO DEL CORREO
destinatario=fila[1]
descripcion=fila[2]
cuerpo=fila[3]

#Hacemos el setup del correo y su protocolo de envio
port = 465 
smtp_server = "smtp.gmail.com"
sender_email = "carlos98frances@gmail.com"
receiver_email = destinatario

#Contraseña de aplicación sin la que no se puede enviar correos desde python
password = "nbjayvzmfwdcqhza"
msg=MIMEMultipart()
message = cuerpo
msg['Subject']=descripcion
msg.attach(MIMEText(message+"\nAPRUEBEME POR FAVOR", 'plain'))
context = ssl.create_default_context()

#Con este metodo se envía el correo. Como ya hemos guardado todo en variables no hay que escribir nada a mano
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    #Logear en tu correo para poder enviar el mail
    server.login(sender_email, password)
    #Finalmente se envía el mail con esta linea
    server.sendmail(sender_email, receiver_email, msg.as_string())
