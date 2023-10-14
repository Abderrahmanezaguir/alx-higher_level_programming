#!/usr/bin/python3
'''Module for Base class.'''

class Base :
    '''A representation of ...'''
    __nb_objects = 0
    def __innit__(self, id=None):
        '''constructor.'''
        if id is not None:
            self.id = id 
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
