import json
import os


def save_to_json(data):                 # gets data as parameter

    os.makedirs("data", exist_ok=True)      # If data folder do not exist then it gets created

    file_path = "data/questions.json"

    if os.path.exists(file_path):               # checks if json file allready exist 
        with open(file_path, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    else:
        existing_data = []                  # creats empty list as data 

    existing_data.append(data)              # Adds new data

    # used to save in json file
    with open(file_path, "w", encoding="utf-8") as file:            
        json.dump(                              # converts python list directory into json file
            existing_data,
            file,
            indent=4,                           # json file looks well formated
            ensure_ascii=False                  # saves unicode text in other language
        )