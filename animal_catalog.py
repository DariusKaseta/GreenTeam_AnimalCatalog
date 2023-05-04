import os
import pickle

def save_data(catalog):
    if isinstance(catalog, Catalog):
        with open("catalog.pickle", "wb") as f:
            pickle.dump(catalog.animals, f)

def load_data():
    catalog = Catalog()
    if not os.path.exists("catalog.pickle"):
        return catalog
    with open("catalog.pickle", "rb") as f:
        catalog.animals = pickle.load(f)
    return catalog


# os.system('cls' if os.name == 'nt' else 'clear')

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

    def as_list(self): #isideti kaip duomenis "animal"is gui
        return [self.species, self.animal_class, self.order, self.family, self.genus]


class Catalog: 
    animals = []
    
    @property
    def total_animals(self):
        return len(self.animals)

    def add_animal(self, animal):  # Karolis
        self.animals.append(animal)

    def remove_animal(self, animal): # Karolis
        self.animals.remove(animal)
    
    def get_animal(self, id):
        return self.animals[id]
    
    # def review_catalog(animal_dict): # Milda
    #     print("Animal catalog: ")
    #     for animal in animal_dict:
    #         print(f"{animal}")

    # def review_by_class(): # Milda
    #     sorted_by_class = dict(sorted(animal.animals(), key = lambda x: x[1]['animal_class']))
    #     print(sorted_by_class)
        
    # def review_by_order(): # Milda
    #     pass

    # def review_by_family(): # Milda
    #     pass

    # def review_by_genus(): # Milda
    #     pass

    # def review_by_species(): # Milda
    #     pass

    def total_animals_added(self): # Darius
        return self.total_animals
        


