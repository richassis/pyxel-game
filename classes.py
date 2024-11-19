import pyxel

class Jogo:
    def __init__(self) -> None:
        self.width = 200
        self.height = 200
        
        pyxel.init(self.width, self.height, title="Jogo", fps=60)

        self.raio = 20
        self.velocidade = 1

        self.x = 20
        self.y = 20

        self.barrierx = 180
        self.barriery = 40
        self.barrierw = 10
        self.barrierh = 6

        pyxel.run(self.update, self.draw)
    
    def update(self):

        self.velocidade = 1
        if pyxel.btn(pyxel.KEY_SHIFT):
            self.velocidade = 3

        # if self.x >= 100-self.raio or self.x <= 0+self.raio:
        #     self.velocidade = self.velocidade * (-1)

        # self.x = self.x + self.velocidade

        if not (self.x+self.raio >= self.barrierx and self.x+self.raio <= self.barrierx+self.barrierw):

            if pyxel.btn(pyxel.KEY_D):
                if self.x<self.width-self.raio:
                    self.x += self.velocidade
            
        #if not (self.y+self.raio)

        if pyxel.btn(pyxel.KEY_A):
            if self.x > self.raio:
                self.x -= self.velocidade

        if pyxel.btn(pyxel.KEY_W):
            if self.y > self.raio:
                self.y -= self.velocidade
        
        if pyxel.btn(pyxel.KEY_S): 
                if self.y < self.height-self.raio:
                    self.y += self.velocidade


    
    def draw(self):
        pyxel.cls(15)
        pyxel.circ(self.x, self.y, self.raio, 0)

        

           
        #x**2 + y**2 = r**2
        
        #pyxel.pset()

        pyxel.rect(self.barrierx, self.barriery, self.barrierw, self.barrierh, 0)

        pass

class Teste:
    
    def __init__(self) -> None:
        print('Teste')