from contato import Contato
import os

def limpar_tela() -> None:
    os.system('clear' if os.name != 'nt' else 'cls')

def ingresar_nome(motivo_uso: str) -> str:
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
                telefone = input("Digite o telefone (ex: 11 912345678): ").strip()
            case "busca":
                telefone = input("Digite o telefone a ser buscado (ex: 11 912345678): ").strip()
            case "editar":
                 telefone = input("Digite o novo telefone (ex: 11 912345678): ").strip()            
        
        if not telefone:
            print("O telefone não pode estar vazio.")
        else:
            telefone_tratado = ""
            for carater in telefone:
                if carater.isdigit():
                    telefone_tratado += carater
            if len(telefone_tratado) != 11: 
                print("Formato de telefone inválido (ex: 11 912345678).")
            else:
                telefone_formatado =f"+{telefone_tratado[:2]} {telefone_tratado[2:7]}-{telefone_tratado[7:]}"
                return telefone_formatado  
 
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
    for contato in contatos:
        if contato["favorito"] == True:
            contatos_filtrados.append(contato)
    return contatos_filtrados

def buscar_telefone(contatos: list[Contato], tel_buscado) -> bool:
    for contato in contatos:
        if contato["telefone"] == tel_buscado:
            return True
    return False
       
                              