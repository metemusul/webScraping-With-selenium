from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import openai
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
from getpass import getpass


# Google oturumu açılacak ilk önce
# GOOGLE OTURUM AÇMA KODU

url = "https://www.google.com/"

username = getpass("Username:musulmete129@gmail.com")
password = getpass("Password:Preomygame23231.")

service = Service(ChromeDriverManager().install())
browser = uc.Chrome(service=service)
browser.maximize_window()

browser.get(url)
browser.implicitly_wait(5)
# oturumacmabutonu = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div/div/div[2]/a").click()
# browser.implicitly_wait(5)

# emailinput =  browser.find_element(By.ID, "identifierId")
# time.sleep(1)
# emailinput.send_keys("musulmete129@gmail.com")
# time.sleep(1)
# emailinput.send_keys(Keys.ENTER)
# time.sleep(10)


# passwordinput =  browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
# if  passwordinput:

#     time.sleep(10)
#     passwordinput.send_keys("Preomygame23231.")
#     time.sleep(1)
#     passwordinput.send_keys(Keys.ENTER)
#     time.sleep(5)
# else:
#     passwordinput1 =  browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
#     time.sleep(10)
#     passwordinput1.send_keys("Preomygame23231.")
#     time.sleep(1)
#     passwordinput1.send_keys(Keys.ENTER)
#     time.sleep(5)


# # GOOGLE OTURUM AÇMA BİTİŞ


# # Hepsiburadaya giriş

searchbar = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
time.sleep(1)
searchbar.send_keys("getiryemek")
time.sleep(1)
searchbar.send_keys(Keys.ENTER)
time.sleep(5)



siteyetıklama = browser.find_element(By.CLASS_NAME, "MBeuO")
                                              
browser.implicitly_wait(100)
siteyetıklama.click()
time.sleep(2)

telgiris = browser.find_element(By.CLASS_NAME,"hdcxmp")
telgiris.send_keys("5312962764")
time.sleep(2)
telgiris.send_keys(Keys.ENTER)
time.sleep(20)
browser.execute_script("window.scrollBy(0,50)","")



# restoransayısı = browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/section/section[4]/div/header/div/div[1]/div/p/span[1]")
# value = restoransayısı.text
# print(value)
main_page = browser.current_window_handle


time.sleep(20)
restoranlar = []

# Veri toplama döngüsü içindeki mevcut kodlarınız buraya gelecek
# Her bir restoran için gerekli verileri alıp, bir sözlük içine yerleştirerek restoranlar listesine ekleyin

