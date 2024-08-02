from classe_contato import Contato

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
    nome = input("Digite o nome do contato: ")
    tel = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato (opcional): ")
    favorito_str = input("É favorito? (sim/não): ")
    favorito = favorito_str.lower() == "sim"
    contato: Contato  = {
        "nome": nome,
        "tel": tel,
        "email": email,
        "favorito": favorito
    }
    lista_contatos.append(contato)
    print(f"Contato {nome} foi adicionada com sucesso!")   