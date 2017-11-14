import os
#Variable para detectar el driver el sensor
ds18b20 = ''
#sudo nano /boot/config.txt 
#dtoverlay=w1-gpio
#sudo reboot
#sudo modprobe w1-gpio
#sudo modprobe w1-therm

#se busca el id del dispositivo
def configuracion():
	global ds18b20
#Se busca en el directorio de la existencia del driver	
	for i in os.listdir('/sys/bus/w1/devices'):
		if i != 'w1_bus_master1':
			ds18b20 = i

def leer():
#	global ds18b20
#	se ubica el archivo donde se almacena la informacion
# recolectada por el sensor
	location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
#Se abre el archivo donde esta almacenada la informacion
	tfile = open(location)
	text = tfile.read()
	tfile.close()
#Se obtiene la segunda linea del archivo
	secondline = text.split("\n")[1]
#Se obtiene la informacion de la temparatura que se encuentra en la segunda
#Linea
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
#Se convierte la temperatura a celsius
	temperature = temperature / 1000
	return temperature
	
def cicloprincipal():
	while True:
		if leer() != None:
			print "La temperatura actual es : %0.3f C" % leer()

def detener():
	pass

if __name__ == '__main__':
	try:
		configuracion()
		cicloprincipal()
	except KeyboardInterrupt:
		detener()
