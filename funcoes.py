from classe_contato import Contato
from utils import ingresar_nome, ingresar_telefone, ingresar_email, limpar_tela

def ver_menu_agenda()-> None:
    print("\nMenu do Gerenciador da Agenda")
    print("1. Cadastrar contato")
    print("2. Visualizar contatos cadastrados")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar um contato como favorito")
    print("5. Ver lista de contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair do programa")
    
def cadastrar_contato(lista_contatos: list[Contato]) -> None:
    limpar_tela()
    nome = ingresar_nome(); 
    tel = ingresar_telefone()
    email = ingresar_email()
    favorito_str = input("É favorito? (s/n): ")
    favorito = favorito_str.lower() == "s"
    contato: Contato  = {
        "nome": nome,
        "tel": tel,
        "email": email,
        "favorito": favorito
    }
    lista_contatos.append(contato)
    print(f"Contato {nome} foi adicionada com sucesso!") 
    
def ver_contatos(contatos: list[Contato]) -> None:
    if not contatos:
        print("Você ainda não possui contatos cadastrados.")
        return
    
    print("\nLista de Contatos") 
    for i, contato in enumerate(contatos, start = 1):
        nome = contato["nome"]
        tel = contato["tel"]
        email = contato["email"]
        status = "✓" if contato["favorito"] == True else "" #"✓"
        print(f"""{i}. Nome: {nome}
    Telefone: {tel}
    E-mail: {email}
    Favorito: [{status}]""") 
    input()    
        
        