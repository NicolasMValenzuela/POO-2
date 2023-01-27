'''1. Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y
“print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos.
2. Agregarle a la clase anterior un constructor que reciba nombre y edad.
3. Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.
4. Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la
del objeto actual.
5. Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad
mayor.
6. Agregar un método estático “dump_csv” que reciba el nombre de un archivo, una lista de
personas y genere un archivo CSV separado por comas con los datos de cada persona.
7. Agregar un método estático “load_csv” que reciba el nombre de un archivo y devuelva una lista
de objetos Persona.'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor_que(self, oponente):
        self.es_mas_grande = False
        if self.edad > oponente.edad:
            self.es_mas_grande = True
            mensaje = f'Es mayor que {oponente.nombre}' 
        else:
            mensaje = f'Es menor que {oponente.nombre}'

        return mensaje

    def es_mayor_de_edad(self):
        mensaje= 'menor'
        self.es_mayor = False
        if self.edad >= 18:
            self.es_mayor = True
            mensaje= 'mayor'
        else:
            pass
        return mensaje

    @staticmethod
    def get_mayor(persona1, persona2):
        if persona1.edad > persona2.edad:
            return print(persona1.nombre)
        else:
            return print(persona2.nombre)
    
    @staticmethod
    def dump_csv(lista):
        try:
            texto = open('dump_csv2.txt','wt')
            for elemento in lista:
                nombre = elemento.nombre
                edad = str(elemento.edad)
                texto.write(nombre+';'+edad+'\n')
            print('archivo creado correctamente')
        except OSError:
            print('No se pudo crear el archivo')
        finally:
            try:
                texto.close()
            except NameError:
                pass   

    @staticmethod
    def load_csv():
        lista = []
        try:
            texto = open('dump_csv2.txt','rt')
            linea= texto.readline()
            while linea:
                nombre, edad = linea.split(';')
                edad = edad.strip('\n')
                linea = texto.readline() 
                lista.append({nombre, edad})
            print('archivo creado correctamente')
            print(lista)
        except OSError:
            print('No se pudo crear el archivo')
        finally:
            try:
                texto.close()
            except NameError:
                pass   



    def set_nombre(self):
            self.nombre = input('Ingrese un nombre: ')
            
    def set_edad(self):
            self.edad = int(input('ingrese una edad: '))

    def get_nombre(self):
            print(self.nombre,'Es el nombre ingresado')

    def get_edad(self):
            print(self.edad,'Es la edad ingresada')

    def print_persona(self, es_mayor):
            print('El nombre de la persona es: ', self.nombre, 'y la edad es: ',self.edad, 'y es', es_mayor ,'de edad')
 
lista= [] 

marcos = Persona('Marcos', 15)

for i in range(4):
    lista.append(Persona(input('Ingrese un nombre: '), int(input('Ingrese una edad: '))))
            
marcos.dump_csv(lista)