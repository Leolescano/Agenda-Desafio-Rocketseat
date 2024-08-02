from funcoes import *
from classe_contato import Contato

lista_contatos: Contato = []

while(True):
    
    ver_menu_agenda()
    opcao_escolhida = input("Digite a sua escolha: ")
    
    match opcao_escolhida:
        case "1":
            cadastrar_contato(lista_contatos)
        case "2":
             None
        case "3":
            None
        case "7":
            break
        case _:  
            print("Opção inválida.")
    
print("Programa finalizado")