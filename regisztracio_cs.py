def regisztracio_rovid_jelszo(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                              varteszteset_kepek,
                              varslaido, varemail, varjelszo, varhibaszoveg, varkepet_keszit=True,
                              kepek_path='c:/kepek/kepek/'):
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
        hibalista = []
        varkepindex = 0
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        # visszaad = []
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
            elm = driver.find_elements_by_link_text("Bejelentkezés")
            elm[0].click()
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                elm = driver.find_elements_by_link_text('Regisztráció')
                elm[0].click()
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                if driver.current_url != varurl + 'user/register':
                    teszteset_sikeres = False
                    hibalista.append('A regisztráció URL-je nem jó. Ami megjelent: ' + driver.current_url)
                szoveg = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/h1')
                if szoveg.text != 'Regisztráció':
                    teszteset_sikeres = False
                    hibalista.append('A regisztráció szöveg nem jelent meg. Helyette ez látható: ' + szoveg.text)
                driver.find_element_by_id('email').send_keys(varemail)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # A jelszó mezőbe beírjuk a jelszo változó tartalmát.
                driver.find_element_by_id('password1').send_keys(varjelszo)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                driver.find_element_by_id('submitReg').click()
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                try:
                    szoveg2 = driver.find_element_by_class_name('validation_errors').text
                    if szoveg2 != varhibaszoveg:
                        teszteset_sikeres = False
                        hibalista.append('A rövid jelszó miatt megjelenő hibaszöveg nem jó. Ez jelent meg: ' + szoveg2)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A hibaszöveg nem jelent meg')
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A regisztrációs link nem található')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Bejelentkezés link nem található')
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

def regisztracio_rovid_jelszo2(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                              varteszteset_kepek,
                              varslaido, varemail, varjelszo, varhibaszoveg, varkepet_keszit=True,
                              kepek_path='c:/kepek/kepek/'):
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
        varkepindex = 0
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        # visszaad = []
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
        seged_cs.cookiemegnyom(driver, True)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            elm = driver.find_elements_by_link_text("Bejelentkezés")
            elm[0].click()
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                elm = driver.find_element_by_link_text('Regisztráció')
                pozicio_szoveg = "window.scrollTo(0," + str(elm.location['y'] - 100) + ");"
                driver.execute_script(pozicio_szoveg)
                elm.click()
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                if driver.current_url != varurl + 'user/register':
                    teszteset_sikeres = False
                    hibalista.append('A regisztráció URL-je nem jó. Ami megjelent: ' + driver.current_url)
                szoveg = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/h1')
                if szoveg.text != 'Regisztráció':
                    teszteset_sikeres = False
                    hibalista.append('A regisztráció szöveg nem jelent meg. Helyette ez látható: ' + szoveg.text)
                driver.find_element_by_id('email').send_keys(varemail)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # A jelszó mezőbe beírjuk a jelszo változó tartalmát.
                driver.find_element_by_id('password1').send_keys(varjelszo)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                try:
                    checkbox = driver.find_element_by_id('accept_terms')
                    ActionChains(driver).move_to_element(checkbox).click().perform()
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A regisztrációhoz szükséges checkbox nem jelent meg')
                driver.find_element_by_id('submitReg').click()
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                try:
                    szoveg2 = driver.find_element_by_class_name('validation_errors').text
                    if szoveg2 != varhibaszoveg:
                        teszteset_sikeres = False
                        hibalista.append('A rövid jelszó miatt megjelenő hibaszöveg nem jó. Ez jelent meg: ' + szoveg2)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A hibaszöveg nem jelent meg')
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A regisztrációs link nem található')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Bejelentkezés link nem található')
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

