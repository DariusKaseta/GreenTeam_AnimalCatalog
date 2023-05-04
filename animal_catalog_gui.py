import PySimpleGUI as sg
from animal_catalog import Animal, Catalog, save_data, load_data

def get_animal_list(animals):
    animal_list = []
    for id, animal in enumerate(animals):
        animal_ = animal.as_list()
        animal_.insert(0, id)
        animal_list.append(animal_)
    return animal_list

# Ši funkcija atvaizduoja gyvūnų sąrašą
def view_animal_list():
    catalog = load_data()
    animal_list = get_animal_list(catalog.animals)

    # Naujo lango kūrimas
    layout = [[sg.Text("Animal List")],
              [sg.Table(values=animal_list, headings=["ID", "Species", "Class", "Order", "Family", "Genus"], max_col_width=25,
                        auto_size_columns=True, justification="left", key="Animal Table")],
              [sg.Button('Add new animal', key="Add new animal"), sg.Button("Remove", key="Remove")],
              [sg.Button("Save", key="Save"), sg.Button("Close", key="Close")]]
    
    window = sg.Window("Animal List", layout)

    # Lango atidarymas

    table = window["Animal Table"]
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
            animal_list = remove_animals(catalog)
            window["Animal Table"].update(values=animal_list)
            save_data(catalog)
    window.close()

def remove_animals(catalog):
    animal_list = get_animal_list(catalog.animals)


    layout = [[sg.Text("Select an animal to remove")],
              [sg.Listbox(values=animal_list, size=(40, 10), key="Animal Listbox")],
              [sg.Button("Remove", key="Remove"), sg.Button("Cancel", key="Cancel")]]

    window_remove = sg.Window("Remove Animal", layout)

    while True:
        event, values = window_remove.read()
        if event in (None, "Cancel"):
            window_remove.close()
            return None
        elif event == "Remove":
            selected_animal = window_remove["Animal Listbox"].get()[0]
            animal = catalog.get_animal(selected_animal[0])
            catalog.remove_animal(animal)
            animal_list.remove(selected_animal)
            window_remove.close()
            return animal_list


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

