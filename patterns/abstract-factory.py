#!/usr/local/bin/ python3
# -*- coding: utf-8 -*-

import random

class PetShop(object):
    '''A pet shop'''

    def __init__(self, animal_factory=None):
        '''pet_factory is our abstract factory'''

        self.pet_factory = animal_factory

    def show_pet(self):

        pet = self.pet_factory()
        print("我们有一只可爱的{}".format(pet))
        print('It says {}'.format(pet.speak()))

class Dog(object):

    def speak(self):
        return 'wooof'

    def __str__(self):
        return 'Dog'

class Cat(object):

    def speak(self):
        return 'meow'

    def __str__(self):
        return 'Cat'

def random_animal():
    '''Let's be dynamic!'''
    return random.choice([Dog, Cat])()

if __name__ == '__main__':
    
    cat_shop = PetShop(Cat)
    cat_shop.show_pet()
    print('')

    shop = PetShop(random_animal)
    for i in range(3):
        shop.show_pet()
        print('=' * 20)