def regisztracio_rovid_jelszo3(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                              varteszteset_kepek,
                              varslaido, varemail, varjelszo, varhibaszoveg, varkepet_keszit=True,
                              kepek_path='c:/kepek/kepek/'):
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
        varkepindex = 0
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        # visszaad = []
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
        seged_cs.cookiemegnyom(driver, True)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            elm = driver.find_elements_by_link_text("Bejelentkezés")
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Bejelentkezés link nem található')
        if teszteset_sikeres == True:
            elm[0].click()
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                elm = driver.find_element_by_link_text('Regisztráció')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A regisztrációs link nem található')
            if teszteset_sikeres== True:
                pozicio_szoveg = "window.scrollTo(0," + str(elm.location['y'] - 100) + ");"
                driver.execute_script(pozicio_szoveg)
                elm.click()
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                if driver.current_url != varurl + 'user/register':
                    teszteset_sikeres = False
                    hibalista.append('A regisztráció URL-je nem jó. Ami megjelent: ' + driver.current_url)
                try:
                    szoveg = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/h1')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A regsiztráció szöveg nem jelent meg')
                if szoveg.text != 'Regisztráció':
                    teszteset_sikeres = False
                    hibalista.append('A regisztráció szöveg nem jelent meg. Helyette ez látható: ' + szoveg.text)
                driver.find_element_by_id('email').send_keys(varemail)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # A jelszó mezőbe beírjuk a jelszo változó tartalmát.
                driver.find_element_by_id('password1').send_keys(varjelszo)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                try:
                    checkbox = driver.find_element_by_id('accept_terms')
                    ActionChains(driver).move_to_element(checkbox).click().perform()
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A regisztrációhoz szükséges checkbox nem jelent meg')
                driver.find_element_by_id('submitReg').click()
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                try:
                    szoveg2 = driver.find_element_by_class_name('validation_errors').text
                    if szoveg2 != varhibaszoveg:
                        teszteset_sikeres = False
                        hibalista.append('A rövid jelszó miatt megjelenő hibaszöveg nem jó. Ez jelent meg: ' + szoveg2)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A hibaszöveg nem jelent meg')
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
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

def regisztracio_rosszjelszo(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                             varteszteset_kepek,
                             varslaido, varemail, varjelszo, varhibaszoveg1, varhibaszoveg2, varkepet_keszit=True,
                             kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        import difflib
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        # visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        varkepindex = 0
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
            elm = driver.find_elements_by_link_text("Bejelentkezés")
            elm[0].click()
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                elm = driver.find_elements_by_link_text('Regisztráció')
                elm[0].click()
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                if driver.current_url != varurl + 'user/register':
                    teszteset_sikeres = False
                    hibalista.append('A regisztráció URL-je nem jó. Ami megjelent: ' + driver.current_url)
                szoveg = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/h1')
                if szoveg.text != 'Regisztráció':
                    teszteset_sikeres = False
                    hibalista.append('A regisztráció szöveg nem jelent meg. Helyette ez látható: ' + szoveg.text)
                driver.find_element_by_id('email').send_keys(varemail)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # A jelszó mezőbe beírjuk a jelszo változó tartalmát.
                driver.find_element_by_id('password1').send_keys(varjelszo)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                driver.find_element_by_id('submitReg').click()
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                if driver.current_url != varurl + 'registration/doRegistration':
                    teszteset_sikeres = False
                    hibalista.append('A hibaoldal url-je nem jó. Ez jelent meg: ' + driver.current_url)
                try:
                    szoveg2 = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/h1')
                    if szoveg2.text != varhibaszoveg1:
                        teszteset_sikeres = False
                        hibalista.append('Az egyik hibaszöveg nem megfelelő. Helyette ez jelent meg: ' + szoveg2.text)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A hibaszöveg1 nem jelent meg')
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                try:
                    szoveg3 = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/p')
                    if szoveg3.text != varhibaszoveg2:
                        # output_list = [li for li in list(difflib.ndiff(szoveg3.text, varhibaszoveg2)) if li[0] != ' ']
                        # print(output_list)
                        teszteset_sikeres = False
                        hibalista.append('Az egyik hibaszöveg nem megfelelő. Helyette ez jelent meg: ' + szoveg3.text)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                except:
                    teszteset_sikeres = False
                    hibalista.append('A hibaszöveg2 nem jelent meg')
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                try:
                    gomb = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/a')
                    # print(gomb.text)
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A vissza a regisztrációhoz gomb nem jelent meg')
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)

            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A regisztrációs link nem található')

        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Bejelentkezés link nem található')
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

