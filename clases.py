class libro:
    def __init__(self, titulo:str, autor:str, año:int) -> None:

        self.titulo = titulo
        self.autor = autor
        self.año = año 


        


    def retornar_informacion (self) -> None:
        print (f"titulo: {self.titulo}, autor: {self.autor}, año de publicacion: {self.año}")



class rectangulo:
    
    def __init__(self, base: float, altura:float) -> None:
        
        self.base = base
        self.altura = altura

    def retornar_perimetro (self) -> float:
        perimetro = (self.base * 2 + self.altura * 2)

        return perimetro

    def retornar_area (self) -> float:
        area = (self.base * self.altura)

        return area 
    

class animal:
    
    def __init__(self, nombre: str) -> None:

        self.nombre = nombre

class perro (animal):

    def __init__(self, nombre: str, guau: str) -> None:

        super().__init__(nombre)

        self.guau = guau

    
    def sonido_perro (self) -> None:
        print (f"sonido del perro: {self.guau}")
        
        
class gato (animal):

    def __init__(self, nombre: str, miau: str) -> None:
        super().__init__(nombre)

        self.miau = miau

    def sonido_gato (self) -> None:
        print (f"sonido del gato: {self.miau}")


class cuenta_bancaria:

    def __init__(self, titular: str, saldo:float) -> None:

        self.titular = titular 
        self._saldo = saldo 

    def obtener_saldo (self) -> None:

        print (f"tu saldo es de {self._saldo}")
        opcion = input ("desea depositar o retirar el saldo: ")

        if opcion == "depositar":
            print("depositando......fue un exito.")
        elif opcion == "retirar":
            print ("retirando......fue un exito.")
        else:
            print ("error")

