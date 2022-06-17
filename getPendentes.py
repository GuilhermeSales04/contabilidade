from PySimpleGUI import PySimpleGUI as sg
from getMes import *
import json as js

def exibir ():
    try:
        with open("contabilidade.json") as file:
            data = js.load(file)
    except IOError:
        sg.popup("Você ainda não inseriu nenhuma conta no sistema!")
        return False
    i = 0
    pendentes = []
    for j in data:
        if data[i]["status"] == "Pendente":
            pendentes.append(data[i])
        i += 1
    return pendentes

def createString ():
    i = 0
    value = exibir()
    if value == False:
        return False
    else:
        b = []
        for m in value:
            mes = getMes(value[i]["mes"])
            name = value[i]["nome_da_conta"]
            name = name.replace(" ", "&")
            a = f"""{"-" * 20}
Nome:{name}
Valor:R${value[i]["preco"]}
Mês:{mes}"""
            a = a.replace("\n", " ")
            b.append(a)
            print(a)
            i += 1
        return b