def regisztracio_rosszjelszo2(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                             varteszteset_kepek,
                             varslaido, varemail, varjelszo, varhibaszoveg1, varhibaszoveg2, varkepet_keszit=True,
                             kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        import difflib
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        # visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        varkepindex = 0
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        seged_cs.cookiemegnyom(driver, True)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            elm = driver.find_element_by_link_text("Bejelentkezés")
            pozicio_szoveg = "window.scrollTo(0," + str(elm.location['y'] - 200) + ");"
            driver.execute_script(pozicio_szoveg)
            elm.click()
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                elm = driver.find_elements_by_link_text('Regisztráció')
                elm[0].click()
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                if driver.current_url != varurl + 'user/register':
                    teszteset_sikeres = False
                    hibalista.append('A regisztráció URL-je nem jó. Ami megjelent: ' + driver.current_url)
                szoveg = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/h1')
                if szoveg.text != 'Regisztráció':
                    teszteset_sikeres = False
                    hibalista.append('A regisztráció szöveg nem jelent meg. Helyette ez látható: ' + szoveg.text)
                driver.find_element_by_id('email').send_keys(varemail)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # A jelszó mezőbe beírjuk a jelszo változó tartalmát.
                driver.find_element_by_id('password1').send_keys(varjelszo)
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                try:
                    checkbox = driver.find_element_by_id('accept_terms')
                    ActionChains(driver).move_to_element(checkbox).click().perform()
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A regisztrációhoz szükséges checkbox nem jelent meg')
                driver.find_element_by_id('submitReg').click()
                if varido > 0:
                    varidodb = varidodb + 1
                    time.sleep(varido)
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                if driver.current_url != varurl + 'registration/doRegistration':
                    teszteset_sikeres = False
                    hibalista.append('A hibaoldal url-je nem jó. Ez jelent meg: ' + driver.current_url)
                try:
                    szoveg2 = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/h1')
                    if szoveg2.text != varhibaszoveg1:
                        teszteset_sikeres = False
                        hibalista.append('Az egyik hibaszöveg nem megfelelő. Helyette ez jelent meg: ' + szoveg2.text)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A hibaszöveg1 nem jelent meg')
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                try:
                    szoveg3 = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/p')
                    if szoveg3.text != varhibaszoveg2:
                        # print(szoveg3.text)
                        output_list = [li for li in list(difflib.ndiff(szoveg3.text, varhibaszoveg2)) if li[0] != ' ']
                        # print(output_list)
                        teszteset_sikeres = False
                        hibalista.append('Az egyik hibaszöveg nem megfelelő. Helyette ez jelent meg: ' +
                                         szoveg3.text + ', de ennek kellett volna megjelennie: '+ varhibaszoveg2 +
                                         '. Különbség:')
                        hibalista.extend(output_list)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                except:
                    teszteset_sikeres = False
                    hibalista.append('A hibaszöveg2 nem jelent meg')
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                try:
                    gomb = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/a')
                    # print(gomb.text)
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A vissza a regisztrációhoz gomb nem jelent meg')
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)

            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A regisztrációs link nem található')

        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Bejelentkezés link nem található')
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


def regisztracio_tooltip(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                         varteszteset_kepek, varslaido, vartooltip1, vartooltip2,
                         varkepet_keszit=True,
                         kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        import difflib
        from selenium.common.exceptions import NoSuchElementException
        from selenium.webdriver import ActionChains
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        # visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        varkepindex = 0
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        #driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
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
            elm = driver.find_element_by_link_text("Bejelentkezés")
        except NoSuchElementException:
            hibalista.append('A bejelentkezés link nem található')
            teszteset_sikeres = False
        finally:
            # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        if teszteset_sikeres != False:
            elm.click()
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                regisztracio = driver.find_element_by_link_text('Regisztráció')
                regisztracio.click()
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A regisztrációs link nem található')
                # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            if teszteset_sikeres != False:
                try:
                    tooltipp1 = driver.find_element_by_xpath('//*[@id="registration"]/div/div/fieldset/div/div/div/div[1]/div/div/div[2]/span')
                    # ActionChains(driver).move_to_element(tooltipp1).perform()
                    ActionChains(driver).click_and_hold(tooltipp1).perform()
                    szoveg = driver.fin
                    #ActionChains.click_and_hold(tooltipp1).perform()
                    # time.sleep(2)
                    print(tooltipp1.get_attribute('title'))


                    print(tooltipp1.text)
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('Az email cím melletti tooltip nem található')


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


def regisztraciogombinaktiv(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                            varteszteset_kepek, varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/',
                            varcookief=True):
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
                seged_cs.cookiemegnyom(driver, True)
            except:
                print('nincs cooki')
        try:
            bejelentkezes = driver.find_element_by_link_text('Bejelentkezés')
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Teszteset megszakadt, mert a bejelentkezés link nem található')
        if teszteset_sikeres:
            bejelentkezes.click()
            try:
                regisztracio = driver.find_element_by_link_text('Regisztráció')
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Teszteset megszakadt, mert a Regisztrációs link nem található az oldalon.')
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek + 'hiba', varkepindex, True)
            if teszteset_sikeres:
                regisztracio.click()
                try:
                    reggomb = driver.find_element_by_id('submitReg')
                    hibaszoveg = ''
                except NoSuchElementException:
                    hibaszoveg = 'hiba'
                    teszteset_sikeres = False
                    hibalista.append('a regisztrációs gomb nem található')
                finally:
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek + hibaszoveg, varkepindex, True)
                if teszteset_sikeres:
                    if reggomb.is_enabled():
                        teszteset_sikeres = False
                        hibalista.append('A regisztrációs gomb aktív, pedig inaktívnak kellene lennie.')
                        if varkepet_keszit:
                            hibaszoveg = 'hiba'
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek + hibaszoveg, varkepindex, True)

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


