from utils import limpar_tela
from funcoes import *
from classe_contato import Contato

lista_contatos: Contato = []

while(True):
    limpar_tela()
    ver_menu_agenda()
    opcao_escolhida = input("Digite a sua escolha: ")
    
    match opcao_escolhida:
        case "1":
            cadastrar_contato(lista_contatos)
        case "2":
             ver_contatos(lista_contatos)
        case "3":
            editar_contato(lista_contatos)
        case "7":
            break
        case _:  
            print("Opção inválida.")
limpar_tela()    
print("Programa finalizado")