from classe_contato import Contato
import os

def limpar_tela()->None:
     # Limpar a consola no Git Bash
    os.system('clear')

def ingresar_nome(uso: str)-> str:
    nome = ""
    while True:
        match uso:
            case "cadastrar":
                nome = input("Digite o nome do contato: ").strip()
            case "busqueda":
                nome = input("Digite o nome do contato buscado: ").strip()
            case "editar":
                nome = input("Digite o novo nome do contato: ").strip()
        if nome == "" or len(nome) <= 1:
            print("Nome não pode ficar vazio e nem ter só uma letra.")
        else:
            return nome
    
def ingresar_telefone(uso: str)-> str:
    while True:
        match uso:
            case "cadastrar":
                tel = input("Digite o número de telefone com DDD ## #########: ").strip()
            case "busqueda":
                tel = input("Digite o número de telefone a ser buscado: ").strip()
            case "editar":
                 tel = input("Digite o novo número de telefone com DDD ## #########: ").strip()            
        if tel == "":
            print("Tel não pode ficar vazio.")
        elif len(tel) != 12: 
            print("Formato incorreto. Use ## #########.")
        else:
            return tel    
 
def ingresar_email(uso: str)-> str: 
    while True:
        match uso:
            case "cadastrar":    
                email = input("Digite o email do contato (opcional): ").strip()
            case "busqueda":
                email = input("Digite o email do contato buscado: ").strip()
            case "editar":
                email = input("Digite o novo email do contato: ").strip()
        if (email == ""):
            return "NÃO informado"
        if ("@" in email and "."  in email):
            return email
        else:    
            print("O e-mail deve conter um símbolo '@' e um ponto final após o '@'.")
            
def ingresar_favorito()-> bool:
    while True:
        favorito = input("É favorito? (s/n): ").lower().strip()
        if favorito == "" or favorito == 's':
            return True
        elif favorito == "n":
            return False
        else:
            print("Opção invalida.")    
            
def verificar_lista(contatos: list[Contato])-> bool:
    if not contatos:
        print("Você ainda não possui contatos em sua agenda.")
        input()
        return False
    return True                 