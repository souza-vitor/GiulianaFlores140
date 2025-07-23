# GiulianaFlores140

## Introdução
Este projeto automatiza testes para o site Giuliana Flores, focando em cenários de cadastro de usuário, autenticação e compra de produtos. Utiliza a abordagem BDD (Behavior Driven Development) para descrever os requisitos de negócio de forma compreensível para todos os envolvidos.

## Ferramentas Utilizadas
- **Python**: Linguagem principal para automação dos testes.
- **Behave**: Framework BDD para Python, utilizado para escrever e executar os cenários de teste descritos em Gherkin.
- **Selenium**: Ferramenta para automação de browsers, utilizada para interagir com a interface web durante os testes.

## Estrutura do Projeto
- `features/`: Contém os arquivos `.feature` com os cenários de teste e a pasta `steps/` com as implementações dos passos.
- `test_*.py`: Scripts de teste adicionais.

## Como Executar Localmente
1. **Clone o repositório:**
   ```powershell
   git clone https://github.com/souza-vitor/GiulianaFlores140.git
   cd GiulianaFlores140
   ```
2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. **Instale as dependências:**
   ```powershell
   pip install behave selenium
   ```
4. **Execute os testes:**
   ```powershell
   behave
   ```