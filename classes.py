# copilot: disable
import pyxel
import numpy as np
import time


class Jogo:
    def __init__(self) -> None:
        
        self.width = 200
        self.height = 200
        self.screenDim = (self.width, self.height)
        
        
        pyxel.init(self.width, self.height, title="Jogo", fps=60)

        self.obstacles_matrix = np.zeros(self.screenDim)
        self.add_rect_obstacle(30, 0, 20, 100, 0, self.obstacles_matrix)
        self.add_rect_obstacle(0, 120, 200, 20, 0, self.obstacles_matrix)

        self.circle1 = CircleAvatar(38, 114, 5, self.screenDim, self.obstacles_matrix)

        self.screen_matrix = self.obstacles_matrix+self.circle1.position_matrix

        pyxel.run(self.update, self.draw)
    

    def update(self):

        self.circle1.update()


    def draw(self):
        pyxel.cls(15)

        self.screen_matrix = self.circle1.position_matrix + self.obstacles_matrix
        self.paint_screen(self.screen_matrix)

        self.matrix_to_txt(self.screen_matrix, 'screen_matrix')
    
        pass


    def add_rect_obstacle(self, x, y, w, h, color, matrix):
        
        pyxel.rect(x, y, w, h, color)
        matrix[y:y+h, x:x+w] += 1
    

    def paint_screen(self, matrix):
        for y in range(matrix.shape[0]):
            for x in range(matrix.shape[1]):
                if matrix[y,x]==1:
                    pyxel.pset(x, y, 0)

    
    def matrix_to_txt(self, matrix, filename):

        with open(filename+'.txt', 'w+') as f:
            for line in matrix:
                f.write(' '.join([str(int(h)) for h in line]) + '\n')        


class CircleAvatar:
    def __init__(self, initial_x, initial_y, radius, screendimension, obstacles_matrix) -> None:

        self.radius = radius
        self.x = initial_x
        self.y = initial_y
        self.screenDim = screendimension
        self.position_matrix = self.add_circle_to_matrix(self.x, self.y)
        self.velocity = 1
        self.obstacles_matrix = obstacles_matrix

        self.jump_height = 20
        self.jumping_left = 0
  

    def update(self):
            
            self.keyboard_movement()

            if self.jumping_left > (-self.jump_height):
                self.jump()

    def add_circle_to_matrix(self, h, k):

        matrix = np.zeros(self.screenDim)
        for y in range(k-self.radius, k+self.radius+1):
            for x in range(h-self.radius, h+self.radius+1):
                coord = ((x-h)**2) + ((y-k)**2)
                if coord <= (self.radius**2)+1:
                    matrix[y, x]+=1

        return matrix

    def keyboard_movement(self):

        if pyxel.btn(pyxel.KEY_D):
            self.x, self.y = self.goto_position(self.x+self.velocity, self.y)

        if pyxel.btn(pyxel.KEY_A):
            self.x, self.y = self.goto_position(self.x-self.velocity, self.y)
            
        if pyxel.btnp(pyxel.KEY_W):
            self.jumping_left = self.jump_height
           # self.x, self.y = self.goto_position(self.x, self.y-self.velocity)
        
        if pyxel.btn(pyxel.KEY_S): 
            self.x, self.y = self.goto_position(self.x, self.y+self.velocity)

        if pyxel.btn(pyxel.KEY_SPACE):
            print(self.x, self.y)

        if pyxel.btn(pyxel.KEY_SHIFT):
            self.velocity = 3
        else:
            self.velocity = 1

    def jump(self):
        
        if self.jumping_left > 0:
            i = 1
        else:
            i = -1
            
        self.x, self.y = self.goto_position(self.x, self.y - i)
        self.jumping_left -= 1

            #print(self.y)        

    
    def goto_position(self, target_x, target_y):

        if target_x+self.radius>=self.screenDim[1] or target_x-self.radius<0 or \
            target_y+self.radius>=self.screenDim[0] or target_y-self.radius<0:
            return [self.x, self.y]
        
        matrix_test = self.obstacles_matrix + self.add_circle_to_matrix(target_x, target_y)

        # return [target_x, target_y]
        if np.count_nonzero(matrix_test==2)==0:
            self.position_matrix = self.add_circle_to_matrix(target_x, target_y)
            return [target_x, target_y]
        else:
            return [self.x, self.y]

Jogo()

class Teste:
    
    def __init__(self) -> None:
        print('Teste')