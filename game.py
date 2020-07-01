""" 
Student Robert Doult
Date 20191129
Class CSCI 1511 - project2
Make the image move back and forth."""
import pygame
import math, random
from superwires import games, color 
 
SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('red') #The background colod of our window
FPS = 10 #Frames per second
BACKGROUND_IMAGE = pygame.image.load('background.jpg')# Set the background
 
class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor and loads all images in directory
        super(MySprite, self).__init__()
        self.images = []
        #list of images used    
        self.images.append(pygame.image.load('walk1.png'))
        self.images.append(pygame.image.load('walk2.png'))
        self.images.append(pygame.image.load('walk3.png'))
        self.images.append(pygame.image.load('walk4.png'))
        self.images.append(pygame.image.load('walk5.png'))
        self.images.append(pygame.image.load('walk6.png'))
        self.images.append(pygame.image.load('walk7.png'))
        self.images.append(pygame.image.load('walk8.png'))
        self.images.append(pygame.image.load('walk9.png'))
        self.images.append(pygame.image.load('walk10.png'))
        self.index = 0
        self.image = self.images[self.index]
        #per dafult your image will be on position (0,0) (top left og the screen). You can change the x and y properties of your car as follows:
        self.rect = pygame.Rect(50, 136, 150, 198)
 
            
    def update(self):
        self.index += 1
        #pygame.key.get_pressed function to detect whether a key is pressed.
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

        
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    #On Window using the clock function returns wall-clock seconds elapsed since the first call to this function, as a floating point number
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        my_group.update()
        #screen.fill(BACKGROUND_COLOR)
        #background image
        screen.blit(BACKGROUND_IMAGE, (0,0))
        my_group.draw(screen)
        #screen.fill(BACKGROUND_COLOR)
        #background image
        pygame.display.update()
        clock.tick(10) 
        
        
 
if __name__ == '__main__':
    main()
