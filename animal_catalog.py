# kelios def aprasytos ir uzkomentuotos (nebutinai gali buti teisinga)

import os
import json

os.system('cls' if os.name == 'nt' else 'clear')

class Animal:
    def __init__(self, animal_class, order, family, genus, species):
        self.animal_class = animal_class
        self.order = order
        self.family = family
        self.genus = genus
        self.species = species

    def print_animal_info(self):
        print(f"Class: {self.animal_class}")
        print(f"Order: {self.order}")
        print(f"Family: {self.family}")
        print(f"Genus: {self.genus}")
        print(f"Species: {self.species}\n")

class Catalog: 
    animals = []
    total_animals = 0
    
    # def add_animal(self, animal): 
    #     self.animals.append(animal)
    #     self.total_animals += 1
    
    def add_animal(): # Karolis
        pass

    # def remove_animal(self, animal): 
    #     self.animals.remove(animal)
    #     self.total_animals -= 1
    
    def remove_animal(): # Karolis
        pass

    def review_catalog(): # Milda
        pass

    def review_by_class(): # Milda
        pass
        
    def review_by_order(): # Milda
        pass

    def review_by_family(): # Milda
        pass

    def review_by_genus(): # Milda
        pass

    def review_by_species(): # Milda
        pass

    def total_animals_added(self): # Darius
        return self.total_animals
        
    
    # def save_in_json(self, filename):
    #     animal_list = []
        
    #     for animal in self.animals:
    #         animal_dict = {
    #             "animal_class": animal.animal_class,
    #             "order": animal.order,
    #             "family": animal.family,
    #             "genus": animal.genus,
    #             "species": animal.species
    #         }
    #         animal_list.append(animal_dict)

    #     with open(filename, "a") as file:
    #         json.dump(animal_list, file)
        



# Petras - save in json
