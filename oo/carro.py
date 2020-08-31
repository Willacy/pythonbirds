"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:
1) Motor;
2) Direção;
O motor terá a responsabilidade de controlar a velocidade. Ele oferece os seguintes atributos:
1) Atributo de dado Velocidade;
2) Metodo acelar, que deverá incrementar a celocidade de uma unidade;
3) Metodo frear que deverá decrementar a velocidade em duas unidades;
A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possiveis: Norte, Sul, Leste, Oeste;
2) Metodo girar a direita;
3) Metodo girar a esquerda;

            N
        O       L
            S
"""


# Criando a classe Motor
class Motor:
    # Criando o metodo inicializador
    def __init__(self):
        self.velocidade = 0

    # Criando o metodo acelerar
    def acelerar(self):
        self.velocidade += 1

    # Criando o metodo frear
    def frear(self):
        if self.velocidade <= 1:
            self.velocidade = 0
        else:
            self.velocidade -= 2

