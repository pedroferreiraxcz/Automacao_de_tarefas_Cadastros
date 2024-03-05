#  Passo 1: Entrar no sistema da empresa.
import pyautogui
from time import sleep
import pandas

pyautogui.PAUSE = 2

pyautogui.press("win")
pyautogui.write('chrome')
pyautogui.press('enter')

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

# Passo 2: Fazer o login
login = "email_qualquer@gmail.com"
senha = "987654321"
pyautogui.click(x=534, y=406)
pyautogui.write(login)
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.click(x=678, y=571)

# pyautogui.click -> Clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado.
# pyautogui.hotkey('ctrl', 'c')
# pyautogui.position() -> Identifica a posição da seta do mouse no momento que o codigo executar.
# pyautogui.scroll() -> O que vai dento do () vai ser um scroll pra cima ou pra baixo na pagina.

# Passo 3: Importar a base de dados
tabela = pandas.read_csv("Python- Power Up/produtos.csv")
# --> Tabela importada a baixo:
#         codigo       marca        tipo  categoria  preco_unitario  custo               obs
#0    MOLO000251    Logitech       Mouse          1           25.95    6.5               NaN
#1    MOLO000192    Logitech       Mouse          2           19.95    5.0               NaN
#2    CAHA000251     Hashtag      Camisa          1           25.00   11.0               NaN
#3    CAHA000252     Hashtag      Camisa          2           25.00   11.0  Conferir estoque
#4    MOMU000111  Multilaser       Mouse          1           11.99    3.4               NaN
#..          ...         ...         ...        ...             ...    ...               ...
#288  ACAP000192       Apple  Acessorios          2           19.00    3.8               NaN
#289  ACSA0009.3     Samsung  Acessorios          3            9.55    2.1               NaN
#290  CEMO000271    Motorola     Celular          1          279.00   72.5               NaN
#291  FOMO000152    Motorola        Fone          2          150.00   33.0               NaN
#292  CEMO000223    Motorola     Celular          3          229.00   55.0               NaN

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    # Campo codigo;
    codigo1 = tabela.loc[linha, 'codigo']
    pyautogui.click(x=618, y=292)
    pyautogui.write(str(codigo1))
    pyautogui.press('tab')

    # Campo marca;
    marca1 = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca1))
    pyautogui.press('tab')

    # Campo Tipo; 
    tipo1 = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo1))
    pyautogui.press('tab')

    # Campo Categoria;
    categoria1 = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria1))
    pyautogui.press('tab')

    # Campo preço;
    preco1 = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco1))
    pyautogui.press('tab')
    
    # Campos custo; 
    custo1 = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo1))
    pyautogui.press('tab')

# Caso a coluna obs esteja vazia, então irá pular.    
    if tabela.loc[linha, 'obs'] == '':
        pyautogui.press('tab')
        pyautogui.press('enter')
    else:
        pyautogui.write(str(tabela.loc[linha, 'obs']))
        pyautogui.press('tab')
        pyautogui.press('enter')
# Para rolar a tela para cima até o topo.
    pyautogui.scroll(5000)
