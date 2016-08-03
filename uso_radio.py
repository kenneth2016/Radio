from radio import Radio 
ra= Radio ("Sony")
desea_continuar = True
while desea_continuar:
	if ra.encendido:
		print("1.subir volumen\n 2.bajar volumen\n 3.subir emisora\n 4.bajar emisora\n 5.cambiar estacion\n 6.apagar")
		opc= int(input("elija una opcion: "))

		if opc==1:
			ra.subir_volumen()
		if opc==2: 
			ra.bajar_volumen()
		if opc==3:
			ra.subir_estacion()
		if opc==4:
			ra.bajar_estacion()
		if opc==5:
			ra.cambiar()
		if opc==6:
			ra.apagar()
	else:
		print("1.encender\n 2.salir\n")
		opc= int(input("elija una opcion: "))
		if opc==1:
			ra.encender()
		if opc==2:
			desea_continuar=False

	print("marca:",ra.marca)
	print("esta encendido :",ra.encendido)
	print("volumen:",ra.volumen)
	print("emisora FM:",ra.emisora_FM)
	print("emisora AM:",ra.emisora_AM)
	print("emisora:",ra.en_FM)
