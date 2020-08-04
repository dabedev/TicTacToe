arr, x, y = [[],[],[]], 0, 0
#Definimos las variables que utilizaremos durante la creación del algoritmo
for x in range(0,3,1): #Creamos el bucle que indicará los subarrays de la matriz
	for y in range(0,3,1): #Creamos el bucle que indicará los elementos del subarray
		user_input = input() #Obtenemos la entrada de datos del usuario
		if not user_input.upper() in ["X", "O"]: #Verificamos que haya ingresado una X o una O
			print("Debes ingresar X/O")
		else: #Si todo está correcto, lo pusheamos al último elemento del subarray indicado, también es válido arr[INT][INT]
			arr[x].append(user_input.upper())
x=0 #Reestablecemos el valor de X así ahorramos recursos de la RAM al no declarar otra variable
print("El resultado es:") 
while x < len(arr): #Iteramos con un bucle para obtener los subarrays de la matriz
	print(arr[x][0] + " " + arr[x][1] + " " + arr[x][2] + " ")
	x+=1