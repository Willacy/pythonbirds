# Criando a Classe Pessoa
class Pessoa:
    def __init__(self, *filhos,nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'{id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    willacy = Pessoa(renzo, nome='Willacy')
    print(Pessoa.cumprimentar(willacy))
    print(id(willacy))
    print(willacy.cumprimentar())
    print(willacy.nome)
    print(willacy.idade)
    for filho in willacy.filhos:
        print(filho.nome)
