#importaciones
import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
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
    driver.get('https://www.nike.com/ar/sportswear/launch/air-jordan-1-retro-high-og-mocha')
    time.sleep(3)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[3]/nav/div/div/div[2]/div/a[1]/div[2]/small')))\
    .click()
    time.sleep(2)
    while True:
        try: 
            driver.get('https://www.nike.com/ar/sportswear/launch/air-jordan-1-retro-high-og-mocha')
            time.sleep(2)
            iframe_source = driver.page_source 

            page = BeautifulSoup(iframe_source, 'html.parser')
            etiqueta = page.find_all('figcaption', class_="_13xDDA0A o0L_Z0WU _1bZ3CnEY")

            try:
                link = etiqueta[0].a['href']
            except:
                link = 0           

            if link != 0:
                embed = discord.Embed(title="NIKE", description= "Disponible para reserva", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue(), url= link)
                await ctx.send(embed= embed)                                

        except Exception as e:
            print("Ha ocurrido un error =>", type(e).__name__)        
            time.sleep(20)
            driver.delete_all_cookies()

bot.run("ODczNTkyODEwOTg3NzQxMjA0.YQ6qtA.vTsxfa7SllpWwPFIfewaQ8h-OPY")