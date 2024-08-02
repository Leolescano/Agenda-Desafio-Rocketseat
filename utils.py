import os

def limpar_tela()->None:
     # Limpar a consola no Git Bash
    os.system('clear')

def ingresar_nome()-> str | None:
    while True:
        nome = input("Digite o nome do contato: ")
        if nome == "":
            print(f"Nome não pode ficar vazio.")
        elif len(nome) <= 1:
            print("Nome não pode ficar vazio.")
        else:
            return nome
    
def ingresar_telefone()-> str | None:
    while True:
        tel = input("Digite o telefone do contato com DDD ## ######### :").strip()
        if tel == "":
            print("Tel não pode ficar vazio.")
        elif len(tel) != 12: 
            print("Formato incorreto. Use ## #########.")
        else:
            return tel    
 
def ingresar_email()-> str | None:
    while True:
        email = input("Digite o email do contato (opcional): ").strip()
        if ("@" in email and "."  in email) or email == "":
            return email
        else:    
            print("Email em formato invalido.")
        
       