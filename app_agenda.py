from utils import limpar_tela
from funcoes import *
from contato import Contato

lista_contatos: list[Contato] = []

while True:
    limpar_tela()
    mostrar_menu_agenda()
    opcao_escolhida = input("Escolha uma opção: ")
    
    match opcao_escolhida:
        case "1":
            cadastrar_contato(lista_contatos)
        case "2":
             ver_contatos(lista_contatos)
        case "3":
            editar_contato(lista_contatos)
        case "5":
            ver_contatos_favoritos(lista_contatos)
        case "6":
            apagar_contato(lista_contatos)
        case "0":
            break
        case _:  
            print("Opção inválida.")
limpar_tela()    
print("Programa encerrado")