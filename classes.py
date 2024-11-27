# copilot: disable
import pyxel
import numpy as np

class CircleAvatar:
    def __init__(self, radius, initial_x, initial_y, matrix) -> None:
        self.radius = radius
        self.x = initial_x
        self.y = initial_y
        self.matrix = matrix
        self.update_position(self.x, self.y)

    
    def update_position(self, target_x, target_y):

        self.y = target_y
        self.x = target_x

        for y in range(self.y-self.radius, self.y+self.radius+1):
            for x in range(self.x-self.radius, self.x+self.radius+1):
                coord = ((x-self.x)**2) + ((y-self.y)**2)
                if coord <= (self.radius**2)+1:
                    self.matrix[y, x]+=1
        

class Jogo:
    def __init__(self) -> None:
        self.width = 200
        self.height = 200
        
        pyxel.init(self.width, self.height, title="Jogo", fps=60)

        self.raio = 5
        self.velocidade = 1

        self.x = 5
        self.y = 5

        self.obstacles_matrix = np.zeros((self.height, self.width))
        self.add_rect_obstacle(30, 0, 20, 40, 0, self.obstacles_matrix)

        self.avatar_matrix = self.add_circle_obstacle(self.x, self.y, self.raio, (self.height, self.width))

        self.screen_matrix = self.obstacles_matrix+self.avatar_matrix

        pyxel.run(self.update, self.draw)
    

    def update(self):

        self.velocidade = 1
        if pyxel.btn(pyxel.KEY_SHIFT):
            self.velocidade = 3

        self.keyboard_movement()


    def draw(self):
        pyxel.cls(15)
        #pyxel.circ(self.raio, 0)

        self.screen_matrix = self.avatar_matrix + self.obstacles_matrix
        self.paint_screen(self.screen_matrix)

        self.matrix_to_txt(self.screen_matrix, 'screen_matrix')
    
        pass


    def add_rect_obstacle(self, x, y, w, h, color, matrix):
        
        pyxel.rect(x, y, w, h, color)
        matrix[y:y+h, x:x+w] += 1
    

    def add_circle_obstacle(self, h, k, radius, matrix_shape):

        matrix = np.zeros(matrix_shape)
        for y in range(k-radius, k+radius+1):
            for x in range(h-radius, h+radius+1):
                coord = ((x-h)**2) + ((y-k)**2)
                if coord <= (radius**2)+1:
                    matrix[y, x]+=1

        return matrix

    def paint_screen(self, matrix):
        for y in range(matrix.shape[0]):
            for x in range(matrix.shape[1]):
                if matrix[y,x]==1:
                    pyxel.pset(x, y, 0)


    def goto_position(self, target_x, target_y, obst_matrix):

        if target_x+self.raio>=obst_matrix.shape[1] or target_x-self.raio<0 or \
            target_y+self.raio>=obst_matrix.shape[0] or target_y-self.raio<0:
            return [self.x, self.y]
        
        matrix_test = self.obstacles_matrix + self.add_circle_obstacle(target_x, target_y, self.raio, (self.height, self.width))
        self.matrix_to_txt(matrix_test, "matrix-test")

        # return [target_x, target_y]
        if np.count_nonzero(matrix_test==2)==0:
            self.avatar_matrix = self.add_circle_obstacle(target_x, target_y, self.raio, (self.height, self.width))
            return [target_x, target_y]
        else:
            print('false2')
            return [self.x, self.y]
        
    def keyboard_movement(self):

        if pyxel.btn(pyxel.KEY_D):
            #self.avatar_matrix = self.add_circle_obstacle(self.x+self.velocidade, self.y, self.raio, self.avatar_matrix.shape)
            self.x, self.y = self.goto_position(self.x+self.velocidade, self.y, self.obstacles_matrix)

        if pyxel.btn(pyxel.KEY_A):
            self.x, self.y = self.goto_position(self.x-self.velocidade, self.y, self.obstacles_matrix)
            
        if pyxel.btn(pyxel.KEY_W):
            self.x, self.y = self.goto_position(self.x, self.y-self.velocidade, self.obstacles_matrix)
        
        if pyxel.btn(pyxel.KEY_S): 
            self.x, self.y = self.goto_position(self.x, self.y+self.velocidade, self.obstacles_matrix)
    
    def matrix_to_txt(self, matrix, filename):

        with open(filename+'.txt', 'w+') as f:
            for line in matrix:
                f.write(' '.join([str(int(h)) for h in line]) + '\n')        


Jogo()

class Teste:
    
    def __init__(self) -> None:
        print('Teste')