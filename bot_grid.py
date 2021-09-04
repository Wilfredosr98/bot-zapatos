#importaciones
import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import datetime



#configuraciones
options =  webdriver.ChromeOptions()
options.add_argument('--headless')
driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)
Lista_interna = []
bot = commands.Bot(command_prefix='@bot ', description="Soy wilbot")           



#bot de discord funcionamiento
@bot.event
async def on_ready():
    print("Soy bot, estoy conectado....")

@bot.command()
async def iniciar(ctx):
    while True:
        try: 
            #pruebas
            driver.get('https://www.grid.com.ar/jordan')
            time.sleep(3)
            iframe_source = driver.page_source 

            #manejo de la informacion 
            #extracción de la pagina
            page = BeautifulSoup(iframe_source, 'html.parser')
            etiqueta = page.find_all('div', class_="prateleira vitrine shelf n1colunas")
            contenido = etiqueta[0]
            link = contenido.find_all('div', id ="product")
            precio = contenido.find_all('span', class_ ="best-price")

            for l in range(0,8,1):
                if link[l].a['href'] not in Lista_interna:
                    Lista_interna.append(link[l].a['href'])
                    links = link[l].a['href']
                    name = link[l].a['title']
                    imag = link[l].img["src"]
                    price = precio[l].text
                    embed = discord.Embed(title="GRID", description= name, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= links)
                    embed.set_thumbnail(url= imag)
                    embed.add_field(name = "Pay in $", value = price)
                    await ctx.send(embed= embed)                                

        except Exception as e:
            print("Ha ocurrido un error =>", type(e).__name__)        
            time.sleep(20)
            driver.delete_all_cookies()



bot.run("ODcyNjE2MDEzMzU3NzkzMzEx.YQsc_g.KrlqsIhKEHDTp3yH6oUTDX6to20")