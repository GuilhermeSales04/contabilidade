import json as js

def inserir (nome, preco, mes, status):
    try:
        file = open("contabilidade.json", "r")
        data = file.read()
        data = js.loads(data)
        file.close()
    except IOError:
        file = open("contabilidade.json", "w")
        data = []
        data.append({"nome_da_conta": nome, "preco": preco,"mes": mes, "status": status})
        js.dump(data, file, indent = 6)
        print("Conta Adicionado com Sucesso!")
        file.close()
        return
       
    i = 0
    for j in data:
        for k in data:
            nomec = data[i]["nome_da_conta"]
            mesc = data[i]["mes"]
            if nome.lower() == nomec.lower():
                if mes == mesc:
                    print("Conta ja existente!")
                    return
            i += 1
        file = open("contabilidade.json", "w")
        data.append({"nome_da_conta": nome, "preco": preco,"mes": mes, "status": status})
        js.dump(data, file, indent = 6)
        file.close()
        return

def is_number(value):
    if not value.strip().replace('-', '').replace('+', '').replace('.', '').isdigit():
        return False
    try:
         float(value)
    except ValueError:
         return False
    return True