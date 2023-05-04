import PySimpleGUI as sg
from animal_catalog import Animal, Catalog, save_data, load_data
import io
import os
from PIL import Image

def get_animal_list(animals):
    animal_list = []
    for animal in animals:
        animal_list.append(animal.as_list())
    return animal_list


# Ši funkcija atvaizduoja gyvūnų sąrašą
def view_animal_list():
    catalog = load_data()
    animal_list = get_animal_list(catalog.animals)

    # Naujo lango kūrimas
    layout = [[sg.Text("Animal List")],
                [sg.Table(values=animal_list, headings=[ "Species", "Class", "Order", "Family", "Genus"], max_col_width=25,
                            auto_size_columns=True, justification="left", key="Animal Table")],
                [sg.Button('Add new animal', key="Add new animal"), sg.Button("Remove", key="Remove"),
                 sg.Button("View animal image", key="View animal image")],
                [sg.Button("Save", key="Save"), sg.Button("Close", key="Close")],
                [sg.Image(key="-IMAGE-")]]
        
    
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
            if animal is not None:
                catalog.add_animal(animal)
                animal_list.append(animal.as_list())
                table.update(values=animal_list)
        elif event == "Remove":
            selected_rows = table.SelectedRows
            if selected_rows:
                selected_row = selected_rows[0]
                selected_animal = catalog.get_animal(selected_row)
                catalog.remove_animal(selected_animal)
                animal_list = get_animal_list(catalog.animals)
                table.update(values=animal_list)
                save_data(catalog)
        elif event == "View animal image":
            selected_row = table.SelectedRows[0]
            animal = catalog.get_animal(selected_row)
            image_path = animal.image_path
            if image_path:
                image = Image.open(image_path)
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                # Actually store the image in memory in binary
                image.save(bio, format="PNG")
                # Use that image data in order to 
                window["-IMAGE-"].update(data=bio.getvalue())
            else:
                window["-IMAGE-"].update(data=None)



            # selected_animal = table.SelectedRows[0]
            # animal = catalog.get_animal(selected_animal[0])
            # image_path = animal.image_path
            # if image_path:
            #     image = sg.Image(image_path)
            #     sg.Window('Image Viewer', [[image]])

        
        
        
        
        
        
        
        # elif event == "Remove":
        #     selected_row = table.SelectedRows[0]
        #     selected_animal = catalog.get_animal(selected_row)
        #     catalog.remove_animal(selected_animal)
        #     animal_list = get_animal_list(catalog.animals)
        #     table.update(values=animal_list)
        #     save_data(catalog)
    window.close()


def add_animals():
    layout = [
        [sg.Text("Insert animal Name/Species:"), sg.Input("", key="species")],
        [sg.Text("Insert animal Class:"), sg.Input("", key="class")],
        [sg.Text("Insert animal Order:"), sg.Input("", key="order")],
        [sg.Text("Insert animal Family:"), sg.Input("", key="family")],
        [sg.Text("Insert animal Genus:"), sg.Input("", key="genus")],
        [sg.Text("Insert animal Image:"), sg.InputText(key="image_path"), sg.FileBrowse()],
        [sg.Button("Approve", key="Approve"), sg.Button("Cancel", key="Cancel")]
    ]
    
    window_add = sg.Window("Add Animal", layout)

    # Pridejimo lango veiksmo gaudymas
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


if __name__ == "__main__":
    view_animal_list()
