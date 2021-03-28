from random import randint

class Televisao:
    def __init__(self):
        self.__canal_inicial = 1
        self.__tv_desligada = 1

    @property
    def canal_inicial(self):
        return self.__canal_inicial

    @property
    def tv_desligada(self):
        return self.__tv_desligada

    def ligar(self):
        self.__tv_desligada = 0
        print("Tv Ligada")

    def desligar(self):
        self.__tv_desligada = 1
        print("Tv Desligada")

    def subir_canal(self):
        if self.tv_desligada == 1:
            print("Tv Desligada, nao adianta subir canal!")
        else:
            self.__canal_inicial += 1
            print(self.__canal_inicial)

    def descer_canal(self):
        if self.tv_desligada == 1:
            print("Tv Desligada, nao adianta descer canal!")
        else:
            self.__canal_inicial -= 1
            print(self.__canal_inicial)

    def canal_aleatorio(self):
        self.__canal_inicial = randint(1,100)
        print(self.__canal_inicial)
        
tv = Televisao()
tv.ligar()
tv.desligar()
tv.subir_canal()
tv.subir_canal()
tv.ligar()
tv.subir_canal()
tv.descer_canal()
tv.desligar()
tv.descer_canal()
tv.ligar()
tv.canal_aleatorio()
print(tv.canal_inicial)
tv.desligar()