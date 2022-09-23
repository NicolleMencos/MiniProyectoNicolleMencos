from persona import persona 
misContactos = []

def crearContacto(nombre, numero, direccion):
   misContactos.append(persona(nombre, numero, direccion))
   print("Contacto almacenado...")

def buscarContacto(nombre):
    if len(misContactos) == 0:
      print("La lista está vacia, no hay contactos...")
    else:
      encontrado = False
      for i in range(len(misContactos)):
          if misContactos[i].verNombre() == nombre:  
            print("El telefono es: ", misContactos[i].verNumero())
            print("La direccion es:", misContactos[i].verDireccion())
            break
          else:
            encontrado = False
            if encontrado == False:
              print("Dato no existente...")

def mostrarContacto():
  if len(misContactos)  == 0:
    print("La lista está vacia, no hay contactos para buscar...")
  else:
    for i in range (len(misContactos)):
      print('Nombre:',misContactos[i].verNombre(),'Direccion',misContactos[i].verDireccion(), 'telefono',misContactos[i].verNumero())

def modificarContacto():
   def buscarContacto(nombre):
    if len(misContactos) == 0:
      print("La lista está vacia, no hay contactos...")
    else:
      encontrado = False
      posicion = None 
      for i in range(len(misContactos)):
          if misContactos[i].verNombre() == nombre:
            posicion = i   
            encontrado = True
            break
          else:
            encontrado = False
            if encontrado == True:
              nuevoNombre = int(input("Ingrese el nuevo nombre: "))
              nuevoNumero = int(input("Ingrese el nuevo número: "))
              nuevaDireccion = int(input("Ingrese la nueva direccion: "))
              misContactos[posicion].modificarNombre(nuevoNombre)
              misContactos[posicion].modificarNumero(nuevoNumero)
              misContactos[posicion].modificarDireccion(nuevaDireccion)
              print("Datos actualizados con exito...")
            else:
               print("Dato no encontrado...") 


def main():
    op = 0
    while op != 7:
      print("---------------------AGENDA TELEFONICA---------------")
      print("1. Crear contacto")
      print("2. Buscar contacto")
      print("3. Ver contacto")
      print("4. Modificar contacto")
      print("5. Eliminar contacto")
      print("6. Crear reporte en HTML")
      print("7. Salir del programa \n\n")
      op= int(input("Ingrese el número de opción"))
      if op ==1:
         nombre  = int(input("Inngrese su nombre"))
         numero = int(input("Ingrese su numero"))
         direccion = int(input("Ingrese su direccion"))
         crearContacto(nombre, numero, direccion)
      elif op == 2:
         nombre = input("Ingrese el nombre del contacto a buscar")
         buscarContacto(nombre)
      elif op ==3:
       mostrarContacto()
      elif op ==4:
       nombre = input("Ingrese el nombre del contacto:")
       modificarContacto(nombre)      
    #INICIAR PROGRAMA


main()