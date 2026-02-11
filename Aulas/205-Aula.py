# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, gravando=False):
        self.nome = nome
        self.gravando = gravando

    def gravar(self):
        if self.gravando:
                print(f'{self.nome} Já está gravando...')
                return

        print(f'{self.nome} está gravando...')
        self.gravando = True
    
    def parar_gravar(self):
            if not self.gravando:
                    print(f'{self.nome} Não está gravando...')
                    return

            print(f'{self.nome} está parando de gravando...')
            self.gravando = False
    
    
    def fotografar(self):
         if self.gravando:
            print(f'{self.nome} não pode fotografar enquanto está gravando...')
            return
         
         print(f'{self.nome} está fotografando...')

c1 = Camera('Cannon')
c2 = Camera('Sony')

c1.gravar()
c1.gravar()
c1.fotografar()
c1.parar_gravar()
c1.fotografar()
print()

c2.gravar()
c2.gravar()
c2.fotografar()
c2.parar_gravar()
c2.fotografar()