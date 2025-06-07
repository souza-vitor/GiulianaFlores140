Feature: Login no site

    Scenario: Autenticar no site
        Given que acesso o site Giuliana Flores
        And clico em perfil
        When sou redirecionado para a pagina de identificacao
        And preencho o campo e-mail e senha
        Then sou redirecionado para a pagina principal e faço logout

    Scenario: login com senha invalida
        Given que acesso o site Giuliana Flores
        And clico em perfil
        When sou redirecionado para a pagina de identificacao
        And preencho errado o campo e-mail e senha
        Then recebo um aviso de erro no login