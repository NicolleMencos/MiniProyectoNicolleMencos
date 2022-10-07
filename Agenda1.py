from persona import persona
from io import open

misContactos = [persona(987,'Besti Andrea','casa 1'),persona(765,'Alysha','Casa 2')]

def crearContacto(numero, nombre, direccion):
    misContactos.append(persona(numero, nombre, direccion))
    print("Contacto almacenado...")

def buscarContacto(nombre):
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
    else:
        encontrado = False
        for i in range(len(misContactos)):
            if misContactos[i].verNombre() == nombre:
                print("----------------------------")
                print("El teléfono es.: ", misContactos[i].verNumero())
                print("La dirección es: ", misContactos[i].verDireccion(),)
                print("----------------------------")
                encontrado = True
                break
            else:
                encontrado = False
        if encontrado == False:
            print("Dato no existente...")

def mostrarContactos():
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
    else:
        for i in range(len(misContactos)):
            print('Nombre: ', misContactos[i].verNombre(), ' - ', 'Dirección', misContactos[i].verDireccion(), ' - ', 'Teléfono', misContactos[i].verNumero())

def modificarContacto(nombre):
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
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
        if encontrado:
            nuevoNumero = int(input("Ingrese el nuevo número: "))
            nuevoNombre = input("Ingrese nuevo nombre: ")
            nuevaDireccion = input("Ingrese la nueva dirección: ")
            misContactos[posicion].modificarNumero(nuevoNumero)
            misContactos[posicion].modificarNombre(nuevoNombre)
            misContactos[posicion].modificarDireccion(nuevaDireccion)
            print("Datos actualizados con éxito...")
        else:
            print("Dato no encontrado...")

def eliminarContacto(nombre):
    if len(misContactos) == 0:
        print("La lista esta vacía, no hay contactos que buscar...")
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
        if encontrado:
            misContactos.pop(posicion)
            print("Dato eliminado con éxito...")
        else:
            print("Dato no encontrado...")

def crearReporte():
    documento = open("reporte contactos.html","w")
    documento.write("<!doctype html>\n")
    documento.write("<html>\n")
    documento.write("<head>\n")
    documento.write("\t<title>Agenda 2022</title>\n")
    documento.write("</head>\n")
    documento.write("<body>\n")
    documento.write("\t<center>\n")
    documento.write("\t<h1>Mis contactos</h1>\n")
    documento.write('\t<table border="1">\n')
    documento.write("\t\t<tr>\n")
    documento.write("\t\t\t<td>Número de teléfono</td><td>Nombre</td><td>Dirección</td>\n")
    for i in range(len(misContactos)):
        documento.write("\t\t<tr>\n")
        documento.write("\t\t\t<td>" + str(misContactos[i].verNumero()) + "</td><td>" + misContactos[i].verNombre() + "</td><td>" + misContactos[i].verDireccion() + "</td>")
        documento.write("\t\t</tr>\n")

    documento.write("\t\t</tr>\n")
    documento.write("\t</table>\n")
    documento.write("\t</center>\n")
    documento.write("</body>\n")
    documento.write("</html>")
    documento.close()
    print("Reporte HTML creado con éxito...")

def main():
    op = 0
    while op != 7:
        print("\n+--------------------------+")
        print("|       Agenda 2022        |")
        print("|--------------------------|")
        print("| 1. Crear contacto        |")
        print("| 2. Buscar contacto       |")
        print("| 3. Ver contactos         |")
        print("| 4. Modificar contacto    |")
        print("| 5. Eliminar contacto     |")
        print("| 6. Crear reporte en HTML |")
        print("| 7. Salir del programa    |")
        print("+--------------------------+\n")
        op = int(input("Ingrese el número de opción: "))
        if op == 1:
            numero = int(input("Ingrese el número de teléfono: "))
            nombre = input("Ingrese el nombre: ")
            direccion = input("Ingrese la dirección: ")
            crearContacto(numero, nombre, direccion)
        elif op == 2:
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscarContacto(nombre)
        elif op == 3:
            mostrarContactos()
        elif op == 4:
            nombre = input("Ingrese el nombre del contacto: ")
            modificarContacto(nombre)
        elif op == 5:
            nombre = input("Ingrese el nombre del contacto: ")
            eliminarContacto(nombre)
        elif op == 6:
            crearReporte()
        elif op == 7:
            print("Programa finalizado...")
        else:
            print("Opción incorrecta..")

#iniciar programa
main()
