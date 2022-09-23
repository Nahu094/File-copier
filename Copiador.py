import Tkinter, tkFileDialog
from colorama import init
from termcolor import colored
import os
import shutil
import sys
import Tkinter as tk
from Tkinter import *


#Variables globales
argv = sys.argv
Key = True
File = "DEF"
Fname=" "
Li = "DEF"
Lname = " "
File_exist = False
Li_exist = False

#Obtener ruta del archivo 
App_dir = os.path.abspath(os.curdir)
Copy_dir = str(App_dir)+"/copias"

#Devuelve el directorio del archivo y su nombre, en este caso el archivo a copiar
def directorio():
	print("Cargando archivo...")

	Window = Tkinter.Tk()
	Window.withdraw()

	File = tkFileDialog.askopenfilename(title="Archivo a copiar")

	Name = os.path.basename(File)
	File_exist = True
	print("Archivo cargado")
	return (File, Name)

#Devuelve el directorio del archivo y su nombre, en este caso la lista de nombres
def directorio_li():
	print("Cargando archivo...")

	Window = Tkinter.Tk()
	Window.withdraw()

	File_li = tkFileDialog.askopenfilename(title="Lista de nombres")
	Name = os.path.basename(File_li)
	Li_exist = True
	print("Archivo cargado")
	return (File_li, Name)

#Copiar archivo
def copiar(nombre, directorio):
	a = str(directorio) #Origen
	Tmp = a.find(".")
	Type = a[Tmp:]
	print(Type)
	Tmp = App_dir+"\\copias\\"+nombre+Type#Destino
	b = Tmp.replace("\\", "/")
	print(Copy_dir)
	if(os.path.isdir(Copy_dir)):
		pass
	else:
		os.mkdir(Copy_dir)
	
	shutil.copy(a,b)
	print("Copiando desde: "+a)
	print("a: "+b)
	print("Completado")

#Copia multiple desde la lista
def inicio(File, Li):

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
							inicio(File, Li)
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
				exit()
				Key = False
			else:
				os.system("cls")
				print("Opcion invalida")
				Pause = raw_input("Presione enter para continuar...")
# Inicio

#Label no se puede copiar, error no cambia la label original

class Application(Frame):
	def fload(self):
		#
		File,Fname = directorio()
		self.lbl_Fresult.configure(text="Archivo:{} cargado".format(Fname))
		self.File.set(File)
		self.Fname.set(Fname)
		self.File_exist.set(value=True)
		print(self.File.get())
		if self.File_exist.get() and self.Li_exist.get():
			self.lbl_Sresult.configure(text = "Listo para copiar")
			self.lbl_Sresult.configure(bg = "yellow")

	def lload(self):
		#
		Li, Lname = directorio_li()
		self.lbl_Lresult.configure(text="Archivo:{} cargado".format(Lname))
		self.Li.set(Li)
		self.Lname.set(Lname)
		self.Li_exist.set(value=True)
		print(self.Li.get())
		if self.File_exist.get() and self.Li_exist.get():
			self.lbl_Sresult.configure(text = "Listo para copiar")
			self.lbl_Sresult.configure(bg = "yellow")

	def start(self):
		if self.File_exist.get() and self.Li_exist.get():
			inicio(self.File.get(), self.Li.get())
			self.lbl_Sresult.configure(text = "Copiado exitosamente")
			self.lbl_Sresult.configure(bg = "green")
		else:
			self.lbl_Sresult(text = "No se puede copiar sin archivos")
			self.lbl_Sresultconfigure(bg = "purple")

	def createWidgets(self):
		#variables
		self.File_exist = tk.BooleanVar(value=False)
		self.Li_exist = tk.BooleanVar(value=False)
		self.File = tk.StringVar(value="DEF")
		self.Fname= tk.StringVar(value=" ")
		self.Li = tk.StringVar(value="DEF")
		self.Lname = tk.StringVar(value=" ")
		#botones
		self.btn_Fload = Button(self)
		self.btn_Fload["text"] = "Cargar archivo a copiar"
		self.btn_Fload["command"] =  self.fload

		self.btn_Fload.grid(row=0, column=1, pady=10)

		self.btn_Lload = Button(self)
		self.btn_Lload["text"] = "Cargar lista de nombres"
		self.btn_Lload["command"] =  self.lload

		self.btn_Lload.grid(row=1, column=1, pady=10)

		self.btn_Start = Button(self)
		self.btn_Start["text"] = "Copiar"
		self.btn_Start["fg"]   = "red"
		self.btn_Start["command"] =  self.start

		self.btn_Start.grid(row=2, column=1, pady=10)

		self.lbl_Fresult = Label(self)
		self.lbl_Fresult["text"] = "Archivo:No cargado"

		self.lbl_Fresult.grid(row=0, column=2, pady=10)

		self.lbl_Lresult = Label(self)
		self.lbl_Lresult["text"] = "Lista:No cargado"

		self.lbl_Lresult.grid(row=1, column=2, pady=10)

		self.lbl_Sresult = Label(self)
		self.lbl_Sresult["text"] = "Cargar archivos..."
		self.lbl_Sresult["bg"] = "red"

		self.lbl_Sresult.grid(row=2, column=2, pady=10)
	def __init__(self, master=None):
	    Frame.__init__(self, master)
	    self.pack()
	    self.createWidgets()

root = Tk()
root.title("Copiador de archivos")
root.resizable(width=False, height=False)
app = Application(master=root)
root.mainloop()
root.destroy()

