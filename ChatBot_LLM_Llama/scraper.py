from autoscraper import AutoScraper
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def buscar_melhor_preco(palavras_chave):
    with open('ecommerce_config.json', 'r') as f:
        config = json.load(f)

    resultados = []

    for site in config['sites']:
        navegador = None
        try:
            url = site["url_base"]
            xpath = site["xpath_busca"]

            navegador = webdriver.Chrome()
            navegador.get(url)
            time.sleep(2)

            campo_busca = navegador.find_element(By.XPATH, xpath)
            campo_busca.send_keys(palavras_chave)
            campo_busca.send_keys(Keys.RETURN)
            time.sleep(4)

            scraper = AutoScraper()
            resultados_parciais = scraper.build(navegador.current_url, wanted_list=["R$ 1.000", "iPhone 14"])
            resultados.append({site["nome"]: resultados_parciais})

        except Exception as e:
            resultados.append({site["nome"]: f"Erro: {str(e)}"})

        finally:
            if navegador:
                try:
                    navegador.quit()
                except:
                    pass

    return resultados
