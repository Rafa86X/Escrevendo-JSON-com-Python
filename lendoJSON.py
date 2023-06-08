import json

f = open("testeJSON.json", encoding="utf8")
testeJSON = json.load(f)

data = testeJSON["data1"][0]
print(data["ecolaridade"][2]["escola"])