magaza_sayac = 0
for i in range(1,491):
    
    if (i % 2 == 0):
        browser.execute_script("window.scrollBy(0,200)","")


    close_check_product = "/html/body/div/div[2]/main/div/section/section[4]/div/section/article[{0}]/div/div/div[2]/div[2]/div/div".format(i)
    check_control_path = browser.find_element(By.XPATH,close_check_product)
    time.sleep(3)
    if(check_control_path.text == "Kapalı"):
        continue
    product_xpath = "/html/body/div[1]/div[2]/main/div/section/section[4]/div/section/article[{0}]/div/div/div[2]/div[1]/a/figure/img".format(i)
    product = browser.find_element(By.XPATH,product_xpath)
    time.sleep(2)

    # Siteye tıklama işlemi
    actions = ActionChains(browser)


    # Ctrl tuşunu basılı tut
    actions.key_down(Keys.CONTROL)

    # Elemente tıkla
    actions.click(product)

    # Ctrl tuşunu bırak
    actions.key_up(Keys.CONTROL)

    # Eylemleri gerçekleştir
    actions.perform()

    # Yeni açılan sekmeye geç
    new_tab = browser.window_handles[-1]  # Son açılan sekmeyi al
    browser.switch_to.window(new_tab)
    time.sleep(5)

    hakkımızda = browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div[2]/h2[3]")
    hakkımızda.click()

    time.sleep(3)

    starrate = browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div/div/div/div[1]/div[1]/div/div[2]/div[2]/div/span[1]")
    print("mağaza genel puanı : " , starrate.text)
    starview = " "
    if(float(starrate.text) > 4.50):
        starview = "⭐⭐⭐⭐⭐"
        print(starview)
    elif(float(starrate.text) > 4.00):
        starview = "⭐⭐⭐⭐"
        print(starview)
    elif(float(starrate.text) > 3.00):
        starview = "⭐⭐⭐"
        print(starview)
    elif(float(starrate.text) >2.00):
        starview = "⭐⭐"
        print(starview)
    elif(float(starrate.text) > 1.00):
        starview = "⭐"
        print(starview)
    else:
        print( " mağaza Rate edilmemiştir !!!")

    time.sleep(1)
    print(" ")


    
    teslimatOptions = browser.find_element(By.CLASS_NAME,"ectCYf")
    print(teslimatOptions.text)

    time.sleep(1)
    print(" ")
    teslimat_text = teslimatOptions.text
    splitteslimat_text = teslimat_text.split("\n")
    print(splitteslimat_text)
    

    payOptions = browser.find_element(By.CLASS_NAME,"zUZMx")
    print(payOptions.text)
    time.sleep(1)
    print(" ")
    pay_text = payOptions.text
    splitpay_text = pay_text.split("\n")
    print(splitpay_text)



    workHours = browser.find_element(By.CLASS_NAME,"eLrWax")
    print(workHours.text)
    time.sleep(1)
    print(" ")
    work_text = workHours.text
    splitwork_text = work_text.split("\n")
    print(splitwork_text)


    exInfo = browser.find_element(By.CLASS_NAME,"jvUbWr")
    print(exInfo.text)
    time.sleep(1)
    print(" ")
    info_text = exInfo.text
    splitinfo_text = info_text.split("\n")
    print(splitinfo_text)
    print(" ")


    

    comments = browser.find_element(By.XPATH,"/html/body/div/div[2]/main/div/div/div[1]/div[2]/h2[2]").click()
    time.sleep(1)
    magazaname = browser.find_element(By.XPATH,"/html/body/div/div[2]/main/div/div/div/div[1]/div/div/div[2]/div[2]/h1")
    time.sleep(1)
    print("MAĞAZA İSİM  :  ",magazaname.text)
    restoran = {
        "name": magazaname.text,
        "url": "Restoran URL'si",
        "servesCuisine": ["Mutfak Türü"],
        "price-category": "TL",
        "phoneNumbers": [{"number": "Telefon Numarası", "type": "Telefon Tipi"}],
        "address": {
            "postOfficeBox": "Posta Kutusu",
            "streetAddress": "Cadde/Sokak",
            "locality": "İstanbul",
            "region": "Marmara",
            "postalCode": "Posta Kodu",
            "countryName": "Türkiye"
        },
       
        "starRating": starview,
        "deliveryOptions":splitteslimat_text,
        "paymentOptions": splitpay_text,
        "workingHours": splitwork_text,
        "extraInfo": splitinfo_text,
        "comments": []  # Yorumlar için boş bir liste
    }

    # Verileri restoran sözlüğüne ekleyin

        
        

    j = 1
    k = 1
    
    # yorum sayısı alma 
    commnet_number = browser.find_element(By.XPATH,"/html/body/div/div[2]/main/div/div/div/div[4]/div[1]/span")
    text = commnet_number.text
    number = int(''.join(filter(str.isdigit, text)))
    print("The extracted number is:", number)
    
    time.sleep(1)
    comments_list = []
    if(number < 21 ):
        for j in range(1, number+1):
            xpath = f"/html/body/div[1]/div[2]/main/div/div/div[1]/div[4]/div[2]/div[{j}]/div[2]/span"
            comment_text = browser.find_element(By.XPATH, xpath).text
            print(f"COMMENT {j}: {comment_text}")
            comments_list.append(comment_text)  # Yorumları listeye ekle
            browser.execute_script("window.scrollBy(0, 250)")
            print(j)
            time.sleep(0.2)

    else:
        num = 1
        for j in range(1, number+1):
        
            xpath = f"/html/body/div[1]/div[2]/main/div/div/div[1]/div[4]/div[2]/div[{num}]/div[2]/span"
            comment_text = browser.find_element(By.XPATH, xpath).text
            print(f"COMMENT {j}: {comment_text}")
            comments_list.append(comment_text)  # Yorumları listeye ekle
            browser.execute_script("window.scrollBy(0, 250)")
    
            time.sleep(0.2)
            num +=1

            if j % 20 == 0:
                comment_next_page = browser.find_element(By.XPATH, "/html/body/div/div[2]/main/div/div/div[1]/div[4]/div[3]/nav/ul/li[last()]")
                if comment_next_page:
                    time.sleep(2)
                    comment_next_page.click()
                    time.sleep(2)
                    num = 1

    time.sleep(3)
    magaza_sayac += 1
    print("mağaza sayısı ",  magaza_sayac)
    # Oluşturulan yorumları restoran sözlüğünün comments listesine ekleyin
    restoran["comments"] = comments_list

    restoranlar.append(restoran)
        # Her döngü adımında JSON dosyasını güncelleyin
    with open('restoran_verileri_ankara_x.json', 'w',encoding="utf-8") as json_dosyasi:
        json.dump(restoranlar, json_dosyasi, ensure_ascii=False, indent=4)
        # Restoran verilerini toplamak için gerekli kodlar buraya gelecek



# Şimdi restoranlar listesini JSON dosyasına yazabilirsiniz


    browser.close()
    browser.switch_to.window(main_page)

    time.sleep(5)
            
        

          
                    
        

      
time.sleep(3)




a = input()