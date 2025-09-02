import os
import re
import shutil
import tkinter as tk
from tkinter import filedialog, Frame, Button, Label, messagebox

APP_DIR = os.path.abspath(os.curdir)
COPY_DIR = os.path.join(APP_DIR, "copias")
# validar guines o caracteres invalidos
VALID_NAME = re.compile(r"^[\w\-. ]+$")

def sanitize_name(nombre: str) -> str:
    """
    Valida el nombre para archivo.
    Reemplaza caracteres inválidos por un guion bajo
    """
    if not VALID_NAME.match(nombre):
        sanitized = re.sub(r"[^\w\-. ]", "_", nombre)
        return sanitized.strip() or "default"
    return nombre.strip()


def copy_file(origen: str, nombre: str) -> None:
    """
    Copia un archivo en la carpeta 'copias' y lo renombra

    Args:
        origen (str): Ruta del archivo original.
        nombre (str): Nuevo nombre del archivo (sin extensión)
    """
    try:
        extension = os.path.splitext(origen)[1]
        nombre = sanitize_name(nombre)
        destination = os.path.join(COPY_DIR, nombre + extension)

        os.makedirs(COPY_DIR, exist_ok=True)
        shutil.copy(origen, destination)

        print(f"Copiando desde {origen} hacia {destination}")
    except Exception as e:
        raise RuntimeError(f"Error copiando archivo: {e}") from e


def copy_list(origen: str, lista: str) -> None:
    """
    Copia un archivo varias veces usando una lista de nombres

    Args:
        origen (str): Ruta del archivo original.
        lista (str): Ruta del archivo de texto con los nombres
    """
    with open(lista, encoding="utf-8") as f:
        for nombre in f.read().splitlines():
            if nombre.strip():
                copy_file(origen, nombre)


class FileCopierApp(Frame):
    """	
    GUI de la app: permite cargar un archivo base, una lista de nombres,
    y generar copias automáticamente.
    """

    def __init__(self, master=None):
        super().__init__(master)
        self.file_path = None
        self.list_path = None
        self.pack()
        self.create_widgets()

    def load_file(self):
        self.file_path = filedialog.askopenfilename(title="Archivo a copiar")
        if self.file_path:
            self.lbl_file.configure(text=f"Archivo: {os.path.basename(self.file_path)}")

    def load_list(self):
        self.list_path = filedialog.askopenfilename(title="Lista de nombres")
        if self.list_path:
            self.lbl_list.configure(text=f"Lista: {os.path.basename(self.list_path)}")

    def start_copy(self):
        if self.file_path and self.list_path:
            try:
                copy_list(self.file_path, self.list_path)
                self.lbl_status.configure(text="Copiado exitosamente", bg="green")
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.lbl_status.configure(text="Error en la copia", bg="red")
        else:
            self.lbl_status.configure(text="Faltan archivos", bg="red")

    def create_widgets(self):
        self.btn_file = Button(self, text="Cargar archivo", command=self.load_file)
        self.btn_file.grid(row=0, column=0, padx=10, pady=10)

        self.btn_list = Button(self, text="Cargar lista de nombres", command=self.load_list)
        self.btn_list.grid(row=1, column=0, padx=10, pady=10)

        self.btn_start = Button(self, text="Copiar", fg="red", command=self.start_copy)
        self.btn_start.grid(row=2, column=0, padx=10, pady=10)

        self.lbl_file = Label(self, text="Archivo: No cargado")
        self.lbl_file.grid(row=0, column=1)

        self.lbl_list = Label(self, text="Lista: No cargada")
        self.lbl_list.grid(row=1, column=1)

        self.lbl_status = Label(self, text="Esperando...", bg="yellow")
        self.lbl_status.grid(row=2, column=1)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("File Copier")
    root.resizable(width=False, height=False)
    app = FileCopierApp(master=root)
    root.mainloop()
