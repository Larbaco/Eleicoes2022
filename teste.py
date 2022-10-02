
import requests
import json

data = requests.get("https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json")
json_data = json.loads(data.content)
#print(json_data['cand'])

for infor in json_data['cand']:
    print(infor['nm'])
    print(infor['seq'])
    print(infor['vap'])
    print(infor['pvap'])