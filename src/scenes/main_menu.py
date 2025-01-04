import sys
import pygame
import random
from src.scripts.textandbuttons import Text, Button
from src.scripts.effects import ParticleSystem, Fire
from cfg import *
import os

class Main_menu:
    def __init__(self):
        self.part_sys = ParticleSystem()
        self.fire = Fire((255, 0, 0), 16)
        self.text_list = [Text(140, "GRIEF", (200, 0, 0), (60, 350))]
        self.buttons = [
            Button(60, 520, 170, 50, (200, 0, 0), (150, 0, 0),
                (100, 0, 0), 32, 'game',"Start"),
            Button(260, 520, 170, 50, (200, 0, 0), (150, 0, 0),
                   (100, 0, 0), 32, 'opt', "Options"),
            Button(460, 520, 170, 50, (200, 0, 0), (150, 0, 0),
                   (100, 0, 0), 32, 'credits', "Credits"), 
            Button(660, 520, 170, 50, (200, 0, 0), (150, 0, 0),
                   (100, 0, 0), 32, 'exit', "Exit")]
        self.button_f = ""
    
    def render(self, surface, events):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = (int(mouse_pos[0]) / SCALE_X, int(mouse_pos[1]) / SCALE_Y)


        surface.fill((0, 0, 0))

        if random.random() > 0.1:
            self.part_sys.add_particle()

        self.fire.draw()
        self.part_sys.draw()
        for t in self.text_list:
            t.draw()

        for button in self.buttons:
            button.check_inp(mouse_pos)
            if button.click(mouse_pos, mouse_pressed):
                self.button_f = button.click_func
            button.draw()


        