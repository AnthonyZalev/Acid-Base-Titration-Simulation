import json


class DataBase:
    def __init__(self):
        self.path = "/"
        self.filename = "AcidNameKADAtaBase.json"

    def WriteToJSONFIle(self, data):
        filePathNameWithExt = "./" + self.path + "/" + self.filename
        with open(filePathNameWithExt, "w") as fp:
            json.dump(data, fp)

    def read_json_file(self, key):
        with open(self.filename) as json_file:
            data = json.load(json_file)
            return data[key]
