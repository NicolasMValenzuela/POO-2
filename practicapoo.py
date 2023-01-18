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