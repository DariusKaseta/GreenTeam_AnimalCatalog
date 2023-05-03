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
              [sg.Button("Close", key="Close"), sg.Button('Add new animal', key="Add new animal")],
              [sg.Button("Save", key="Save")]]
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
    window.close()

# Pradinio lango kūrimas
def add_animals():  #perkelti i virsu.
    layout = [
        [sg.Text("Insert animal Name/Species:"), sg.Input("", key="species")],
        [sg.Text("Insert animal Class:"), sg.Input("", key="class")],
        [sg.Text("Insert animal Order:"), sg.Input("", key="order")],
        [sg.Text("Insert animal Family:"), sg.Input("", key= "family")],
        [sg.Text("Insert animal Genus:"), sg.Input("", key="genus")],
        [sg.Button('Approve', key="Approve")]]
    
    window_add = sg.Window("Main Window", layout) #pakeisti window pavadinima

    # Pridejimo lango veiksmo gaudymas
    while True:
        event, values = window_add.read()
        if event in (None, "Exit"):
            break
        elif event == "Approve":
            print(values["species"])
            try:
                animal = Animal(values["species"], values["class"], values["order"], values["family"], values["genus"])
            except:
                pass
            else:
                window_add.close()
                return animal


if __name__ == "__main__":
    view_animal_list()

