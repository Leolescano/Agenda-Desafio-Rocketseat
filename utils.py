from contato import Contato
import os

def limpar_tela() -> None:
    os.system('clear' if os.name != 'nt' else 'cls')

def ingresar_nome(motivo_uso: str) -> str:
    # nome = ""
    while True:
        match motivo_uso:
            case "cadastrar":
                nome = input("Digite o nome do contato: ").strip()
            case "busca":
                nome = input("Digite o nome do contato a ser buscado: ").strip()
            case "editar":
                nome = input("Digite o novo nome do contato: ").strip()
        if not nome or len(nome) <= 1:
            print("Nome inválido. O nome deve conter pelo menos duas letras.")
        else:
            return nome
    
def ingresar_telefone(motivo_uso: str) -> str:
    while True:
        match motivo_uso:
            case "cadastrar":
                telefone = input("Digite o telefone (com DDD): ").strip()
            case "busca":
                telefone = input("Digite o telefone a ser buscado (com DDD): ").strip()
            case "editar":
                 telefone = input("Digite o novo telefone (com DDD): ").strip()            
        if not telefone:
            print("Telefone inválido. O telefone não pode estar vazio.")
        elif not telefone.isdigit() or len(telefone) != 3: 
            print("Formato de telefone inválido. Use (##) #########.")
        else:
            return telefone    
 
def ingresar_email(motivo_uso: str) -> str: 
    while True:
        match motivo_uso:
            case "cadastrar":    
                email = input("Digite o e-mail (opcional): ").strip()
            case "busca":
                email = input("Digite o e-mail a ser buscado: ").strip()
            case "editar":
                email = input("Digite o novo email: ").strip()
        if not email:
            return "Nao informado"
        if "@" in email and "."  in email and len(email) > 7:
            return email
        else:    
            print("E-mail inválido. Verifique se o e-mail está correto.")
            
def ingresar_favorito() -> bool:
    while True:
        favorito = input("O contato é favorito? (s/n): ").lower().strip()
        if favorito == 's':
            return True
        elif favorito == "n":
            return False
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")    
            
def verificar_lista(contatos: list[Contato]) -> bool:
    limpar_tela()
    if not contatos:
        print("A agenda está vazia.")
        input("Pressione Enter para continuar...")
        return False
    return True   

def filtrar_lista(contatos: list[Contato]) -> list[Contato]:
    contatos_filtrados: list[Contato] = []
    for _, contato in enumerate(contatos):
        if contato["favorito"] == True:
            contatos_filtrados.append(contato)
    return contatos_filtrados
       
                              