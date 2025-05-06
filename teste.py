# print("Hello World")
# print("Hello World2")

 # Revisão Herança (base para o Django: classe, herança, construtor)

# # 1) Herança simples
# class Animal:
#     def falar(self):
#         pass
#
# class Cachorro(Animal):
#     def falar(self):
#         print("Au, au.")
#
# dog = Cachorro()
# dog.falar()

# # 2) Herança com construtor
# class Pessoa:
#     def __init__(self, nome):
#         self.nome = nome
#
# class Estudante(Pessoa):
#     def __init__(self, nome, matricula):
#         super().__init__(nome)
#         self.matricula = matricula
#
# estudante1 = Estudante('Carlinhos', '01234')
# print(estudante1.nome)
# print(estudante1.matricula)

# # 3) Injecao de dependencia simples
#
# class Mensagem:
#     def enviar(self, texto):
#         print(f"Mensagem enviada: {texto}") # fstring
#
# class Usuario():
#     def __init__(self, mensagem):
#         self.mensagem = mensagem
#     def notificar(self, texto):
#         self.mensagem.enviar(texto)
#
# msn = Mensagem()
# usr = Usuario(msn)
# usr.notificar("Olá Usuário, boa noite.")

# 4) Herança e injecao de dependencia

class Veiculo:
    def mover(self):
        pass

class Motor:
    def partida(self):
        print("Vrumm")
    def desliga(self):
        print("Desligando")

class Carro(Veiculo):
    def __init__(self, motor):
        self.motor = motor
    def mover(self):
        self.motor.partida()
        print("Veiculo se movendo")
    def parar(self):
        self.motor.desliga()

m = Motor()
c = Carro(m)
c. mover()
c.parar()