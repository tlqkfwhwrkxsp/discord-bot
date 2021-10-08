from typing_extensions import runtime
from PIL import ImageGrab
from discord import message
from discord.errors import DiscordServerError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
import pyautogui
import time
import discord





client = discord.Client()

token = "ODkyMzIxMTAyMDExOTY1NDgw.YVLMyQ.JErNRQRFkb7CCeOWAJO-ptsGLgA"
 
@client.event
async def on_ready():

    print(client.user.name)
    print('ㅜㅜ.')
    game = discord.Game('ㅋㅋㄹㅃㅃ')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!자가진단"):
      await message.channel.send("기다리세요..")
      try:          
        driver = webdriver.Chrome()
        url = 'https://hcs.eduro.go.kr/#/loginHome'
        driver.maximize_window()
        driver.get(url)
           

        driver.maximize_window()
       

        driver.find_element_by_css_selector('#btnConfirm2').click()
  
        driver.find_element_by_css_selector('.searchBtn').click()

        driver.implicitly_wait(3)

        driver.find_element_by_id('sidolabel').click()
        driver.implicitly_wait(3)

        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td/select/option[16]').click()
        driver.implicitly_wait(3)
        driver.find_element_by_id('crseScCode').click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td/select/option[3]').click()
        driver.implicitly_wait(3)
        driver.find_element_by_class_name('searchArea').click()
        driver.find_element_by_class_name('searchArea').send_keys('경산압량초등학교')
        driver.implicitly_wait(3)
        driver.find_element_by_class_name('searchBtn').click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[1]/ul/li/a/p/a').click()
        driver.find_element_by_class_name('layerFullBtn').click()
        driver.implicitly_wait(3)
        driver.find_element_by_id('user_name_input').click()
        driver.find_element_by_id('user_name_input').send_keys('최성현')
        driver.implicitly_wait(3)
        driver.find_element_by_id('birthday_input').click()
        driver.find_element_by_id('birthday_input').send_keys('090227')
        driver.implicitly_wait(10)
        driver.find_element_by_id('btnConfirm').click()
        driver.implicitly_wait(10)
        time.sleep(0.3) #최소값 0.3초 
        driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/div[1]/table/tbody/tr/td/input[1]').click()
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//a[@aria-label='4']").click()
        driver.find_element_by_xpath("//a[@aria-label='8']").click()
        driver.find_element_by_xpath("//a[@aria-label='6']").click()
        driver.find_element_by_xpath("//a[@aria-label='0']").click()
        
        driver.find_element_by_id('btnConfirm').click()
        driver.implicitly_wait(10)
        time.sleep(0.7) #최소값 0.7초 
        driver.find_element_by_class_name('btn').click()
        driver.implicitly_wait(2)
        driver.find_element_by_id('survey_q1a1').click()
        driver.find_element_by_id('survey_q2a1').click()
        driver.find_element_by_id('survey_q3a1').click()

        from selenium.webdriver import ActionChains

        d = driver.find_element_by_id('btnConfirm')
        action = ActionChains(driver)
        action.move_to_element(d).perform()
        driver.implicitly_wait(3)
    
        d.click()
        await message.channel.send("성공!")
        driver.close()
        #time.sleep(500)

    

      except:
          await message.channel.send("오류가 발생했습니다. 다시 시도해주세요.")
          driver.close()
client.run(token)

















