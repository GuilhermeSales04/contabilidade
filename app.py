from PySimpleGUI import PySimpleGUI as sg
from getPendentes import *
from inserirConta import *

#layout
def menu ():
    sg.theme("DarkBlue3")
    layout = [
        [sg.Button("Inserir Conta Pendente", size=(50,5), pad=((190,0), (160,0)))],
        [sg.Button("Visualizar Contas Pendentes", size=(50,5), pad=((190,0), (2,0)))],
        [sg.Text("By: Kiraa", justification='center',size=(100,1),pad=((0,0),(150,0)), font=("Arial", 12))]
    ]
    return sg.Window("Contabilidade V0.1", layout=layout, finalize=True, size=(800, 600))

def inserirConta ():
    sg.theme("Reddit")
    layout = [
        [sg.Text("Nome da Conta:"), sg.Input("", key="nome_conta")],
        [sg.Text("Valor:"), sg.Input("", key="preco")],
        [sg.Text("Mês Vigente:"), sg.Input("", key="mes")],
        [sg.Button("Confirm")]
    ]
    return sg.Window("Contabilidade V0.1", layout=layout, finalize=True, size=(500, 200))

def visualizarContas ():
    sg.theme("Reddit")
    stringC = createString()
    if stringC == False:
        d = "Nenhuma Conta Adicionada"
    else:
        d = "\n".join(stringC)
        d = d.replace(" ", "\n")
        d = d.replace(":", ": ")
        d = d.replace("&", " ")
    layout = [
        [sg.Multiline(d,size=(100,30), key="contas", font=("Arial", 22))],
        [sg.Button("Voltar", size=(180,60))]
    ]
    return sg.Window("Contabilidade V0.1", layout=layout, finalize=True, size=(600, 1200), resizable = True)

#janela
janela, janela2, janela3 = menu(), None, None
#eventos
while True:
    window, eventos, valores = sg.read_all_windows()
    if window == janela and eventos == sg.WINDOW_CLOSED:
        break
    if window == janela and eventos == "Inserir Conta Pendente":
        janela2 = inserirConta()
        janela.hide()
    if window == janela and eventos == "Visualizar Contas Pendentes":
        janela3 = visualizarContas()
        janela3.maximize()
    if window == janela2  and eventos == sg.WINDOW_CLOSED:
        janela2.close()
        janela.UnHide()
    if window == janela3  and eventos == sg.WINDOW_CLOSED:
        janela3.close()
        janela.UnHide()
    if window == janela2 and eventos == "Confirm":
        vpreco = valores["preco"].replace(",", ".")
        if len(valores["nome_conta"]) > 0 and is_number(vpreco) and valores["mes"].isdigit():
            inserir(valores["nome_conta"], float(vpreco), int(valores["mes"]), "Pendente")
            janela2.hide()
            janela.UnHide()
            sg.popup("Conta Pendente Adicionada!")
        else:
            sg.popup_error("Por favor insira valores validos!")
    if window == janela3 and eventos == "Voltar":
        janela3.hide()
        janela.UnHide()
janela.close()