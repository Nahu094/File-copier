import Tkinter, tkFileDialog
from colorama import init
from termcolor import colored
import os
import shutil
import sys

#Variables globales
argv = sys.argv
Key = True
File = "DEF"
Fname=" "
Li = "DEF"
Lname = " "
#Obtener ruta del archivo 
App_dir = os.path.abspath(os.curdir)
Copy_dir = str(App_dir)+"/copias"

#Devuelve el directorio del archivo y su nombre, en este caso el archivo a copiar
def directorio():
	print("Cargando archivo...")

	Window = Tkinter.Tk()
	Window.withdraw()

	File = tkFileDialog.askopenfilename(title="Archivo a copiar")
	print("Archivo cargado")
	Name = os.path.basename(File)
	return (File, Name)

#Devuelve el directorio del archivo y su nombre, en este caso la lista de nombres
def directorio_li():
	print("Cargando archivo...")

	Window = Tkinter.Tk()
	Window.withdraw()

	File_li = tkFileDialog.askopenfilename(title="Lista de nombres")
	print("Archivo cargado")
	Name = os.path.basename(File_li)
	return (File_li, Name)

#Copiar archivo
def copiar(nombre, directorio):
	a = str(directorio) #Origen
	Tmp = a.find(".")
	Type = a[Tmp:]
	print(Type)
	Tmp = App_dir+"\\copias\\"+nombre+Type#Destino
	b = Tmp.replace("\\", "/")

	if(os.path.isdir(Copy_dir)):
		pass
	else:
		os.mkdir(Copy_dir)
	
	shutil.copy(a,b)
	print("Copiando desde: "+a)
	print("a: "+b)
	print("Completado")

#Copia multiple desde la lista
def Inicio(File, Li):

	with open (Li) as F:
		x = F.read().splitlines()
		
		for i in x:
			copiar(i, File)
    
		F.close()

#Main noGUI
init()
if (len(argv)>1):
	if (argv[1] == "test"):
		while(Key):
			os.system("cls")
			print colored("Dev mode no gui", "blue")
			print("\n1)copiar archivo")
			print("2)Salir")
			Menu = input()
			if (Menu == 1):
				#Ejecucion del programa
				Key2 = True
				while(Key2):
					os.system("cls")
					File_exist = False
					Li_exist = False
					if File == "DEF":
						print("Archivo:"), colored(" No cargado","red")
						pass
					else:
						print("Archivo:"+ Fname), colored(" Cargado","green")
						File_exist = True
						pass
					if Li == "DEF":
						print("Lista de nombres:"), colored(" No cargado","red")
						pass
					else:
						print("Lista de nombres:"+ Lname), colored(" Cargado","green")
						Li_exist = True
					print("\n1)Cargar archivo a copiar")
					print("\n2)Cargar lista de nombres")
					print("\n3)Comenzar")
					print("\n4)Salir")
					Menu = input()

					if Menu == 1:
						#Cargar directorio
						File, Fname = directorio()
					elif Menu == 2:
						#Cargar lista
						Li, Lname = directorio_li()
					elif Menu == 3:
						#Copiar
						if File_exist == False:
							print colored("Imposible comenzar sin archivo", "red")
							Pause = raw_input("Presione enter para continuar...")
						elif Li_exist == False:
							print colored("Imposible comenzar sin lista", "red")
							Pause = raw_input("Presione enter para continuar...")
						else:
							Inicio(File, Li)
							Pause = raw_input("Presione enter para continuar...")
							pass
					elif Menu == 4:
						#salir
						Key2 = False 
					else:
						os.system("cls")
						print("Opcion invalida")
						Pause = raw_input("Presione enter para continuar...")

			elif Menu == 2:
				#salir
				Key = False
			else:
				os.system("cls")
				print("Opcion invalida")
				Pause = raw_input("Presione enter para continuar...")
