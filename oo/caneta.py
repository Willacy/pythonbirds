class Caneta:
    def __init__(self, marca=None, *modelo, tapado=True):
        self.marca = marca
        self.modelo = list(modelo)
        self.tampado = tapado

    def destampar_caneta(self):
        if self.tampado:
            self.tampado = False
            print('Caneta destampada!')
        else:
            print('Caneta já está destampada!')

    def tampar_caneta(self):
        if self.tampado:
            print('Caneta já esta tampada!')
        else:
            self.tampado = True
            print('Caneta tampada')


if __name__ == '__main__':
    caneta1 = Caneta('BIC', 'A')
    caneta1.destampar_caneta()
    caneta1.destampar_caneta()
    caneta1.tampar_caneta()
    caneta1.tampar_caneta()