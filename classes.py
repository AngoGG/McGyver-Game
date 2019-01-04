"""
    Will contain all the program classes
"""
import pygame
from pygame.locals import *
from constants import *

class Level:
    """
        Generation of the Labyrinth Design from a flat file
    """
    def __init__(self):
        self.file = FILE
        self.level_structure = []

    @classmethod
    def window_generation(cls):
        """
            Window Generation, does'nt work at the moment,
            Cant get the result back to use it in show method
        """
        return pygame.display.set_mode((WINDOW_SIDE_LENGTH, WINDOW_SIDE_LENGTH))

    def get_labyrinth_structure(self):
        """
            Labyrinth data recuperation from file
        """
        with open(self.file, "r") as fichier:
            level_structure = []
            for line in fichier:
                line_level = []
                for sprite in line:
                    if sprite != "\n":
                        line_level.append(sprite)
                level_structure.append(line_level)
            self.level_structure = level_structure
            return self.level_structure

    def set_labyrinth(self, window):
        """
            Generation of the map using map_data
                - Add image to each part of the map, basically wall, floor & guardian for the finish
                - Starting from top left with line & sprite = 0, then go for line after line filling
        """
        wall = pygame.image.load(WALL).convert()
        floor = pygame.image.load(FLOOR).convert()
        guard = pygame.image.load(GUARD).convert_alpha()
        #mcgyver = pygame.image.load(MCGYVER).convert_alpha()

        line_number = 0
        for line in self.level_structure:
            case_number = 0
            for sprite in line:
                abscissa = case_number * SPRITE_SIZE
                ordinate = line_number * SPRITE_SIZE
                if sprite == "0":
                    window.blit(wall, (abscissa, ordinate))
                elif sprite == "C":
                    window.blit(wall, (abscissa, ordinate))
                elif sprite == "1":
                    window.blit(floor, (abscissa, ordinate))
                elif sprite == "G":
                    window.blit(guard, (abscissa, ordinate))
                case_number += 1
            line_number += 1

class Character:
    """
        Main Character class
        Generation and motion management
    """

    def __init__(self, map_structure):
        #Recupération de la position du personnage en case et en pixel
        self.abscissa = 0
        self.ordinate = 0
        self.pixel_x = 0
        self.pixel_y = 0
        self.map = map_structure
        self.image = pygame.image.load(MCGYVER).convert_alpha()

    def move(self, direction):
        """
            Make the character move
        """
        if direction == "right":
            #Check that he wont get outside the Screen
            if self.abscissa < (SPRITES_NUMBER - 1):
                #Check that he wont go on the wall
                if self.map[self.ordinate][self.abscissa+1] != "0":
                    self.abscissa += 1  #Move one case on the right (positive axis)
                    self.pixel_x = self.abscissa * SPRITE_SIZE #Set new pixel position
        if direction == "left":
            #Check that he wont get outside the Screen
            if self.abscissa > 0:
                #Check that he wont go on the wall
                if self.map[self.ordinate][self.abscissa-1] != "0":
                    self.abscissa -= 1  #Move one case on the left (positive axis)
                    self.pixel_x = self.abscissa * SPRITE_SIZE #Set new pixel position
        if direction == "up":
            #Check that he wont get outside the Screen
            if self.ordinate > 0:
                #Check that he wont go on the wall
                if self.map[self.ordinate-1][self.abscissa] != "0":
                    self.ordinate -= 1  #Move one case up (negative axis)
                    self.pixel_y = self.ordinate * SPRITE_SIZE #Set new pixel position
        if direction == "down":
            #Check that he wont get outside the Screen
            if self.ordinate < (SPRITES_NUMBER - 1):
                #Check that he wont go on the wall
                if self.map[self.ordinate+1][self.abscissa] != "0":
                    self.ordinate += 1  #Move one case down (positive axis)
                    self.pixel_y = self.ordinate * SPRITE_SIZE #Set new pixel position
    @property
    def position(self):
        """
            Characters position, for image bliting
        """
        return [self.pixel_x, self.pixel_y]

class Objects:
    """
        So Here the  built of this class
            In the Level class (or Objects class still not decided where it should better be),
            Add a method that take all the free sprites and add them to a dictionnary
            Count number of dictionnary entries, then rand a number from 0 to max in
            The Number got is the sprite where the item has to be set
            There are 3 items, do we launch the class for each or set up a auto rand
            for all Items in 1-time?
            When McGyver walk on an Object, it disapears and is counted as collected
            How to get an item on pygame?
    """