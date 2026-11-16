import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image, ImageFilter

ruta_1 = ('perro.jpg')
ruta_2 = ('paredes.jpg')
ruta_3 = ('paisaje.jpg')
ruta_4 = ('scorsese.jpg')

#Cargamos las imagenes en variables
img_1_perro = cv2.imread(ruta_1)
img_2_paredes = cv2.imread(ruta_2)
img_3_paisaje = cv2.imread(ruta_3)
img_4_scorsese = cv2.imread(ruta_4)

#Lista de redes sociales para la primera funcion
red_social_list = ['Youtube', 'Facebook', 'Instagram', 'Twitter']

#Diccionario de imagenes
imagenes = {
  1: img_1_perro,
  2: img_2_paredes,
  3: img_3_paisaje,
  4: img_4_scorsese
}

#----1----
#Funcion para procesar una imagen
def leer_imagen(imagen, red_social):
    
    red_social = red_social.strip().capitalize()

    if not isinstance(imagen, np.ndarray):
      return ('Como primer parametro debe ingresar una Imagen')


    if len(imagen.shape) == 3 and imagen.shape[2] == 3:
      imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

    match red_social:
      case 'Youtube':
        nueva_imagen = cv2.resize(imagen, (1280,720))
        plt.imshow(nueva_imagen)
        plt.title('Imagen Youtube: 1280 x 720')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        plt.close('all')

      case 'Facebook':
        nueva_imagen = cv2.resize(imagen, (1200,630))
        plt.imshow(nueva_imagen)
        plt.title('Imagen Facebook: 1200 x 630')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        plt.close('all')

      case 'Instagram':
        nueva_imagen = cv2.resize(imagen, (1080,566))
        plt.imshow(nueva_imagen)
        plt.title('Imagen Instagram: 1080 x 566')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        plt.close('all')

      case 'Twitter':
        nueva_imagen = cv2.resize(imagen, (1600,900))
        plt.imshow(nueva_imagen)
        plt.title('Imagen Twitter: 1600 x 900')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        plt.close('all')

      case _:
        print('Ingreso un valor invalido ')

#---2---
#Funcion para equalizar una imagen
def equalizar_imagen(imagen):

  if not isinstance(imagen, np.ndarray):
      return ('Como parametro debe ingresar una Imagen')

  fig, axes = plt.subplots(1, 2, figsize=(12,5))

  if len(imagen.shape) == 2:
      imagen_equalizada = cv2.equalizeHist(imagen)
      axes[0].imshow(imagen)
      axes[0].set_title('Imagen original')
      axes[0].axis('off')

      axes[1].imshow(imagen_equalizada)
      axes[1].set_title('Imagen ecualizada')
      axes[1].axis('off')


  elif len(imagen.shape) == 3 and imagen.shape[2] == 3:
      image_ycrcb = cv2.cvtColor(imagen, cv2.COLOR_BGR2YCrCb)
      Y, Cr, Cb = cv2.split(image_ycrcb)
      Y_equalize = cv2.equalizeHist(Y)
      imagen_ycrcb_equalizada = cv2.merge((Y_equalize, Cr, Cb))
      imagen_equalizada = cv2.cvtColor(imagen_ycrcb_equalizada, cv2.COLOR_YCrCb2RGB)

      axes[0].imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
      axes[0].set_title('Imagen original')
      axes[0].axis('off')

      axes[1].imshow(imagen_equalizada)
      axes[1].set_title('Imagen ecualizada')
      axes[1].axis('off')

      plt.tight_layout()
      plt.show()

  os.makedirs('images', exist_ok=True)
  Image.fromarray(imagen_equalizada).save('images/imagen_ecualizada.jpg')
  Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)).save('images/imagen_original.jpg')

