from contato import Contato
from utils import *

def mostrar_menu_agenda() -> None:
    print("\n--- Menu da Agenda ---")
    print("1. Cadastrar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Favoritar/Desfavoritar contato")
    print("5. Listar contatos favoritos")
    print("6. Apagar contato")
    print("0. Sair")

    
def cadastrar_contato(lista_contatos: list[Contato]) -> None:
    limpar_tela()
    nome = ingresar_nome("cadastrar"); 
    while True:
        telefone = ingresar_telefone("cadastrar")
        if not buscar_telefone(lista_contatos, telefone):
            break 
        else:
            print("Esse numero já foi cadastrado")
             
    email = ingresar_email("cadastrar")
    favorito = ingresar_favorito()
    contato: Contato  = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": favorito
    }
    lista_contatos.append(contato)
    print(f"Contato {nome} cadastrado com sucesso!") 
    
def ver_contatos(contatos: list[Contato]) -> None:
    if verificar_lista(contatos):
        print("Lista de Contatos:") 
        for i, contato in enumerate(contatos, start = 1):
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            status = "✓" if contato["favorito"] == True else "" 
            print("------------------------")
            print(f"{i}. Nome: {nome}")            
            print(f"Telefone: {telefone}")
            print(f"E-mail: {email}")
            print(f"Favorito: [{status}]")        
            print("------------------------")
            if i % 3 == 0:
                input("\nPressione Enter para continuar...\n")   
        input("\nPressione Enter para volver ao menu principal...")   
        
def buscar_contato (contatos: list[Contato], mensagem: str) -> Contato | None:
    if verificar_lista(contatos):
        while True:
            print(mensagem)
            print("1. Por Nome")
            print("2. Por Telefone")
            print("3. Por E-mail")
            print("0. Voltar ao menu principal")
            escolha = input("Escolha uma opção: ")
            
            match escolha:
                    case "1":
                        criterio_busqueda = "nome"
                        buscado = ingresar_nome("busca")
                        break
                    case "2":
                        criterio_busqueda = "telefone"
                        buscado = ingresar_telefone("busca")
                        break
                    case "3":
                        criterio_busqueda = "email"
                        buscado = ingresar_email("busca")
                        break
                    case "0":
                        return None
                    case _:  
                        print("Opção inválida.")
        
        for contato in contatos:
            if contato[criterio_busqueda] == buscado: 
                return contato
        print("Contato não encontrado.")  
        input("Pressione Enter para continuar...")
        return None

def editar_contato(contatos: list[Contato]) -> None:
    mensagem = "Buscar contato para editar:"
    contato = buscar_contato(contatos, mensagem) 
    contador = 0
    valor_editado = ""
    while contato is not None:
        limpar_tela()
        mensagem = "Contato Encontrado" if contador == 0 else f"O {valor_editado} foi Editado com sucesso!"
        print(mensagem)
        print(f"1. Nome: {contato['nome']}")
        print(f"2. Telefone: {contato['telefone']}")
        print(f"3. E-mail: {contato['email']}")
        print("0. Voltar para o menu principal.")
        escolha = input("Escolha uma opção: ")
        
        match escolha:
            case "1":
                contato["nome"] = ingresar_nome("editar")
                valor_editado = "nombre"
            case "2":
                contato["telefone"] = ingresar_telefone("editar")
                valor_editado = "telefone"
            case "3":
                contato["email"] = ingresar_email("editar")                
                valor_editado = "email"
            case "0":
                break
            case _:  
                print("Opção inválida.")
        contador += 1  
            
def favoritar_desfavoritar_contato(contatos: list[Contato]) -> None:
    mensagem = "Buscar contato para favoritar/desfavoritar:"
    contato = buscar_contato(contatos, mensagem)
    if contato is not None:
        contato["favorito"] = not contato["favorito"]
        status = "favorito" if contato["favorito"] else "não favorito"
        print(f"O contato {contato['nome']} agora é {status}.")
        input("Pressione Enter para continuar...")

def ver_contatos_favoritos(contatos: list[Contato]) -> None:
    if verificar_lista(contatos):
       contatos_filtrados = filtrar_lista(contatos) 
       ver_contatos(contatos_filtrados)
             
def apagar_contato(contatos: list[Contato]) -> None:
    mensagem = "Buscar contato para apagar:"
    contato  = buscar_contato(contatos, mensagem)
    if contato is not None:
        while True:
            escolha = input(f"O contado {contato['nome']} foi encontrado, confirma que vai apagá-lo? (s/n)").lower().strip()
            if escolha == "s":
                contatos.remove(contato) 
                print("Contato apagado com sucesso.")  
                break
            elif escolha == "n":
                print("Operação cancelada.")  
                break
            else:
                print("Opção inválida. Digite 's' para sim ou 'n' para não.")
        input("Pressione Enter para continuar...")






