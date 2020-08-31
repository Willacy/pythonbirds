# Criando a Classe Pessoa
class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'{id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atrubutos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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
    print(Pessoa.metodo_estatico())
    print(willacy.metodo_estatico())
