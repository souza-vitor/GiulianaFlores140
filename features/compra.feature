Feature: Compra no site

    Scenario: Compra de flores no site
        Given que acesso o site Giuliana Flores
        And clico no banner
        When preencho o campo endereco
        And seleciono o produto
        Then confirmo uma data de entrega
        And checo o carrinho de compras
