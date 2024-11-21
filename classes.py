import pyxel
import numpy as np

class Jogo:
    def __init__(self) -> None:
        self.width = 100
        self.height = 100
        
        pyxel.init(self.width, self.height, title="Jogo", fps=60)

        self.raio = 20
        self.velocidade = 1


        self.x = 20
        self.y = 20


        print(np.zeros((10,1)))

        self.obstacles = np.zeros((self.height, self.width))

        pyxel.run(self.update, self.draw)
    

    def update(self):

        self.velocidade = 1
        if pyxel.btn(pyxel.KEY_SHIFT):
            self.velocidade = 3

        self.keyboard_movement()


    
    def draw(self):
        pyxel.cls(15)
        pyxel.circ(self.x, self.y, self.raio, 0)



        self.add_rect_obstacle(60, 0, 6, 30, 0)

        pass


    def add_rect_obstacle(self, x, y, w, h, color):
        
        pyxel.rect(x, y, w, h, color)
        self.obstacles[y:y+h, x:x+w] = 1
        

        with open('matrix.txt', 'w+') as f:
            for line in self.obstacles:
                f.write(' '.join([str(int(x)) for x in line]) + '\n')
    

    def is_position_allowed(self, x, y):

        if x>len(self.obstacles) or x<0 or y>len(self.obstacles[0]) or y<0:
            return False
            

        if self.obstacles[x,y]:
            return False
        else:
            return True
        
        

    def keyboard_movement(self):

        if pyxel.btn(pyxel.KEY_D):
            target_x = self.x + self.velocidade
            if self.is_position_allowed(target_x, self.y):
                self.x=target_x



        if pyxel.btn(pyxel.KEY_A):
            if self.x > self.raio:
                self.x -= self.velocidade

        if pyxel.btn(pyxel.KEY_W):
            if self.y > self.raio:
                self.y -= self.velocidade
        
        if pyxel.btn(pyxel.KEY_S): 
                if self.y < self.height-self.raio:
                    self.y += self.velocidade
        
Jogo()

class Teste:
    
    def __init__(self) -> None:
        print('Teste')