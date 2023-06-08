import json


def inseriDados(dadoAdicionaveis):
    
    f = open("data3.json", encoding="utf8")
    LeituraJSON = json.load(f)
    dados = LeituraJSON["dado"]
    dadoExtra = dadoAdicionaveis
    dados.append(dadoExtra)
    jsonDados = {"dado":dados}
    with open('data3.json', 'w') as f:
        json.dump(jsonDados, f, indent=2)


print("\n\n*********** Prenchendo o JSON ***********\n\n")

nome = input("\nDigite o Nome: ")
sobrenome = input("\nDigite o Sobrenome: ")
cargo = input("\nDigite o cargo: ")
chefe = input("\nChefe(True/False): ")
salario = input("\nDigite o Salario: ")
descricaoDasAtividades = input("\nDigite a Descrição das atividades: ")

dadoNovo = {"Nome":nome,"Sobrenome":sobrenome,"Cargo":cargo, "Chefe":chefe, 
            "Salario": salario, "Descricao das atividades":descricaoDasAtividades}

inseriDados(dadoNovo)
