# File-copier
File-copier es un programa que copia un archivo y crea multiples copias de este con distintos nombres previamente dados en un archivo de texto (.txt).

*** Interfaz Grafica ***
--
![image](https://user-images.githubusercontent.com/81646953/191968371-65b71ae4-8a7d-4aad-9d54-e0e46d247317.png)

este programa cuenta con una interfaz grafica de facil entendimiento, con el primer boton se elige el archivo a copiar. Esto abrira una ventana selectora de archivos

![image](https://user-images.githubusercontent.com/81646953/191968767-8b601a2d-c923-4771-a96b-d644edaf3915.png)

Ahi cargara el archivo que se desea clonar.

Con el segundo boton se carga el archivo de texto en el que se deben encontrar los nombres para los archivos a ser creados, esta lista de nombres tiene que estar en formato archivo de texto de windows(.txt) y sus nombres deben estar dados por saltos de linea (separados por enter).

![image](https://user-images.githubusercontent.com/81646953/191969512-d80ac5e2-e4ae-43f7-a498-1979d0890442.png)

Una vez los 2 archivos esten cargados el programa informara que se encuentra listo para la clonacion

![image](https://user-images.githubusercontent.com/81646953/191969852-7a2e8039-7f9e-41b0-92d9-6a9588cf9192.png)

clickeando el boton Copiar se iniciara el proceso de clonado. Cuando el programa finalice la copia lo informara con una bandera verde

![image](https://user-images.githubusercontent.com/81646953/191970318-02873a8a-e89b-4fc5-8b13-77a495b34515.png)

Los archivos copiados se encontraran en la ruta del programa, alli encontrara una carpeta llamda "copias", (si esta carpeta no existia el programa se encargara de crearla)

![image](https://user-images.githubusercontent.com/81646953/191970895-241d595d-47f6-4d5a-8ee7-cde88b6c406a.png)

![image](https://user-images.githubusercontent.com/81646953/191970998-bb2ff7c5-0dc8-41a6-b6d2-229b3d94bf62.png)

*** Como construir ***
###Necesita Python 3
--
Crear un entorno virtual y activarlo o probarlo baremetal
``python -m venv venv ``
``.\venv/Scripts/activate ``
Instalar dependencias del archivo pyproject.toml
``pip install . ``
Lanzar Copiador.py
``python Copiador.py ``