#---3---
#Funcion para aplicar filtros a una imagen
def filtrar_imagen(imagen, filtro):

  if not isinstance(imagen, np.ndarray):
      return ('Como primer parametro debe ingresar una Imagen')

  if filtro not in range(1,10):
    return ('Como segundo parametro debe ingresar un numero del 1 al 9')

  fig, axes = plt.subplots(1,2, figsize=(12,5))

  os.makedirs('figures', exist_ok=True)

  imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
  imagen = Image.fromarray(imagen)

  match filtro:
    case 1:
      
      imagen_blur = imagen.filter(ImageFilter.BLUR)
      print('Filtro Blur Aplicado ')

      axes[0].imshow(imagen)
      axes[0].axis('off')
      axes[0].set_title('Imagen original')

      axes[1].imshow(imagen_blur)
      axes[1].axis('off')
      axes[1].set_title('Imagen Blur')

      plt.tight_layout()
      plt.show()

      figura_blur = fig.savefig('figures/figura_blur.jpg')

    case 2:
      
      imagen_contour = imagen.filter(ImageFilter.CONTOUR)
      print('Filtro Contour Aplicado')
      
      axes[0].imshow(imagen)
      axes[0].axis('off')
      axes[0].set_title('Imagen original')

      axes[1].imshow(imagen_contour)
      axes[1].axis('off')
      axes[1].set_title('Imagen Contour')

      plt.tight_layout()
      plt.show()

      figura_contour = fig.savefig('figures/figura_contour.jpg')

    case 3:
      
      imagen_detail = imagen.filter(ImageFilter.DETAIL)
      print('Filtro Detail Aplicado')
      
      axes[0].imshow(imagen)
      axes[0].axis('off')
      axes[0].set_title('Imagen original')

      axes[1].imshow(imagen_detail)
      axes[1].axis('off')
      axes[1].set_title('Imagen Detail')

      plt.tight_layout()
      plt.show()

      figura_detail = fig.savefig('figures/figura_detail.jpg')

    case 4:
      
      imagen_edge = imagen.filter(ImageFilter.EDGE_ENHANCE)
      print('Filtro Edge Enhance Aplicado')
      
      axes[0].imshow(imagen)
      axes[0].axis('off')
      axes[0].set_title('Imagen original')

      axes[1].imshow(imagen_edge)
      axes[1].axis('off')
      axes[1].set_title('Imagen Edge Enhance')

      plt.tight_layout()
      plt.show()

      figura_edge = fig.savefig('figures/figura_edge_enhance.jpg')

    case 5:
      
      imagen_edge_more = imagen.filter(ImageFilter.EDGE_ENHANCE_MORE)
      print('Filtro Edge Enhance More Aplicado')

      axes[0].imshow(imagen)
      axes[0].axis('off')
      axes[0].set_title('Imagen original')

      axes[1].imshow(imagen_edge_more)
      axes[1].axis('off')
      axes[1].set_title('Imagen Edge Enhance More')

      plt.tight_layout()
      plt.show()

      figura_edge_more = fig.savefig('figures/figura_edge_enhance_more.jpg')

    case 6:
      
      imagen_emboss = imagen.filter(ImageFilter.EMBOSS)
      print('Filtro Emboss Aplicado')
      
      axes[0].imshow(imagen)
      axes[0].axis('off')
      axes[0].set_title('Imagen original')

      axes[1].imshow(imagen_emboss)
      axes[1].axis('off')
      axes[1].set_title('Imagen Emboss')

      plt.tight_layout()
      plt.show()

      figura_emboss = fig.savefig('figures/figura_emboss.jpg')

    case 7:
      
      imagen_find_edges = imagen.filter(ImageFilter.FIND_EDGES)
      print('Filtro Find Edges Aplicado')
      
      axes[0].imshow(imagen)
      axes[0].axis('off')
      axes[0].set_title('Imagen original')

      axes[1].imshow(imagen_find_edges)
      axes[1].axis('off')
      axes[1].set_title('Imagen Find Edges')

      plt.tight_layout()
      plt.show()

      figura_find_edge = fig.savefig('figures/figura_find_edge.jpg')

    case 8:

      imagen_sharpen = imagen.filter(ImageFilter.SHARPEN)
      print('Filtro Sharpen Aplicado')
      
      axes[0].imshow(imagen)
      axes[0].axis('off')
      axes[0].set_title('Imagen original')

      axes[1].imshow(imagen_sharpen)
      axes[1].axis('off')
      axes[1].set_title('Imagen Sharpem')

      plt.tight_layout()
      plt.show()

      figura_sharpen = fig.savefig('figures/figura_sharpen.jpg')

    case 9:

      imagen_smooth = imagen.filter(ImageFilter.SMOOTH)
      print('Filtro Smooth Aplicado')
      
      axes[0].imshow(imagen)
      axes[0].axis('off')
      axes[0].set_title('Imagen original')

      axes[1].imshow(imagen_smooth)
      axes[1].axis('off')
      axes[1].set_title('Imagen Smooth')

      plt.tight_layout()
      plt.show()

      figura_smooth = fig.savefig('figures/figura_smooth.jpg')

