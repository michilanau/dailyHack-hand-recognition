import cv2
import tkinter as tk
import os
from PIL import Image, ImageTk
from translator import getTextFromImages

def mostrar_vista_previa():
    ret, frame = camara.read()  # Capturar un frame desde la cámara

    if ret:  # Verificar si se capturó correctamente el frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir el frame de BGR a RGB
        imagen = Image.fromarray(frame)  # Crear una imagen PIL desde el frame
        imagen_tk = ImageTk.PhotoImage(imagen)  # Convertir la imagen PIL a una imagen Tkinter

        # Mostrar la imagen en el widget Label de Tkinter
        label_vista_previa.imgtk = imagen_tk
        label_vista_previa.configure(image=imagen_tk)
        label_vista_previa.after(10, mostrar_vista_previa)  # Actualizar la vista previa cada 10 milisegundos

def capturar_imagen():
    global contador
    global temp_dir
    ret, frame = camara.read()  # Capturar un frame desde la cámara

    if ret:  # Verificar si se capturó correctamente el frame
        frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ruta_imagen_temporal = os.path.join(temp_dir, f"imagen_{contador}.png")

        # Guardar la imagen en el directorio temporal
        cv2.imwrite(ruta_imagen_temporal, frame_gris)

        # Guardar la ruta de la imagen en el array
        imagenes.append(ruta_imagen_temporal)
        contador += 1
        translate_images()
        
# Función para traducir el texto
def translate_images():
    global texto
    newText = getTextFromImages(imagenes)
    if(newText == -1):
        imagenes.pop()
    elif (newText != texto and newText != -1):
        texto = newText
        label_texto.config(text=f"Texto: {texto}")

def reset():
    global texto
    global imagenes
    texto = ""
    imagenes = []
    label_texto.config(text=f"Texto: {texto}")

# Inicializar la cámara
camara = cv2.VideoCapture(0)  # El número 0 indica la cámara predeterminada (puede variar en diferentes sistemas)

# Inicialización de variables
imagenes = []
contador = 0
texto = ""
temp_dir = "temp"

#Reseteamos el directorio temporal
for f in os.listdir(temp_dir):
    os.remove(os.path.join(temp_dir, f))

# Configurar ventana de interfaz gráfica
root = tk.Tk()
root.title("Vista Previa y Captura de Imagen")

# Crear un widget Label para mostrar la vista previa
label_vista_previa = tk.Label(root)
label_vista_previa.pack()

# Crear un botón para capturar una imagen
boton_capturar = tk.Button(root, text="Capturar Imagen", command=capturar_imagen)
boton_capturar.pack()

boton_reset = tk.Button(root, text="Reset", command=reset)
boton_reset.pack()

# Contador para el número de imágenes capturadas
label_texto = tk.Label(root, text=f"Texto: {texto}")
label_texto.pack()

# Llamar a la función para mostrar la vista previa
mostrar_vista_previa()

# Función para cerrar la cámara y la ventana al salir
def cerrar_programa():
    camara.release()
    root.destroy()


# Botón para cerrar el programa
boton_salir = tk.Button(root, text="Salir", command=cerrar_programa)
boton_salir.pack()

# Ejecutar el loop principal de la interfaz gráfica
root.mainloop()
