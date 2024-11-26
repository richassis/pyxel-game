# copilot: disable
import pyxel
import numpy as np

class Jogo:
    def __init__(self) -> None:
        self.width = 100
        self.height = 100
        
        pyxel.init(self.width, self.height, title="Jogo", fps=60)

        self.raio = 5
        self.velocidade = 1


        self.x = 6
        self.y = 6

        self.obstacles_matrix = np.zeros((self.height, self.width))
        self.avatar_matrix = np.zeros((self.height, self.width))

        pyxel.run(self.update, self.draw)
    

    def update(self):

        self.velocidade = 1
        if pyxel.btn(pyxel.KEY_SHIFT):
            self.velocidade = 3

        self.keyboard_movement()


    
    def draw(self):
        pyxel.cls(15)
        #pyxel.circ(self.x, self.y, self.raio, 0)

        self.add_circle_obstacle(self.x, self.y, self.raio, self.avatar_matrix)
        self.add_rect_obstacle(60, 0, 6, 30, 0, self.obstacles_matrix)

        pass


    def add_rect_obstacle(self, x, y, w, h, color, matrix):
        
        pyxel.rect(x, y, w, h, color)
        matrix[y:y+h, x:x+w] = 1

        with open('obstacles_matrix.txt', 'w+') as f:
            for line in matrix:
                f.write(' '.join([str(int(x)) for x in line]) + '\n')
    

    def add_circle_obstacle(self, x, y, radius, matrix):

        matrix.fill(0)
        for i in range(y-radius, y+radius+1):
            for j in range(x-radius, x+radius+1):
                coord = ((j-x)**2) + ((i-y)**2)
                if coord <= (radius**2)+1:
                    matrix[i, j]=1
                    pyxel.pset(j, i, 0)
        
        with open('avatar_matrix.txt', 'w+') as f:
            for line in matrix:
                f.write(' '.join([str(int(x)) for x in line]) + '\n')

    def is_position_allowed(self, x, y, obst_matrix):

        if x+self.raio>obst_matrix.shape[1] or x-self.raio<0 or \
            y+self.raio>obst_matrix.shape[0] or y-self.raio<0:
            return False

        
        # for i in range(self.height):
        #     for j in range(self.width):
        #         #if i<12 and j<12:
        #          #   print(((i+self.x)**2) + ((j+self.y)**2), self.raio**2)
        #         if ((j+self.x)**2) + ((i+self.y)**2) == self.raio**2:
        #             print(i, j)
        
        # self.add_circle_obstacle(x, y, self.raio)
        result_matrix = (obst_matrix+self.avatar_matrix)

        with open('result_matrix.txt', 'w+') as f:
            for line in result_matrix:
                f.write(' '.join([str(int(x)) for x in line]) + '\n')

        if np.count_nonzero(result_matrix==2)>0:
            return False
        else:
            return True
        
        

    def keyboard_movement(self):

        if pyxel.btn(pyxel.KEY_D):
            target_x = self.x + self.velocidade
            if self.is_position_allowed(target_x, self.y, self.obstacles_matrix):
                self.x=target_x

        if pyxel.btn(pyxel.KEY_A):
            target_x = self.x - self.velocidade
            if self.is_position_allowed(target_x, self.y, self.obstacles_matrix):
                self.x=target_x

        if pyxel.btn(pyxel.KEY_W):
            target_y = self.y - self.velocidade
            if self.is_position_allowed(self.x, target_y, self.obstacles_matrix):
                self.y=target_y
        
        if pyxel.btn(pyxel.KEY_S): 
            target_y = self.y + self.velocidade
            if self.is_position_allowed(self.x, target_y, self.obstacles_matrix):
                self.y=target_y
        
Jogo()

class Teste:
    
    def __init__(self) -> None:
        print('Teste')