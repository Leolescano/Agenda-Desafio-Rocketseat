# Agenda de Contatos

Uma aplicação simples em Python para gerenciar contatos. O projeto permite cadastrar, listar, editar, favoritar e apagar contatos, além de visualizar contatos favoritos.

## Funcionalidades

- **Cadastrar contato**: Adiciona um novo contato à agenda.
- **Listar contatos**: Exibe todos os contatos cadastrados.
- **Editar contato**: Modifica informações de um contato existente.
- **Favoritar/Desfavoritar contato**: Marca um contato como favorito ou remove a marcação.
- **Listar contatos favoritos**: Mostra apenas os contatos que estão marcados como favoritos.
- **Apagar contato**: Remove um contato da agenda.

## Requisitos

- Python 3.x

## Instalação

1. Clone o repositório para o seu ambiente local:
    ```bash
   https://github.com/Leolescano/Agenda-Desafio-Rocketseat.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd agenda-contatos
    ```

3. Instale as dependências, se houver. Este projeto não possui dependências externas além da biblioteca padrão do Python.

## Uso

1. Execute o aplicativo:
    ```bash
    python app_agenda.py
    ```

2. Siga as instruções no terminal para interagir com a agenda de contatos.

## Estrutura do Projeto

- **`app_agenda.py`**: O script principal que executa a aplicação de agenda de contatos.
- **`contato.py`**: Define a estrutura dos contatos usando o tipo `TypedDict`.
- **`funcoes.py`**: Contém as funções principais para gerenciamento dos contatos.
- **`utils.py`**: Inclui funções utilitárias como limpar a tela e obter entradas do usuário.

## Próximos Passos 

- **Implementar persistência de dados**: Salvar os contatos em um arquivo para que eles não sejam perdidos ao fechar o programa.
- **Adicionar mais funcionalidades**:
  - Ordenar contatos por nome ou data de cadastro.
  - Importar/exportar contatos de/para um arquivo CSV.
  - Enviar e-mails ou SMS para os contatos.
- **Criar uma interface gráfica**: Usar uma biblioteca como Tkinter ou PyQt para criar uma interface gráfica mais amigável para a agenda.


## Contato

Para qualquer dúvida ou sugestão, entre em contato com [leolescanomdq@gmail.com](leolescanomdq@gmail.com).
