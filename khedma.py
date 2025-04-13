from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome('chromedriver.exe')
browser.get("https://www.marocannonces.com/index.php?a=4")

blassa_dyal_Username = browser.find_element_by_id('username')
blassa_dyal_Username.send_keys("bouysfi.othman@gmail.com")
blassa_dyal_password = browser.find_element_by_id('password')
blassa_dyal_password.send_keys("123456789")

browser.find_element_by_xpath("//input[@type='submit' and @value='Valider']").click()
tsena_chwiya = time.sleep(15)


lien1 = "https://www.marocannonces.com/maroc/offres-emploi-domaine-informatique-multimedia-internet-casablanca-b309-t563.html?f_3=Informatique+%2F+Multim%C3%A9dia+%2F+Internet"



def postule ( ):
    postuler1 = browser.find_element_by_class_name("btn-reply")
    time.sleep(4)
    postuler1.click()
    time.sleep(12)
    smiya_dyalk = browser.find_element_by_id("c_senders_name")
    smiya_dyalk.send_keys("Othman Bouysfi")
    num_dyalk = browser.find_element_by_id("c_senders_phone")
    num_dyalk.send_keys("0637208455")
    postuler_final = browser.find_element_by_id("btn_envoyer")
    postuler_final.click()
    retour = browser.find_element_by_class_name("backtoads")
    retour.click()
    time.sleep(4)

lien1_de_depart = browser.get(lien1)


while True:
    try:
        postule()
        anance_suivant = browser.find_element_by_class_name("previous_ad_link")
        anance_suivant.click()
        time.sleep(60)
    except:
        browser.refresh()
        time.sleep(6)