#---4---
#Funcion para resaltar contornos a una imagen
def resaltar_contorno_imagen(imagen):
    
    if not isinstance(imagen, np.ndarray):
      return('Debe ingresar una imagen como parametro')

    fig, axes = plt.subplots(1, 3, figsize=(10,5))

    if len(imagen.shape) == 2:
      umbral, imagen_umbralizada = cv2.threshold(
          imagen,
          200,
          255,
          cv2.THRESH_BINARY
      )

      imagen_canny = cv2.Canny(imagen, 100, 200)

    elif len(imagen.shape) == 3 and imagen.shape[2] == 3:
      imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

      umbral, imagen_umbralizada = cv2.threshold(
          imagen_gris,
          127,
          255,
          cv2.THRESH_BINARY)

      imagen_canny = cv2.Canny(imagen_gris, 100, 200)

    axes[0].imshow(cv2.cvtColor(imagen_gris, cv2.COLOR_BGR2RGB))
    axes[0].axis('off')
    axes[0].set_title('Imagen original')

    axes[1].imshow(cv2.cvtColor(imagen_umbralizada, cv2.COLOR_BGR2RGB))
    axes[1].axis('off')
    axes[1].set_title('Imagen umbralizada')

    axes[2].imshow(cv2.cvtColor(imagen_canny, cv2.COLOR_BGR2RGB))
    axes[2].axis('off')
    axes[2].set_title('Imagen filtro canny')

    plt.tight_layout()
    plt.show()

