Feature: Cadastro

    Scenario: Criação de conta no site Giuliana Flores
        Given que acesso o site Giuliana Flores
        And clico em perfil
        When sou redirecionado para a pagina de identificacao
        And clico em Criar Cadastro
        Then sou redirecionado para a pagina de Cadastro
        And preencho os campos de nome, cpf, e-mail, senha e endereco
        And verifico o botao de finalizar cadastro 
