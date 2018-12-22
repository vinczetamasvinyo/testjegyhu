def kiemelt_ajanlat_megnezese(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                  varslaido, varindex, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindex-ét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        try:
            driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p/a[2]').click()
            time.sleep(1)
        except NoSuchElementException:
            # print('nincs cooki')
            pass
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            a = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/h4')
            # összerakjuk a görgetéshez szükséges szöveget
            pozicio_szoveg = "window.scrollTo(0," + str(a.location['y'] - 100) + ");"  # legörgetünk a TOP10-es listához
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            szoveg = a.text
            if szoveg.upper() != 'KIEMELT AJÁNLATAINK':
                teszteset_sikeres = False
                hibalista.append('A \"KIEMELT AJÁNLATAINK\" szöveg helytelenül szerepel.')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Kiemelt ajánlataink szöveg nem található')
            driver.execute_script("window.scrollTo(0,500);")
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        if varindex == 1:
            try:
                elem = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[1]/div/div[1]/a[1]/img')
                #elem = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[1]/div/div[1]/a[1]')
                ActionChains(driver).move_to_element(elem).perform()
                time.sleep(2)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                elem2 = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[1]/div/div[1]/a[2]')
                elem2.click()
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                time.sleep(2)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # print(varurl)
                # print(driver.current_url)
                if varurl == driver.current_url:
                    teszteset_sikeres = False
                    hibalista.append('Kattintás után nem navigált el a kiemelt ajánlat')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Kiemelt első ajánló nem található')
        elif varindex == 2:
            try:
                elem = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/div[1]/a[1]/img')
                ActionChains(driver).move_to_element(elem).perform()
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                elem2 = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/div[1]/a[2]')
                elem2.click()
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                time.sleep(2)
                #print(varurl)
                #print(driver.current_url)
                if varurl == driver.current_url:
                    teszteset_sikeres = False
                    hibalista.append('Kattintás után nem navigált el a kiemelt ajánlat')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Kiemelt masodik ajánló nem található')
        elif varindex == 3:
            try:
                elem = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[3]/div/div[1]/a[1]/img')
                ActionChains(driver).move_to_element(elem).perform()
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                elem2 = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[3]/div/div[1]/a[2]')
                elem2.click()
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                time.sleep(2)
                #print(varurl)
                #print(driver.current_url)
                if varurl == driver.current_url:
                    teszteset_sikeres = False
                    hibalista.append('Kattintás után nem navigált el a kiemelt ajánlat')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Kiemelt harmadik ajánló nem található')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            #print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            #print(tiszta_futasi_ido.total_seconds())
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
        kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad, hibalista


def ajanlo_megnezese(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                  varslaido, varindex, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindex-ét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            a = driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[2]/div[1]/div/div/h4')
            # összerakjuk a görgetéshez szükséges szöveget
            pozicio_szoveg = "window.scrollTo(0," + str(a.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            szoveg = a.text
            # print(szoveg)
            # print(szoveg.upper())
            if szoveg.upper() != 'AJÁNLÓ':
                teszteset_sikeres = False
                hibalista.append('Az ajánló szöveg helytelenül szerepel.')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az ajánló szöveg nem található')
            driver.execute_script("window.scrollTo(0,800);")
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        if varindex == 1:
            elemhelye = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]/img'
            gomb = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[1]/div[1]/a[2]'
        elif varindex == 2:
            elemhelye = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[2]/div[1]/a[1]/img'
            gomb = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[2]/div[1]/a[2]'
        elif varindex == 3:
            elemhelye = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[3]/div[1]/a[1]/img'
            gomb = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[3]/div[1]/a[2]'
        elif varindex == 4:
            elemhelye = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[5]/div[1]/a[1]/img'
            gomb = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[5]/div[1]/a[2]'
        elif varindex == 5:
            elemhelye = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[6]/div[1]/a[1]/img'
            gomb = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[6]/div[1]/a[2]'
        elif varindex == 6:
            elemhelye = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[7]/div[1]/a[1]/img'
            gomb = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[7]/div[1]/a[2]'
        elif varindex == 7:
            elemhelye = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[9]/div[1]/a[1]/img'
            gomb = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[9]/div[1]/a[2]'
        elif varindex == 8:
            elemhelye = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[10]/div[1]/a[1]/img'
            gomb = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[10]/div[1]/a[2]'
        elif varindex == 9:
            elemhelye = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[11]/div[1]/a[1]/img'
            gomb = '/html/body/div[1]/div[6]/div[1]/div[2]/div[2]/div[11]/div[1]/a[2]'
        try:
            elem = driver.find_element_by_xpath(elemhelye)
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            ActionChains(driver).move_to_element(elem).perform()
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            elem2 = driver.find_element_by_xpath(gomb)
            elem2.click()
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            time.sleep(2)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            #print(varurl)
            #print(driver.current_url)
            if varurl == driver.current_url:
                teszteset_sikeres = False
                hibalista.append('Kattintás után nem navigált el az ajánló programhoz')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az ajánló program nem található')
            if 0 < varindex < 4:
                driver.execute_script("window.scrollTo(0,900);")
            elif 3 < varindex < 7:
                driver.execute_script("window.scrollTo(0,1300);")
            else:
                driver.execute_script("window.scrollTo(0,1700);")
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepindex, True)
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            #print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            #print(tiszta_futasi_ido.total_seconds())
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
        kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad, hibalista


def felsokereso(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                  varslaido, varszoveg, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome5\chromedriver.exe')
        # driver.maximize_window()
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            driver.find_element_by_id('generalSearch').click()
            driver.find_element_by_id('generalSearch').send_keys(varszoveg)
            time.sleep(4)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A felső kereső nem található')
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            # driver.find_element_by_xpath('//*[@id="row_holder"]/div/div[1]/div[2]/div[1]/a').click()
            # el3 = driver.find_element_by_xpath("//*[@class='moreResult']/a")
            el3 = driver.find_elements_by_class_name('pf-suggestion')
            # el3 = driver.find_element_by_xpath('//*[@id="pf-group-3"]/ul/li[1]/div[2]/span[2]/span[1]/span')
            el3[7].click()
            time.sleep(5)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            if driver.current_url == varurl:
                teszteset_sikeres = False
                hibalista.append('Keresés után nem sikerült átnavigálni a kiválasztott oldalra.')
            #hely = driver.find_element_by_class_name('moreResult')
            # hely = driver.find_element_by_xpath('//*[@id="row_holder"]/div/div[1]/div[6]/div[2]/a')
            #hely.click()
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A keresés nem hozott eredményt')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            #print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            #print(tiszta_futasi_ido.total_seconds())
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
        kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        # log = driver.get_log('browser')
        # hibalista.append(log)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad, hibalista

def instagram(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                  varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        #driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            driver.find_element_by_id('instagramLink').click()
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[1])
            #print(driver.current_url)
            if driver.current_url != 'https://www.instagram.com/jegyhu/':
                teszteset_sikeres = False
                hibalista.append('Az instragram oldal nem jött be')
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az instagramikon nem található')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            #print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            #print(tiszta_futasi_ido.total_seconds())
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
        kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad, hibalista

def facebook(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                  varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    '''

    :param driver2:
    :param varbongeszo:
    :param varido:
    :param varurl: String.
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varkepet_keszit:
    :param kepek_path:
    :return:
    '''
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        #driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            elem = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/nav/section/ul[2]/li[1]/div[2]/span')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A facebook ikon nem jelent meg')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            #print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            #print(tiszta_futasi_ido.total_seconds())
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
        kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad, hibalista

def berletek(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                  varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        tesztvege = False
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        # print(driver.current_url)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            menu = driver.find_element_by_class_name('top-bar-section')
        except NoSuchElementException:
            teszteset_sikeres = False
            tesztvege = True
            hibalista.append('A bérleteket tartalmazó menüsor nem található')
        if tesztvege == False:
            try:
                berlet2 = menu.find_element_by_class_name('season_ticket')
            except NoSuchElementException:
                teszteset_sikeres = False
                tesztvege = True
                hibalista.append('A bérletek link nem található a menüben.')
            if tesztvege == False:
                berlet2.click()
                if driver.current_url != varurl + 'articles/461/brletek':
                    teszteset_sikeres = False
                    hibalista.append('A bérletek url-je nem jó')
                try:
                    elem = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div[1]/div/h1')
                    if elem.text != 'Bérletek':
                        teszteset_sikeres = False
                        hibalista.append('Bérletek szöveg nem egyezik a Bérletekkel')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('Bérletek szöveg nem található az oldalon')
                try:
                    link = driver.find_elements_by_xpath('.//a')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('Link nem található az oldalon')
                    tesztvege = True
                if tesztvege == False:
                    linkhossz = len(link)
                    i = -1
                    l = False
                    while (i < linkhossz) and not l:
                        i = i + 1
                        szoveg = link[i].get_attribute('href')
                        # print(type(szoveg))
                        if szoveg != None:
                            if ('seasonticket' in szoveg) and (link[i].is_displayed() == True):
                                l = True
                                # print(szoveg)
                                pozicio_szoveg = "window.scrollTo(0," + str(link[i].location['y'] - 100) + ");"
                                # legörgetünk a TOP10-es listához
                                driver.execute_script(pozicio_szoveg)
                                # time.sleep(3)
                                # print(link[i].is_displayed())
                                link[i].click()
                    if l == False:
                        teszteset_sikeres = False
                        hibalista.append('Bérlet link nem található az oldalon')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            # print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            # print(tiszta_futasi_ido.total_seconds())
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
        kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad, hibalista

def app(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                  varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/nav/section/ul[1]/li[2]/a').click()
            if driver.current_url != varurl + 'articles/457/jegyhu-mobil-alkalmazas':
                teszteset_sikeres = False
                hibalista.append('A mobilapp url-je nem jó')
            try:
                elem = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div[1]/div/h1')
                # print(elem.text)
                if elem.text != 'JEGY.HU - mobil alkalmazás':
                    teszteset_sikeres = False
                    hibalista.append('JEGY.HU - mobil alkalmazás szövege nem megfelelő')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A mobile app szövege nem található')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A mobilapp linkje nem található')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            #print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            #print(tiszta_futasi_ido.total_seconds())
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
        kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad, hibalista

def fokiemelt(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
        varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Bővebben')]")
            if len(buttons) > 0:
                i = -1
                l = False
                while (i < (len(buttons) - 1)) and (l == False):
                    i = i + 1
                    if buttons[i].is_displayed():
                        buttons[i].click()
                        l = True
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                if varurl == driver.current_url:
                    teszteset_sikeres = False
                    hibalista.append('A gomb kattintása után az oldal nem jött be')
            else:
                teszteset_sikeres =False
                hibalista.append('Gomb nem található')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Bővebben gomb nem található')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + 'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            hibalista.append('Túlléptük az SLA időt')
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                             kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad, hibalista

def nyelvvalaszto(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
              varslaido, varnyelv, varszoveg, varelem, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        # driver.maximize_window()
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        #
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            driver.find_element_by_id('main_lang_select2').click()
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                driver.find_element_by_xpath('//*[@id="main_lang_list2"]/a['+str(varnyelv)+']').click()
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                url = driver.current_url
                if varnyelv == 1:
                    keres = '?lang=en'
                elif varnyelv == 2:
                    keres ='?lang=da'
                elif varnyelv == 3:
                    keres = '?lang=hu'
                elif varnyelv == 4:
                    keres = '?lang=sk'
                elif  varnyelv == 5:
                    keres = '?lang=pl'
                elif varnyelv == 6:
                    keres = '?lang=de'
                h = len(varurl)
                # print(url[h:h+len(keres)])
                if url[h:h+len(keres)] != keres:
                    teszteset_sikeres = False
                    hibalista.append('Az url-ben nem található a nyelvválasztó. Ez hiányzik: ' + keres)
                elem = driver.find_element_by_xpath(varelem)
                pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 200) + ");"
                driver.execute_script(pozicio_szoveg)
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                # time.sleep(3)
                # print(elem.text)
                if elem.text != varszoveg:
                    teszteset_sikeres = False
                    hibalista.append('Az idegen nyelv szövege rosszul jelenik meg. Ez lett megadva: '+ varszoveg
                                     + '. Ez jelenik meg: ' + elem.text)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A megadott nyelv almenüpontja nem található')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A nyelvválasztó menü nem található')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + 'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            hibalista.append('Túlléptük az SLA időt')
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                             kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad, hibalista

def nyelvvalaszto_alul(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                      varslaido, varnyelv, varszoveg, varelem, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        import seged_cs
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        #driver.maximize_window()
        #driver.maximize_window()
        #driver.set_window_position(0,0)
        #driver.set_window_size(1300,700)
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        # driver.maximize_window()
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        seged_cs.cookiemegnyom(driver)
        try:
            seged_cs.cookiemegnyom(driver, True)
            time.sleep(2)
        except:
            print('nincs cooki')

        try:
            hely = driver.find_element_by_id('main_lang_select1')
            pozicio_szoveg = "window.scrollTo(0," + str(hely.location['y'] - 200) + ");"
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                driver.find_element_by_id('main_lang_select1').click()
            except Exception as e:
                print(e.__class__.__name__)
            try:
                driver.find_element_by_xpath('//*[@id="main_lang_list1"]/a[' + str(varnyelv) + ']').click()
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                url = driver.current_url
                if varnyelv == 1:
                    keres = '?lang=en'
                elif varnyelv == 2:
                    keres = '?lang=da'
                elif varnyelv == 3:
                    keres = '?lang=hu'
                elif varnyelv == 4:
                    keres = '?lang=sk'
                elif varnyelv == 5:
                    keres = '?lang=pl'
                elif varnyelv == 6:
                    keres = '?lang=de'
                h = len(varurl)
                print(url[h:h+len(keres)])
                if url[h:h + len(keres)] != keres:
                    teszteset_sikeres = False
                    hibalista.append('Az url-ben nem található a nyelvválasztó. Ez hiányzik: ' + keres)
                elem = driver.find_element_by_xpath(varelem)
                pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 200) + ");"
                driver.execute_script(pozicio_szoveg)
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                # time.sleep(3)
                # print(elem.text)
                if elem.text != varszoveg:
                    teszteset_sikeres = False
                    hibalista.append('Az idegen nyelv szövege rosszul jelenik meg. Ez lett megadva: ' + varszoveg
                                     + '. Ez jelenik meg: ' + elem.text)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A megadott nyelv almenüpontja nem található')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A nyelvválasztó menü nem található')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + 'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            hibalista.append('Túlléptük az SLA időt')
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                             kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
    return visszaad, hibalista

def nyelvvalaszto_alul2(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                      varslaido, varnyelv, varszoveg, varelem, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        import seged_cs
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        #driver.maximize_window()
        #driver.maximize_window()
        #driver.set_window_position(0,0)
        #driver.set_window_size(1300,700)
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        # driver.maximize_window()
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            seged_cs.cookiemegnyom(driver, True)
            time.sleep(2)
        except:
            print('nincs cooki')
        try:
            hely = driver.find_element_by_id('main_lang_select1')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A nyelvválasztó menü nem található')
        if teszteset_sikeres == True:
            pozicio_szoveg = "window.scrollTo(0," + str(hely.location['y'] - 200) + ");"
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                driver.find_element_by_id('main_lang_select1').click()
            # TODO: utána nézni hogy ez a rész hogyan működik
            except Exception as e:
                print(e.__class__.__name__)
                teszteset_sikeres = False
                hibalista.append('A nyelválasztóra való kattintás során probléma történt.')
            try:
                driver.find_element_by_xpath('//*[@id="main_lang_list1"]/a[' + str(varnyelv) + ']').click()
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A megadott nyelv almenüpontja nem található')
            if teszteset_sikeres == True:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                url = driver.current_url
                if varnyelv == 1:
                    keres = '?lang=en'
                elif varnyelv == 2:
                    keres = '?lang=da'
                elif varnyelv == 3:
                    keres = '?lang=hu'
                elif varnyelv == 4:
                    keres = '?lang=sk'
                elif varnyelv == 5:
                    keres = '?lang=pl'
                elif varnyelv == 6:
                    keres = '?lang=de'
                h = len(varurl)
                print(url[h:h+len(keres)])
                if url[h:h + len(keres)] != keres:
                    teszteset_sikeres = False
                    hibalista.append('Az url-ben nem található a nyelvválasztó. Ez hiányzik: ' + keres)
                try:
                    elem = driver.find_element_by_xpath(varelem)
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A nyelvválasztó működéséhez megadott keresési elem nem található az oldalon')
                if teszteset_sikeres == True:
                    pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 200) + ");"
                    driver.execute_script(pozicio_szoveg)
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    if elem.text != varszoveg:
                        teszteset_sikeres = False
                        hibalista.append('Az idegen nyelv szövege rosszul jelenik meg. Ez lett megadva: ' + varszoveg
                                         + '. Ez jelenik meg: ' + elem.text)
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + 'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            hibalista.append('Túlléptük az SLA időt')
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                             kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
    return visszaad, hibalista


def megnezprogramjegydb(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                          varteszteset_kepek, varslaido, varelem, varminimum, varmaximum, varkepet_keszit=True,
                        kepek_path='c:/kepek/kepek/', varcookief=True):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        varkepindex = 0
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome5\chromedriver.exe')
        # driver.maximize_window()
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        if varcookief:
            try:
                cookie = driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p/a[2]')
                cookie.click()
                time.sleep(1)
            except:
                print('nincs cooki')
        try:
            darabszam = driver.find_element_by_xpath(varelem)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Nem sikerült megtalálni a kiválasztott elemet.')
        if teszteset_sikeres:
            # print(darabszam.text)
            alap = darabszam.text
            szoveg2 = alap.replace(" ", "")
            szam = int(szoveg2)
            # print(szam)
            if not (varminimum < szam < varmaximum):
                teszteset_sikeres = False
                hibalista.append('A talált szám(' + szoveg2 + ') nem a megadott értékek(minimum:' + str(varminimum)
                                 +', maximum:' + str(varmaximum) +'), közé esik.' )
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + 'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            hibalista.append('Túlléptük az SLA időt')
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                             kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
    return visszaad, hibalista

def oldafokepvisszahoz(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                          varteszteset_kepek, varslaido, varelem, varkepet_keszit=True, kepek_path='c:/kepek/kepek/',
                                 varcookief=True):
    '''
    A jegy.hu fo oldalról elnavigál és megnézi, hogy a fő logo visszahoz-e az oldalra.

    :param driver:
    :param varbongeszo:
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varelem:
    :param varkepet_keszit:
    :param kepek_path:
    :param varcookief:
    :return:
    '''
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        varkepindex = 0
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome5\chromedriver.exe')
        # driver.maximize_window()
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        if varcookief:
            try:
                cookie = driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p/a[2]')
                cookie.click()
            except:
                print('nincs cooki')
        try:
            # link = driver.find_element_by_xpath(varelem)
            link = driver.find_element_by_id(varelem)
        except:
            teszteset_sikeres = False
            hibalista.append('A megadott link nem található. Teszteset nem folytatható.')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(link.location['y'] - 200) + ");"
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            link.click()
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            if driver.current_url == varurl:
                teszteset_sikeres = False
                hibalista.append('A megadott link nem navigált el a fő oldalró. Teszteset megszakad')
            if teszteset_sikeres:
                try:
                    jegyhulogo = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/a ')
                except:
                    teszteset_sikeres = False
                    hibalista.append(' A jegyhu logo nem található')
                if teszteset_sikeres:
                    jegyhulogo.click()
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    if driver.current_url != varurl:
                        teszteset_sikeres = False
                        hibalista.append('Visszanavigálás után nem a kezdő oldalra jutottunk. Ez volt a kezdő oldal:'
                                         + varurl + ', de ide sikerült jutni:' + driver.current_url)
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + 'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            hibalista.append('Túlléptük az SLA időt')
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                             kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
    return visszaad, hibalista


def ajanlodb(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                            varteszteset_kepek, varslaido, varmin, varmax, varkepet_keszit=True,
                                kepek_path='c:/kepek/kepek/', varcookief=True):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        varkepindex = 0
        varlinkdb = 2
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome5\chromedriver.exe')
        # driver.maximize_window()
        driver.get(varurl)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        if varcookief:
            try:
                cookie = driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p/a[2]')
                cookie.click()
                varlinkdb = 1
            except:
                print('nincs cooki')
                varlinkdb = 1
        try:
            ajanlodarab = driver.find_elements_by_class_name('mainImgContainer')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az oldalon nem található ajánló')
            pozicio_szoveg = "window.scrollTo(0," + str(800 - 100) + ");"
            driver.execute_script(pozicio_szoveg)
        if teszteset_sikeres:
            if (varmin < len(ajanlodarab) < varmax) == False:
                teszteset_sikeres = False
                hibalista.append('Az ajánlók darabszáma(' + str(len(ajanlodarab)) + ') nem a megadott értékek('
                                 + str(varmin) + ',' + str(varmax) + ') közé esik.')
            if varkepet_keszit:
                for i in range(0,len(ajanlodarab)):
                    if (i % 3) == 0:
                        pozicio_szoveg = "window.scrollTo(0," + str(ajanlodarab[i].location['y'] - 100) + ");"
                        driver.execute_script(pozicio_szoveg)
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + 'hiba', varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        tiszta_futasi_ido = tisztavege - kezdet2
        if tiszta_futasi_ido.total_seconds() > varslaido:
            teszteset_sikeres = False
            hibalista.append('Túlléptük az SLA időt')
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                             kezdet2, vege2, varido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
    return visszaad, hibalista
