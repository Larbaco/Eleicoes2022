import time
import requests
import json
import pandas as pd
from os import system

def carrega_Hora(): 
    data = requests.get('http://worldtimeapi.org/api/timezone/America/Sao_Paulo')
    json_data = json.loads(data.content)
    return json_data['datetime']

def atualiza():    
    candidato = []
    partido = []
    votos = []
    porcentagem = []
    data = requests.get("https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json")
    json_data = json.loads(data.content)
    #print(json_data)
    print('Horario da ultima Atualização: '+json_data['ht'])
    print('Total Apurado: '+json_data['pst']+' %')
    print('Quantidade total de votos apurados: '+json_data['c'])
    for info in json_data['cand']:
        #if info['seq'] in [1,2,3,4,5,6,7]:
        if(info['nm'] == 'JAIR BOLSONARO'):
            candidato.append('Jair Genocida Bozonaro')
        else:
            candidato.append(info['nm'])
        votos.append(info['vap'])
        porcentagem.append(info['pvap']+' %')
        #print(candidato)

    df_eleicao = pd.DataFrame(list(zip(candidato,votos,porcentagem)), columns=['Candidato','Numero de Votos','Porcentagem'])
    print(df_eleicao)
    return json_data['ht']
ultima= ''
#hora = carrega_Hora()
while True:
    try:
        system('cls')
        print('/************* Eleicoes 2022 família buscapé ***************/')
        #print(hora)
        anterior = ultima
        ultima = atualiza()
        '''
        if(ultima != anterior):
            print('MUDOU')'''
        time.sleep(30)
        #hora = carrega_Hora()
    except:
        print('Erro de Conexão')
        time.sleep(5)