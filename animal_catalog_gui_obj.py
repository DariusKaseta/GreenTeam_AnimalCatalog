import PySimpleGUI as sg
from animal_catalog import Animal, Catalog, save_data, load_data
import io
import os
from PIL import Image




class AnimalCatalogGui:
    def __init__(self):
        self.catalog = load_data()
        self.animal_list = self.get_animal_list(self.catalog.animals)
        self.table = sg.Table(values=self.animal_list, headings=Animal.headers(), auto_size_columns=True, key="-TABLE-")
        self.layout = [
            [self.table],
            [sg.Button("Add new animal"), sg.Button("Remove"), sg.Button("View animal image"), sg.Button("Save"), sg.Button("Close")],
            [sg.Image(key="-IMAGE-")]
        ]
        self.window = sg.Window("Animal Catalog", layout=self.layout)

    def get_animal_list(self, animals):
        animal_list = []
        for animal in animals:
            animal_list.append(animal.as_list())
        return animal_list


    def run(self):
        while True:
            event, values = self.window.read()
            if event in (None, "Close"):
                break
            elif event == "Save":
                save_data(self.catalog)
            elif event == "Add new animal":
                animal = self.add_animals()
                if animal is not None:
                    self.catalog.add_animal(animal)
                    self.animal_list.append(animal.as_list())
                    self.table.update(values=self.animal_list)
            elif event == "Remove":
                selected_rows = values["-TABLE-"]
                if selected_rows:
                    selected_row = selected_rows[0]
                    selected_animal = self.catalog.get_animal(selected_row)
                    self.catalog.remove_animal(selected_animal)
                    self.animal_list = self.get_animal_list(self.catalog.animals)
                    self.table.update(values=self.animal_list)
                    save_data(self.catalog)
            elif event == "View animal image":
                selected_row = values["-TABLE-"][0]
                animal = self.catalog.get_animal(selected_row)
                image_path = animal.image_path
                if image_path:
                    image = Image.open(image_path)
                    image.thumbnail((400, 400))
                    bio = io.BytesIO()
                    # Actually store the image in memory in binary
                    image.save(bio, format="PNG")
                    # Use that image data in order to 
                    self.window["-IMAGE-"].update(data=bio.getvalue())
                else:
                    self.window["-IMAGE-"].update(data=None)

        self.window.close()

    def add_animals(self):
            
        layout = [
            [sg.Text("Insert animal Name/Species:"), sg.Input("", key="species")],
            [sg.Text("Insert animal Class:"), sg.Input("", key="class")],
            [sg.Text("Insert animal Order:"), sg.Input("", key="order")],
            [sg.Text("Insert animal Family:"), sg.Input("", key="family")],
            [sg.Text("Insert animal Genus:"), sg.Input("", key="genus")],
            [sg.Text("Insert animal Image:"), sg.InputText(key="image_path"), sg.FileBrowse()],
            [sg.Button("Approve", key="Approve"), sg.Button("Cancel", key="Cancel")]
    ]
    
        window_add = sg.Window("Add Animal", layout=layout)

        self.window.close()

        while True:
            event, values = window_add.read()
            if event in (None, "Cancel"):
                window_add.close()
                return None
            elif event == "Approve":
                try:
                    animal = Animal(values["species"], values["class"], values["order"], values["family"], values["genus"], values["image_path"])
                except:
                    pass
                else:
                    window_add.close()
                    return animal





