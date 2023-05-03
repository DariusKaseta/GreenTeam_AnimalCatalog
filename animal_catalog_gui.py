import PySimpleGUI as sg
from animal_catalog import Animal, Catalog, save_data, load_data


# Ši funkcija atvaizduoja gyvūnų sąrašą
def view_animal_list():
    catalog = load_data()
    # Sukurkite savo gyvūnų sąrašo elementus čia
    #
    animal_list = [animal.as_list() for animal in catalog.animals]

    # Naujo lango kūrimas
    layout = [[sg.Text("Animal List")],
              [sg.Table(values=animal_list, headings=["Species", "Class", "Order", "Family", "Genus"], max_col_width=25,
                        auto_size_columns=True, justification="left", key="Animal Table")],
              [sg.Button('Add new animal', key="Add new animal"), sg.Button("Remove", key="Remove")],
              [sg.Button("Save", key="Save"), sg.Button("Close", key="Close")]]
    
    window = sg.Window("Animal List", layout)

    # Lango atidarymas
    while True:
        event, values = window.read()
        if event in (None, "Close"):
            break
        elif event == "Save":
            save_data(catalog)
        elif event == "Add new animal":
            animal = add_animals()
            catalog.add_animal(animal)
            animal_list.append(animal.as_list())
            window["Animal Table"].update(values=animal_list)
        elif event == "Remove":
            animal = remove_animals()
            if animal is not None:
                catalog.remove_animal(animal)
                animal_list.remove(animal.as_list())
                window["Animal Table"].update(values=animal_list)
    window.close()

def remove_animals():
    catalog = load_data()
    animal_list = animal_list = [animal.as_list() for animal in catalog.animals]

    layout = [[sg.Text("Select an animal to remove")],
              [sg.Listbox(values=animal_list, size=(40, 10), key="Animal Listbox")],
              [sg.Button("Remove", key="Remove"), sg.Button("Cancel", key="Cancel")]]

    window_remove = sg.Window("Remove Animal", layout)

    while True:
        event , values = window_remove.read()
        if event in (None, "Cancel"):
            window_remove.close()
            return None
        elif event == "Remove":
            selected_animal = window_remove["Animal Listbox"].get()[0]
            animal = Animal(*selected_animal)
            catalog.remove_animal(animal)
            animal_list.remove(selected_animal)
            window_remove.close()
            return animal


#  while True:
#         event, values = window.read()
#         print(values)
#         if event in (None, "Close"):
#             break
#         elif event == "Save":
#             save_data(catalog)
#         elif event == "Add new animal":
#             animal = add_animals()
#             catalog.add_animal(animal)
#             animal_list.append(animal.as_list())
#             window["Animal Table"].update(values=animal_list)
#         elif event == "Remove":
#             pass
#     window.close()

# Pradinio lango kūrimas
def add_animals():  #perkelti i virsu.
    layout = [
        [sg.Text("Insert animal Name/Species:"), sg.Input("", key="species")],
        [sg.Text("Insert animal Class:"), sg.Input("", key="class")],
        [sg.Text("Insert animal Order:"), sg.Input("", key="order")],
        [sg.Text("Insert animal Family:"), sg.Input("", key= "family")],
        [sg.Text("Insert animal Genus:"), sg.Input("", key="genus")],
        [sg.Text("Insert animal Image:"), sg.InputText(key="image_path"), sg.FileBrowse()],
        [sg.Button("Approve", key="Approve"), sg.Button("Cancel", key="Cancel")]]
    
    
    window_add = sg.Window("Add Animal", layout)

    # Pridejimo lango veiksmo gaudymas
    while True:
        event, values = window_add.read()
        if event in (None, "Cancel"):
            window_add.close()
            return None
        elif event == "Approve":
            print(values["species"])
            try:
                animal = Animal(values["species"], values["class"], values["order"], values["family"], values["genus"])
                animal.image_path = values["image_path"]
            except:
                pass
            else:
                window_add.close()
                return animal


if __name__ == "__main__":
    view_animal_list()

