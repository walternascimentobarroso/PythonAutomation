# Step 1 - Open browser in correct link
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Define o caminho para o diretório onde o perfil do usuário será armazenado
profile_directory = "/Users/macbook/Library/Application Support/Google/Chrome/Default"

chrome_options = webdriver.ChromeOptions()
# Define o diretório do perfil do usuário
chrome_options.add_argument("user-data-dir=" + profile_directory)

# Inicializa o serviço do ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicializa o navegador com as opções e o serviço definidos
nav = webdriver.Chrome(service=service, options=chrome_options)
nav.get("https://web.whatsapp.com")

# Deixa o navegador aberto por 10 segundos
time.sleep(20)

# Step 2 - send message for me
from selenium. webdriver.common.keys import Keys
import pyperclip

message = """Bom dia!, Ja saiu?!"""

lista_contatos = ["Walter Old Number", "Teste", "Walter PT"]

# enviar a mensagem para O Meu Numero para poder depois encaminhar

# clicar na lupa
nav.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
nav.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(lista_contatos[0])
nav.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(1)

# escrever a mensagem para nós mesmos
pyperclip.copy(message)
nav.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(pyperclip.paste())
nav.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
time.sleep(1)

# Step 3 - Encaminhar a mensagem para a lista de contatos
from selenium.webdriver.common.action_chains import ActionChains




qtde_contatos = len(lista_contatos)
if qtde_contatos % 5 == 0:
    qtde_blocos = qtde_contatos / 5
else:
    qtde_blocos = int(qtde_contatos / 5) + 1

for i in range(qtde_blocos):
    # rodar o codigo de encaminhar
    i_inicial = i * 5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

    # Seleciona a mensagem para enviar e abre a caixa de encaminhar

    lista_elementos = nav.find_elements(By.CLASS_NAME, '_2AOIt')
    elemento = None  # Inicializa a variável 'elemento'

    for item in lista_elementos:
        message = message.replace("\n", "")
        texto = item.text.replace("\n", "")
        if message in texto:
            elemento = item

    ActionChains(nav).move_to_element(elemento).perform()
    elemento.find_element(By.CLASS_NAME, '_3u9t-').click()
    time.sleep(1)

    nav.find_element(By.XPATH, '//*[@id="app"]/div/span[4]/div/ul/div/li[4]/div').click()
    nav.find_element(By.XPATH, '//*[@id="main"]/span[2]/div/button[4]/span').click()
    time.sleep(3)

    for nome in lista_enviar:
        # escrever o nome do contato
        nav. find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(nome)
        time.sleep(1)
        # dar enter
        nav.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        time.sleep(1)
        # apagar O nome do contato
        nav.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
        time.sleep(1)

    nav.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(5)