#---Funcion Main\Menu
def main():
  while True:
    print('---Bienvenido a FotoApp---')
    print('1. Leer imagen \n'
          '2. Equalizar imagen \n'
          '3. Darle filtros a la imagen \n'
          '4. Resaltar contorno de la imagen \n'
          '5. Salir de FotoApp')
    try:
      opcion_menu = int(input('Elija su opcion: '))
      print('')

      match opcion_menu:
            case 1:
              print('---Leer una imagen---')
              print('Para leer una imagen debe seguir las siguiente instrucciones ')
      
              while True:
                try:
                  imagen = int(input('- Coloque el numero de la imagen que quiere usar \n'
                                        '1. Imagen 1 --> Perro a Color \n'
                                        '2. Imagen 2 --> Leandro Paredes a Color \n'
                                        '3. Imagen 3 --> Paisaje en Blanco y Negro \n'
                                        '4. Imagen 4 --> Martin Scorsese en Blanco y Negro \n'))
      
                  if imagen not in imagenes:
                    print('Debe elegir una de las opciones ')
      
                  else:
                    imagen = imagenes[imagen]
                    print('Haz elegido una imagen ')
                    break
      
                except ValueError:
                    print('Debe elegir una de las opciones ')
      
              while True:
                red_social = input('- Elija una red social para procesar la imagen con sus dimensiones \n'
                                      'Opciones: - Youtube - Instagram - Facebook - Twitter: ').capitalize()
                              
                if red_social not in red_social_list:
                      print(f'Como segundo parametro debe ingresar algunas de las siguientes opciones: '
                              'Youtube, Facebook, Instagram, Twitter \n')
                else:
                  print('')
                  print('Haz elegido una red social')
                  break
      
              
              print('Leyendo imagen... ')
              leer_imagen(imagen, red_social)
              print('Imagen leida. Volviendo al menu... \n')
              break
      
            case 2:
              print('---Ecualizar una imagen')
              print('Para ecualizar una imagen debe seguir las siguientes instrucciones')
              while True:
                try:
                  imagen = int(input('- Coloque el numero de la imagen que quiere usar \n'
                                        '1. Imagen 1 --> Perro a Color \n'
                                        '2. Imagen 2 --> Leandro Paredes a Color \n'
                                        '3. Imagen 3 --> Paisaje en Blanco y Negro \n'
                                        '4. Imagen 4 --> Martin Scorsese en Blanco y Negro \n'))
      
                  if imagen not in imagenes:
                    print('Debe elegir una de las opciones ')
                  else:
                    imagen = imagenes[imagen]
                    print('A elegido una imagen ')
                    break
                
                except ValueError:
                    print('Debe elegir una de las opciones ')
      
              print('Ecualizando imagen... ')
              equalizar_imagen(imagen)
              print('Imagen ecualizada. Volviendo al menu... \n')
              break
      
            case 3:
              print('---Filtrar una imagen---')
              print('Para darle filtros a una imagen debe seguir las siguientes instrucciones')
      
              while True:
                try:
                  imagen = int(input('- Coloque el numero de la imagen que quiere usar \n'
                                        '1. Imagen 1 --> Perro a Color \n'
                                        '2. Imagen 2 --> Leandro Paredes a Color \n'
                                        '3. Imagen 3 --> Paisaje en Blanco y Negro \n'
                                        '4. Imagen 4 --> Martin Scorsese en Blanco y Negro \n'))
      
                  if imagen not in imagenes:
                    print('Debe elegir una de las opciones ')
                  else:
                    imagen = imagenes[imagen]
                    print('A elegido una imagen ')
                    break
                
                except ValueError:
                    print('Debe elegir una de las opciones ')
              while True:
                try:
                  filtro = int(input('Coloque el numero del filtro que quiere usar \n '
                                    '1. Blur\n' 
                                    '2. Contour\n' 
                                    '3. Detail\n' 
                                    '4. Edge Enhance\n' 
                                    '5. Edge Enhance More\n' 
                                    '6. Emboss\n' 
                                    '7. Find Edges\n' 
                                    '8. Sharpen\n'  
                                    '9. Smooth\n'))
                  
                  if filtro not in range(1,10):
                    print('Debe elegir una de las opciones ')
                  else:
                    print('Haz elegido un filtro')
                    break 
      
                except:
                  print('Debe elegir una de las opciones')

              print('Creando figura...')
              filtrar_imagen(imagen, filtro)
              print('Figura creada. Volviendo al menu...')
              break
      
            case 4:
              print('---Aplicar contorno a una imagen---')
              print('Para Aplicar contorno a una imagen debe seguir las siguiente instrucciones ')
      
              while True:
                try:
                  imagen = int(input('- Coloque el numero de la imagen que quiere usar \n'
                                        '1. Imagen 1 --> Perro a Color \n'
                                        '2. Imagen 2 --> Leandro Paredes a Color \n'
                                        '3. Imagen 3 --> Paisaje en Blanco y Negro \n'
                                        '4. Imagen 4 --> Martin Scorsese en Blanco y Negro \n'))
      
                  if imagen not in imagenes:
                    print('Debe elegir una de las opciones ')
      
                  else:
                    imagen = imagenes[imagen]
                    print('Haz elegido una imagen ')
                    break
      
                except ValueError:
                    print('Debe elegir una de las opciones ')

              print('Creando figura...')      
              resaltar_contorno_imagen(imagen)
              print('Figura creada. Volviendo al menu...')
              break

            case 5:
              print('Gracias por utilizar FotoApp!')
              break

            case _:
              print('Debe elegir una de las opciones')

    except:
      print('\n La opcion no es correcta ')

main()