def regisztraciogcheckboxszoveg(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                            varteszteset_kepek, varslaido, varcheckszoveg, varkepet_keszit=True,
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
                seged_cs.cookiemegnyom(driver, True)
            except:
                print('nincs cooki')
        try:
            bejelentkezes = driver.find_element_by_link_text('Bejelentkezés')
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Teszteset megszakadt, mert a bejelentkezés link nem található')
        if teszteset_sikeres:
            bejelentkezes.click()
            try:
                regisztracio = driver.find_element_by_link_text('Regisztráció')
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Teszteset megszakadt, mert a Regisztrációs link nem található az oldalon.')
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek + 'hiba', varkepindex, True)
            if teszteset_sikeres:
                regisztracio.click()
                try:
                    szoveg = driver.find_element_by_class_name('checkbox-custom-label')
                    hibaszoveg = ''
                except NoSuchElementException:
                    hibaszoveg = 'hiba'
                    teszteset_sikeres = False
                    hibalista.append('A checkboxhoz tartozó szöveg nem található')
                finally:
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek + hibaszoveg, varkepindex, True)
                if teszteset_sikeres:
                    if szoveg.text != varcheckszoveg:
                        teszteset_sikeres = False
                        szov= 'A checkbox szövege nem megfelelő. Ez jelen meg: "' + szoveg.text + '", ' \
                              'de ennek kellett volna megjelennie:"' + varcheckszoveg + '".'
                        hibalista.append(szov)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepindex, True)
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


def regisztraciolinkszoveg(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                            varteszteset_kepek, varslaido, varlinkszoveg, varlinkurl, varkepet_keszit=True,
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
                seged_cs.cookiemegnyom(driver,True)
                varlinkdb = 1
            except:
                print('nincs cooki')
                varlinkdb = 1
        try:
            bejelentkezes = driver.find_element_by_link_text('Bejelentkezés')
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Teszteset megszakadt, mert a bejelentkezés link nem található')
        if teszteset_sikeres:
            bejelentkezes.click()
            try:
                regisztracio = driver.find_element_by_link_text('Regisztráció')
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Teszteset megszakadt, mert a Regisztrációs link nem található az oldalon.')
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek + 'hiba', varkepindex, True)
            if teszteset_sikeres:
                regisztracio.click()
                try:
                    szoveg = driver.find_element_by_class_name('checkbox-custom-label')
                    hibaszoveg = ''
                except NoSuchElementException:
                    hibaszoveg = 'hiba'
                    teszteset_sikeres = False
                    hibalista.append('A checkboxhoz tartozó szöveg nem található')
                finally:
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek + hibaszoveg, varkepindex, True)
                if teszteset_sikeres:
                    szoveg2 = szoveg.text
                    if varlinkszoveg not in szoveg.text:
                        # print(varlinkszoveg)
                        # print(szoveg.text)
                        teszteset_sikeres = False
                        hibalista.append('A chekcbox szövege nem tartalmazza a megadott szöveget')
                    if teszteset_sikeres:
                        try:
                            link = driver.find_elements_by_link_text(varlinkszoveg)
                        except NoSuchElementException:
                            teszteset_sikeres = False
                            hibalista.append('A megadott link szövege(' + varlinkszoveg + '), nem található')
                        finally:
                            if varkepet_keszit:
                                varkepindex = varkepindex + 1
                                seged_cs.kepet_keszit(driver, varteszteset_kepek + hibaszoveg, varkepindex, True)
                        if teszteset_sikeres:
                            if varlinkdb != len(link):
                                teszteset_sikeres = False
                                hibalista.append('A linkek száma nem egyezik. Ellenőrizni kell az esetet.')
                            link[0].click()
                            if varkepet_keszit:
                                varkepindex = varkepindex + 1
                                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                            if driver.current_url != varlinkurl:
                                teszteset_sikeres = False
                                hibalista.append('A link nem a megadott(' + varlinkurl + ') url-re vezetett, '
                                                'mert ez jelent meg:' + driver.current_url)
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