import pyautogui
import time
from selenium import webdriver
navegador = webdriver.Chrome("chromedriver.exe")
navegador.get ("https://br.indeed.com/?r=us")
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="text-input-what"]').send_keys('suabusca')
pyautogui.press("ENTER")


navegador.find_element_by_link_text[("Candidate-se Via Indeed")].click()




