'''
Este script retorna informações de algumas açoes da bovespa.
Pasta você adicionar o codigo da ação na lista, que ele retornara informações da mesma
'''

import requests
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup
from class_acoes import Acoes

def varrendo_acoes():
    l_acoes = ['IBOV11', 'ITUB4', 'VALE3', 'ITUB4', 'B3SA3', 'BBAS3', 'GGBR4', 'BOVA11', 'ABEV3', 'PETR3',
               'LAME4', 'SANB11', 'CMIG4', 'ITSA4', 'BTOW3', 'RAIL3', 'PCAR4', 'AZUL4', 'USIM5']

    lista_resultado = []

    for a in l_acoes:
        page = requests.get("https://www.guiainvest.com.br/raiox/default.aspx?sigla=" + a + "")
        soup = BeautifulSoup(page.text, 'html.parser')
        empresa = soup.find(id='lbNomeEmpresa')
        codigo = soup.find(id='lbAcaoCodigo')
        ultimo_fechamento = soup.find(id='lbUltimoFechamento')
        maxima52s = soup.find(id='lbMaxima52Sem')
        minima52s = soup.find(id='lbMinima52Sem')
        qtd_negocios21d = soup.find(id='lbNumeroNegocioMedio21d')
        volume_medio = soup.find(id='lbVolumeMedio')

        lista_resultado.append(empresa.text)
        lista_resultado.append(codigo.text)
        lista_resultado.append(ultimo_fechamento.text)
        lista_resultado.append(maxima52s.text)
        lista_resultado.append(minima52s.text)
        lista_resultado.append(qtd_negocios21d.text)
        lista_resultado.append(volume_medio.text)

    lista_acoes = []
    colunas = 7
    tamanho_lista = len(lista_resultado)
    count = 0
    qtd_acoes = len(l_acoes)
    contador = 1

    while count < tamanho_lista:

        acoes = Acoes()
        acoes.empresa = lista_resultado[count]
        acoes.codigo = lista_resultado[count + 1]
        acoes.ultimo_fechamento = lista_resultado[count + 2]
        acoes.maxima52s = lista_resultado[count + 3]
        acoes.minima52s = lista_resultado[count + 4]
        acoes.qtd_negocios21d = lista_resultado[count + 5]
        acoes.volume_medio = lista_resultado[count + 6]
        acoes.data = datetime.today().date()
        count = count + colunas
        lista_acoes.append(acoes)
        print('Adicionado ação {}'.format(acoes.empresa), ' | ', contador, 'de', qtd_acoes)
        contador += 1

    conn = sqlite3.connect('../db.sqlite3')
    MyCursor = conn.cursor()

    for i in lista_acoes:
        MyCursor.execute(
            "INSERT INTO acoes (empresa, codigo, ultimo_fechamento, maxima52semanas, minima52semanas, qtdnegociado_21dias, volume_medio, data_json) VALUES (?,?,?,?,?,?,?,?)",

            [
                (i.empresa),
                (i.codigo),
                (i.ultimo_fechamento),
                (i.maxima52s),
                (i.minima52s),
                (i.qtd_negocios21d),
                (i.volume_medio),
                (i.data)

            ]
            )
    conn.commit()
    conn.close()

varrendo_acoes()