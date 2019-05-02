import json

def  WriteToJSONFIle(path,filename,data):
    filePathNameWithExt = "./" + path + "/" + filename + ".json"
    with open(filePathNameWithExt,"w") as fp:
        json.dump(data, fp)

path = "./"
filename = "AcidNameKADAtaBase.json"
