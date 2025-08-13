import json
from pathlib import Path


data_file  = Path("utils/test_data.json")

def save_user_data(email, password):
    #saving data to json file
    data_file.write_text(json.dumps({"email" : email, "password" : password}))


def load_user_data():
    # load the credential from json file

    try:
        if data_file.exists():
            return json.loads(data_file.read_text())
        else:
            print("the data file not found : run regression test first : ")

    except Exception as e :

        print(f" problem with reading file as :: {e} ")
