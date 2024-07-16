from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import pandas as pd
import time
import os

def download_file():
    """
    Faz o download de um arquivo da página da B3 usando o Selenium WebDriver.

    Esta função configura o WebDriver do Chrome para baixar arquivos automaticamente em um diretório especificado,
    navega até a página do índice IBOVESPA, seleciona uma opção de segmento e inicia o download de um arquivo.
    """

    path = os.getcwd().split('\\scripts')[0] + "\\raw_data"

    try:
        options = webdriver.ChromeOptions()
        prefs={"download.default_directory": path}

        options.add_experimental_option("prefs",prefs)
        options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=options)

        driver.get("https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br")

        time.sleep(5)

        campo_consulta = driver.find_element(By.ID, "segment")

        campo_consulta.click()

        time.sleep(3)

        opcao_setor_de_atuacao = driver.find_element(By.XPATH, '//*[@id="segment"]/option[2]')

        opcao_setor_de_atuacao.click()

        time.sleep(3)

        gotit = driver.find_element(By.XPATH, '//*[@id="divContainerIframeB3"]/div/div[1]/form/div[2]/div/div[2]/div/div/div[1]/div[2]/p/a')

        gotit.click()

        time.sleep(5)

        driver.close()
    except:
        raise Exception("Não foi possível baixar o arquivo.")