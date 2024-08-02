from classe_contato import Contato
from utils import *

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
    nome = ingresar_nome("cadastrar"); 
    tel = ingresar_telefone("cadastrar")
    email = ingresar_email("cadastrar")
    favorito = ingresar_favorito()
    contato: Contato  = {
        "nome": nome,
        "tel": tel,
        "email": email,
        "favorito": favorito
    }
    lista_contatos.append(contato)
    print(f"Contato {nome} foi adicionada com sucesso!") 
    
def ver_contatos(contatos: list[Contato]) -> None:
    limpar_tela()
    if verificar_lista(contatos):
        print("Lista de Contatos") 
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
        
def buscar_contato(contatos: list[Contato])-> Contato | None:
    limpar_tela()
    while True:
        print("Buscar contato para ser editado:")
        print("1. Por Nome")
        print("2. Por Telefone")
        print("3. Por E-mail")
        print("4. Voltar ao menu principal")
        escolha = input("Digite a sua escolha: ")
        match escolha:
                case "1":
                    criterio_busqueda = "nome"
                    buscado = ingresar_nome("busqueda")
                    break
                case "2":
                    criterio_busqueda = "tel"
                    buscado = ingresar_telefone("busqueda")
                    break
                case "3":
                    criterio_busqueda = "email"
                    buscado = ingresar_email("busqueda")
                    break
                case "4":
                    break
                case _:  
                    print("Opção inválida.")
    if escolha != "4":
        for i, cont in enumerate(contatos):
            if cont[criterio_busqueda] == buscado: 
                return cont
        print("Contato no encontrado na agenda.")  
        input()
        return None

def editar_contato(contatos: list[Contato])-> None:
    limpar_tela()
    if verificar_lista(contatos):
        contato = buscar_contato(contatos) 
        contador = 0
        valor_editado = ""
        while contato is not None:
            limpar_tela()
            mensagem = "Contato Encontrado" if contador == 0 else f"O {valor_editado} foi Editado com sucesso"
            print(mensagem)
            print(f"1. Nome: {contato['nome']}")
            print(f"2. Telefone: {contato['tel']}")
            print(f"3. E-mail: {contato['email']}")
            print("4. Voltar para o menu principal.")
            escolha = input("Digite a sua escolha: ")
            match escolha:
                case "1":
                    contato["nome"] = ingresar_nome("editar")
                    valor_editado = "Nombre"
                case "2":
                    contato["tel"] = ingresar_telefone("editar")
                    valor_editado = "Telefone"
                case "3":
                    contato["email"] = ingresar_email("editar")                
                    valor_editado = "Email"
                case "4":
                    break
                case _:  
                    print("Opção inválida.")
            contador += 1        
    
    
    
        
        