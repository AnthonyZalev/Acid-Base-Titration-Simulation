
import json
class DataBase:

    def __init__(self):
        self.path = "./"
        self.filename = "AcidNameKADAtaBase.json"

    def WriteToJSONFIle(self, data):
        filePathNameWithExt = "./" + self.path + "/" + self.filename
        with open(filePathNameWithExt,"w") as fp:
            json.dump(data, fp)

    def ReadJSONFile(self, title):
        with open(self.filename) as json_file:
            data = json.load(json_file)
            return data[title]

Data = {}
Data["WeakSolutionNames"] = [
    "Acetic",
    "Ascorbic (I)",
    "Ascorbic (II)",
    "Benzoic",
    "Boric (I)",
    "Boric (II)",
    "Boric (III)",
    "Carbonic (I)",
    "Carbonic (II)",
    "Citric (I)",
    "Citric (II)",
    "Citric (III)",
    "Formic",
    "Hydrazidic",
    "Hydrocyanic",
    "Hydrofluoric",
    "Hydrogen Peroxide",
    "Hydrogen Sulfate Ion",
    "Hypochlorous",
    "Lactic",
    "Nitrous",
    "Oxalic (I)",
    "Oxalic (II)",
    "Phenol",
    "Propanic",
    "Sulfurous (I)",
    "Sulfurous (II)",
    "Uric",
    "Hydrochloric Acid",
    "Nitric Acid",
    "Hydroiodic Acid",
    "Perchloric Acid",
    "Chloric Acid",
    "Lithium Hydroxide",
    "Sodium Hydroxide",
    "Potassium Hydroxide"

]
Data["KAValues"] = [
    .000018,
    .000079,
    .0000000000016,
    .000064,
    .00000000054,
    .00000000000018,
    .00000000000016,
    .00000045,
    .000000000047,
    .00000032,
    .000017,
    .00000041,
    .00018,
    .000019,
    .00000000062,
    .00063,
    .0000000000024,
    .012,
    .000000035,
    .00083,
    .0004,
    .058,
    .000065,
    .00000000016,
    .000013,
    .014,
    .000000063,
    .00013,
    1,
    1,
    1,
    1,
    1,
    .000000000000001,
    .000000000000001,
    .000000000000001
                    ]
stuff = DataBase()
stuff.WriteToJSONFIle(Data)