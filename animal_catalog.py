# kelios def aprasytos ir uzkomentuotos (nebutinai gali buti teisinga)

import os
import json

def save_data (animals):
    with open ("catalog.json", "w", encoding= "utf-8") as f:
        json.dump(animals, f)

def load_data():
    if not os.path.exists("catalog.json"):
        return []
    with open ("catalog.json", "r") as f:
        animals = json.load(f)
    return animals


os.system('cls' if os.name == 'nt' else 'clear')

class Animal:
    def __init__(self, species_name, animal_class, order, family, genus):
        self.species = species_name
        self.animal_class = animal_class
        self.order = order
        self.family = family
        self.genus = genus

    def print_animal_info(self):
        print(f"Class: {self.animal_class}")
        print(f"Order: {self.order}")
        print(f"Family: {self.family}")
        print(f"Genus: {self.genus}")
        print(f"Species: {self.species}\n")

class Catalog: 
    animals = []
    total_animals = 0
    
    @property
    def total_animal(self, animal):
        return len(animal)

    def add_animal(self, animal):  # Karolis
        self.animals.append(animal)

    def remove_animal(self, animal): # Karolis
        self.animals.remove(animal)

    def review_catalog(animal_dict): # Milda
        print("Animal catalog: ")
        for animal in animal_dict:
            print(f"{animal}")

    def review_by_class(self, animal): # Milda
        sorted_by_class = dict(sorted(animal.animals(), key = lambda x: x[1]['animal_class']))
        print(sorted_by_class)
        
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

