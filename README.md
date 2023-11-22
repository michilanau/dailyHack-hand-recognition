# 👨🏻‍💻 DailyHack HackEPS Lleida 2023

Soy Miguel Ángel Lanau 👋, esta es mi solución al dailyHack del Hackaton de Lleida 2023, HackEPS.
 
refs: [REPO DEL RETO](https://github.com/FerranAD/dailyhack2023)

# 📜 Descripción
Se ha realizado en python un modelo de reconocimiento de gestos de manos, los cuales son los siguientes:

<img align="center" src="categories.png" height="350px" width="350px"/> 
  
|                |                 |
|----------------|-----------------|
| forma de 'C'   |  forma d' 'L'   |
| des de sota    |   'OK'          |
| puny           | palma           |
| puny de perfil | palma de perfil |
| index          | polze           |


Además se ha realizado una traducción de estos gestos a letras, de forma que podamos utilizarlos para escribir en lenguaje natural.
Las traducciones serían las siguientes:


| Gestos          | Símbolo |
|-----------------|-------  |
| palm            |         |
| l+l             | a       |
| l+fist          | b       |
| l+thumb         | c       |
| l+ok            | d       |
| l+c             | e       |
| fist+fist       | f       |
| fist+l          | g       |
| fist+thumb      | h       |
| fist+ok         | i       |
| fist+c          | j       |
| thumb+l         | k       |
| thumb+fist      | l       |
| thumb+thumb     | m       |
| thumb+ok        | n       |
| thumb+c         | ñ       |
| ok+l            | o       |
| ok+fist         | p       |
| ok+thumb        | q       |
| ok+ok           | r       |
| ok+c            | s       |
| c+l             | t       |
| c+fist          | u       |
| c+thumb         | v       |
| c+ok            | w       |
| c+c             | x       |
| c+palm          | y       |
| l+palm          | z       |

Por último, se ha realizado una interfaz gráfica que permite introducir a través de la webcam los diferentes signos, y va mostrando el texto generado.
Entre las funciones de la interfaz tendremos la posibilidad de Capturar una imagen, resetear el texto y Salir.

<img align="center" src="interfaz.png" height="350px" width="350px"/> 

# 💁‍♂️ Requisitos
- Python 3.10 o inferior (Si se usa alguna versión superior es posible que no esté disponible alguna de las dependencias siguientes)
- PyTorch
- OpenCV
- Matplotlib
- Pillow
- tkinter

# 🗿 Funcionamiento

Para el funcionamiento bastaría con ir capturando las imágenes de los diferentes signos. 

**RECOMENDABLE** utilizar un fondo oscuro, ya que el entrenamiento del modelo se ha hecho con imágenes en blanco y negro con una mano blanca sobre fondo negro.

Pongo un gif en el que se puede ver un ejemplo de funcionamiento. La calidad no es muy buena, osea que en el directorio raiz del repo subiré el video de la prueba.

![GIF Funcionamiento](https://github.com/michilanau/dailyHack-hand-recognition/blob/14a42d43db2c2a7bd5ef5d11abf27184c998f6d0/gifFuncionamiento.gif)

# 🛠️ Desarrollo

El primer paso para la solución del reto ha sido crear y entrenar un modelo capaz de indentificar los diferentes gestos de las manos.

Para ello, se ha optado por reorganizar la estructura de carpetas del dataset de fotos, clasificando los gestos en unicamente una carpeta por gesto. De esta manera, en mi opinión, queda sintácticamente más ordenado.

A continuación, en el fichero ``modelCreator.py`` se ha realizado todo el código necesario para el entrenamiento y creación del modelo, dando como resultado el fichero ``best_model.pth``.

Este lo emplearemos para la traducción imágen -> gesto. En el fichero ``classifier.py`` encontraremos la función encargada de esto. En ``translator.py`` haciendo uso de esta función anteriormente mencionada y del diccionario que se encargará de realizar los mapeos de gestos a letras y espacios, situado en ``translation.py``, somos capaces de transformar un array de imágenes a lenguaje natural.

Por último llegamos a nuestra interfaz, a través de esta podremos capturar gestos de nuestra mano y ver como se van transformando en un texto. Todo esto lo podremos encontrar en ``cam.py``.

# 🚀 Arranque
Para el arranque de la aplicación deberemos lanzar el siguiente comando:
```
py src/cam.py
```
