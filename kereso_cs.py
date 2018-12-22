def kereso_osszes(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                  varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        # driver.implicitly_wait(6)
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
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            # driver.get_screenshot_as_file(varteszteset_kepek + '_1.png')
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Rákattintunk a keresés gombra.
        driver.find_element_by_id('searchSubmit').click()
        time.sleep(1)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            # driver.get_screenshot_as_file(varteszteset_kepek + '_2.png')
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # print(driver.current_url)
        # Megkeressük hány darabot talált a kereső
        try:
            a = driver.find_element_by_xpath('//*[@id="contentMain"]/div/div[1]/div/div/h4/span')
            # Megnézzük, hogy a találati darabszáma az 0-e. Ha igen, akkor baj van
            if int(a.text) == 0:
                teszteset_sikeres = False
                hibalista.append('0 a találati darabszám')
        except NoSuchElementException:
            hibalista.append('Lista darabszám nem található')
            teszteset_sikeres = False
        # Megkeressük a ketegória mezőt
        try:
            kategoria = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[1]/h4')
            s = kategoria.text
            if s.upper() != 'KATEGÓRIA':
                teszteset_sikeres = False
                hibalista.append('Kategória neve rossz')
            pozicio_szoveg = "window.scrollTo(0," + str(kategoria.location['y'] - 200) + ");"
            driver.execute_script(pozicio_szoveg)
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # print(kategoria.text)
        except NoSuchElementException:
            hibalista.append('Kategória mező nem található')
            teszteset_sikeres = False
        # Megkeressük a város mezőt
        try:
            varos = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[3]/h4')
            s = varos.text
            if s.upper() != 'VÁROS':
                teszteset_sikeres = False
                hibalista.append('A város szövege neve rossz')
            pozicio_szoveg = "window.scrollTo(0," + str(varos.location['y'] - 200) + ");"
            driver.execute_script(pozicio_szoveg)
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # print(varos.text)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Város szöveg nem található')
        # Megkeressük az időpont mezőt.
        try:
            idopont = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[9]/h4')
            s = idopont.text
            if s.upper() != 'IDŐPONT':
                teszteset_sikeres = False
                hibalista.append('Időpont mező szövege rossz')
            pozicio_szoveg = "window.scrollTo(0," + str(idopont.location['y'] - 200) + ");"
            driver.execute_script(pozicio_szoveg)
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # print(idopont.text)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az időpont mező nem található')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * ido
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
        kezdet2, vege2, ido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        return visszaad, hibalista


def kereso_masodik(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                   varslaido, var_index, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        from selenium.webdriver.support.select import Select
        import file_muveletek
        import seged_cs
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        hibalista = []
        varidodb = 0
        kezdet2 = datetime.datetime.now()
        # teszteset sikerességét true-ra állítjuk.
        teszteset_sikeres = True
        # Megnézzük, hogy kell-e képet készíteni a teszteset során.
        if varkepet_keszit:
            varkepsorszama = 0
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
        # maximumra állítjuk a képernyőt
        driver.maximize_window()
        # meghívjuk a kapott url-t.
        driver.get(varurl)
        if ido > 0:
            varidodb = varidodb + 1
            time.sleep(ido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        # Megkeressük a város választót, és kijelöljük az indexben megadottat.
        try:
            s2 = Select(driver.find_element_by_id('searchCity'))
            s2.select_by_index(var_index)
            varos = s2.first_selected_option.text
            #print(s2.first_selected_option.text)
           # print(s2.getAttribute('value'))
            # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                time.sleep(ido)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A város kereső nem található.')
        # Rákattintunk a mehet gombra, hogy a kereső elinduljon.
        try:
            driver.find_element_by_id('searchSubmit').click()
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A mehet gomb nem található')
        # Megkeressük a kategória szöveget, hogy elérhető-e.
        try:
            varos2 = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/h1')
            if varos != varos2.text:
                teszteset_sikeres = False
                hibalista.append('Nem a kiválasztott város neve jelenik meg az oldalon')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A kiválaszott városnév nem jelenik meg az oldalon')
        try:
            kategoria = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[1]/h4')
            s = kategoria.text
            pozicio_szoveg = "window.scrollTo(0," + str(kategoria.location['y'] - 200) + ");"
            # legörgetünk a kategóira
            driver.execute_script(pozicio_szoveg)
            if ido > 0:
                varidodb = varidodb + 1
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            time.sleep(ido)
            if s.upper() != 'KATEGÓRIA':
                teszteset_sikeres = False
                hibalista.append('Kategória neve rossz')
            # print(kategoria.text)
        except NoSuchElementException:
            hibalista.append('Kategória mező nem található')
            teszteset_sikeres = False
        # Megkeressük a Helyszín szöveget, hogy elérhető-e.
        try:
            helyszin = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[3]/h4')
            s = helyszin.text
            pozicio_szoveg = "window.scrollTo(0," + str(helyszin.location['y'] - 200) + ");"
            # legörgetünk a helyszín szöveghez
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                time.sleep(ido)
            if s.upper() != 'HELYSZÍN':
                teszteset_sikeres = False
                hibalista.append('Helyszín neve rossz')
            # print(kategoria.text)
        except NoSuchElementException:
            hibalista.append('Helyszín mező nem található')
            teszteset_sikeres = False
        # Megkeressük az időpont mezőt.
        try:
            idopont = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[6]/h4')
            s = idopont.text
            pozicio_szoveg = "window.scrollTo(0," + str(idopont.location['y'] - 200) + ");"
            # legörgetünk az időponthoz
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                #vdarabszam = vdarabszam + 1
                time.sleep(ido)
            if s.upper() != 'IDŐPONT':
                teszteset_sikeres = False
                hibalista.append('Időpont mező szövege rossz')
            # print(idopont.text)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az időpont mező nem található.')
        try:
            driver.find_element_by_xpath('//*[@id="contentMain"]/div/div[2]/div[1]/div/div/div[1]/div/a[1]/h2').click()
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                #vdarabszam = vdarabszam + 1
                time.sleep(ido)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Nincs eredmény a találati listában')
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                #vdarabszam = vdarabszam + 1
                time.sleep(ido)
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * ido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        id = tisztavege - kezdet2
        # print(id.min)
        # print(id.seconds)
        if id.total_seconds() > varslaido:
            teszteset_sikeres = False
            #print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            #print(id.total_seconds())
        #print(tisztavege - kezdet2)
        #print(id)
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad2 = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                            kezdet2,vege2,ido,id,varslaido,kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad2, hibalista

def kereso_elso(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                   varslaido, var_index, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        from selenium.webdriver.support.select import Select
        import file_muveletek
        import seged_cs
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        hibalista = []
        varidodb = 0
        kezdet2 = datetime.datetime.now()
        # teszteset sikerességét true-ra állítjuk.
        teszteset_sikeres = True
        # Megnézzük, hogy kell-e képet készíteni a teszteset során.
        if varkepet_keszit:
            varkepsorszama = 0
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
        # maximumra állítjuk a képernyőt
        driver.maximize_window()
        # meghívjuk a kapott url-t.
        driver.get(varurl)
        if ido > 0:
            varidodb = varidodb + 1
            time.sleep(ido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        # Megkeressük a típus választót, és kijelöljük az indexben megadottat.
        try:
            #s2 = Select(driver.find_element_by_id('searchProgramType'))
            s2 = Select(driver.find_element_by_id('searchProgramType_chosen'))
            s2.select_by_index(var_index)
            tipus = s2.first_selected_option.text
            #print(s2.first_selected_option.text)
           # print(s2.getAttribute('value'))
            # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                time.sleep(ido)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A típus választó nem található.')
        # Rákattintunk a mehet gombra, hogy a kereső elinduljon.
        try:
            driver.find_element_by_id('searchSubmit').click()
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A mehet gomb nem található')
        # Megkeressük a kategória szöveget, hogy elérhető-e.
        try:
            tipus2 = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/h1')
            if tipus != tipus2.text:
                teszteset_sikeres = False
                hibalista.append('Nem a kiválasztott programtípus neve jelenik meg az oldalon')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A kiválaszott programtípus nem jelenik meg az oldalon')
        try:
            kategoria = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[1]/h4')
            s = kategoria.text
            pozicio_szoveg = "window.scrollTo(0," + str(kategoria.location['y'] - 200) + ");"
            # legörgetünk a kategóira
            driver.execute_script(pozicio_szoveg)
            if ido > 0:
                varidodb = varidodb + 1
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            time.sleep(ido)
            if s.upper() != 'KATEGÓRIA':
                teszteset_sikeres = False
                hibalista.append('Kategória neve rossz')
            # print(kategoria.text)
        except NoSuchElementException:
            hibalista.append('Kategória mező nem található')
            teszteset_sikeres = False
        try:
            varos = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[3]/h4')
            s = varos.text
            pozicio_szoveg = "window.scrollTo(0," + str(varos.location['y'] - 200) + ");"
            # legörgetünk a helyszín szöveghez
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                time.sleep(ido)
            if s.upper() != 'VÁROS':
                teszteset_sikeres = False
                hibalista.append('Helyszín neve rossz')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A város szűrő nem található')
        # Megkeressük a Helyszín szöveget, hogy elérhető-e.
        try:
            helyszin = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[6]/h4')
            s = helyszin.text
            pozicio_szoveg = "window.scrollTo(0," + str(helyszin.location['y'] - 200) + ");"
            # legörgetünk a helyszín szöveghez
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                time.sleep(ido)
            if s.upper() != 'HELYSZÍN':
                teszteset_sikeres = False
                hibalista.append('Helyszín neve rossz')
            # print(kategoria.text)
        except NoSuchElementException:
            hibalista.append('Helyszín mező nem található')
            teszteset_sikeres = False
        # Megkeressük az időpont mezőt.
        try:
            idopont = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[9]/h4')
            s = idopont.text
            pozicio_szoveg = "window.scrollTo(0," + str(idopont.location['y'] - 200) + ");"
            # legörgetünk az időponthoz
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                #vdarabszam = vdarabszam + 1
                time.sleep(ido)
            if s.upper() != 'IDŐPONT':
                teszteset_sikeres = False
                hibalista.append('Időpont mező szövege rossz')
            # print(idopont.text)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az időpont mező nem található.')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * ido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        id = tisztavege - kezdet2
        # print(id.min)
        # print(id.seconds)
        if id.total_seconds() > varslaido:
            #print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            teszteset_sikeres = False
            #print(id.total_seconds())
        #print(tisztavege - kezdet2)
        #print(id)
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad2 = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                            kezdet2,vege2,ido,id,varslaido,kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad2, hibalista

def kereso_harmadik(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                   varslaido, var_index, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        from selenium.webdriver.support.select import Select
        import file_muveletek
        import seged_cs
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        hibalista = []
        varidodb = 0
        kezdet2 = datetime.datetime.now()
        # teszteset sikerességét true-ra állítjuk.
        teszteset_sikeres = True
        # Megnézzük, hogy kell-e képet készíteni a teszteset során.
        if varkepet_keszit:
            varkepsorszama = 0
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
        # maximumra állítjuk a képernyőt
        driver.maximize_window()
        # meghívjuk a kapott url-t.
        driver.get(varurl)
        if ido > 0:
            varidodb = varidodb + 1
            time.sleep(ido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        # Megkeressük a város választót, és kijelöljük az indexben megadottat.
        try:
            s2 = Select(driver.find_element_by_id('searchVenue'))
            s2.select_by_index(var_index)
            eloado = s2.first_selected_option.text
            #print(s2.first_selected_option.text)
           # print(s2.getAttribute('value'))
            # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                time.sleep(ido)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A előadóhely kereső nem található.')
        # Rákattintunk a mehet gombra, hogy a kereső elinduljon.
        try:
            driver.find_element_by_id('searchSubmit').click()
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A mehet gomb nem található')
        # Megkeressük a kategória szöveget, hogy elérhető-e.
        try:
            eloado2 = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/h1')
            if eloado != eloado2.text:
                teszteset_sikeres = False
                hibalista.append('Nem a kiválasztott eloado neve jelenik meg az oldalon')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A kiválaszott előadóhely neve nem jelenik meg az oldalon')
        try:
            kategoria = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[3]/h4')
            s = kategoria.text
            pozicio_szoveg = "window.scrollTo(0," + str(kategoria.location['y'] - 200) + ");"
            # legörgetünk a kategóira
            driver.execute_script(pozicio_szoveg)
            if ido > 0:
                varidodb = varidodb + 1
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            time.sleep(ido)
            if s.upper() != 'KATEGÓRIA':
                teszteset_sikeres = False
                hibalista.append('Kategória neve rossz')
            # print(kategoria.text)
        except NoSuchElementException:
            hibalista.append('Kategória mező nem található')
            teszteset_sikeres = False
        # Megkeressük a Helyszín szöveget, hogy elérhető-e.
        try:
            helyszin = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[1]/h4')
            s = helyszin.text
            pozicio_szoveg = "window.scrollTo(0," + str(helyszin.location['y'] - 200) + ");"
            # legörgetünk a helyszín szöveghez
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                time.sleep(ido)
            if s.upper() != 'HELYSZÍN':
                teszteset_sikeres = False
                hibalista.append('Helyszín neve rossz')
            # print(kategoria.text)
        except NoSuchElementException:
            hibalista.append('Helyszín mező nem található')
            teszteset_sikeres = False
        # Megkeressük az időpont mezőt.
        try:
            idopont = driver.find_element_by_xpath('//*[@id="contentLeft"]/div/div[5]/h4')
            s = idopont.text
            pozicio_szoveg = "window.scrollTo(0," + str(idopont.location['y'] - 200) + ");"
            # legörgetünk az időponthoz
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                #vdarabszam = vdarabszam + 1
                time.sleep(ido)
            if s.upper() != 'IDŐPONT':
                teszteset_sikeres = False
                hibalista.append('Időpont mező szövege rossz')
            # print(idopont.text)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az időpont mező nem található.')
        try:
            driver.find_element_by_xpath('//*[@id="contentMain"]/div/div[2]/div[1]/div/div/div[1]/div/a[1]/h2').click()
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                #vdarabszam = vdarabszam + 1
                time.sleep(ido)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Nincs eredmény a találati listában')
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if ido > 0:
                varidodb = varidodb + 1
                #vdarabszam = vdarabszam + 1
                time.sleep(ido)
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * ido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        id = tisztavege - kezdet2
        # print(id.min)
        # print(id.seconds)
        if id.total_seconds() > varslaido:
            teszteset_sikeres = False
            #print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            #print(id.total_seconds())
        #print(tisztavege - kezdet2)
        #print(id)
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        # visszaad2 = seged_cs.lista_osszerak(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
        #                                    kezdet2, vege2,
        #                                    ido, kepek_helye)
        visszaad2 = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                            kezdet2,vege2,ido,id,varslaido,kepek_helye)

        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad2, hibalista

def ujosszes(driver, varbongeszo, ido, varurl, varteszteset_neve,varteszteset_leiras,varteszteset_kepek,
              varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    global kepek_helye, seged_cs, teszteset_sikeres, kezdet2, varidodb, datetime
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        from selenium.webdriver.support.select import Select
        import file_muveletek
        import seged_cs
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        hibalista = []
        varidodb = 0
        kezdet2 = datetime.datetime.now()
        # teszteset sikerességét true-ra állítjuk.
        teszteset_sikeres = True
        # Megnézzük, hogy kell-e képet készíteni a teszteset során.
        if varkepet_keszit:
            varkepsorszama = 0
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
        driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome4\chromedriver.exe')
        # maximumra állítjuk a képernyőt
        driver.maximize_window()
        # meghívjuk a kapott url-t.
        driver.get(varurl)
        if ido > 0:
            varidodb = varidodb + 1
            time.sleep(ido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        try:
            gomb = driver.find_element_by_id('searchSubmit')
            pozicio_szoveg = "window.scrollTo(0," + str(gomb.location['y'] - 200) + ");"
            # legörgetünk az időponthoz
            driver.execute_script(pozicio_szoveg)
            gomb.click()
            if driver.current_url !=  varurl + 'ticketsearch':
                teszteset_sikeres = False
                hibalista.append('A kereső URL-je nem stímmel. Ez jelenik meg: '+ driver.current_url
                                 + '. De ennek kellene megjelennie: ' + varurl + 'ticketsearch')
            try:
                szoveg = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[1]/div/h1')
                if szoveg.text != 'Eseménykereső':
                    teszteset_sikeres = False
                    hibalista.append('Eseménykereső szövege nem megfelelő. Ez jelenik meg: ' + szoveg.text
                                     + ', de az Eseménykereső szövegnek kellene megjelennie.')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Az eseménykerső szöveg nem található.')
            try:
                esemenyszam = driver.find_element_by_xpath('//*[@id="contentMain"]/div/div[1]/div/div/h4/span')
                pozicio_szoveg = "window.scrollTo(0," + str(esemenyszam.location['y'] - 200) + ");"
                # legörgetünk az időponthoz
                driver.execute_script(pozicio_szoveg)
                if varkepet_keszit:
                    varkepsorszama = varkepsorszama + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Események száma nem található')
            try:
                '''
                Ez is működik ha szükséges.
                valami5 = driver.find_elements_by_xpath("//*[@class='button moreIcon buyTicketButton']")
                '''
                buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Jegyvásárlás')]")
                pozicio_szoveg = "window.scrollTo(0," + str(buttons[0].location['y'] - 200) + ");"
                # legörgetünk az időponthoz
                driver.execute_script(pozicio_szoveg)
                if varkepet_keszit:
                    varkepsorszama = varkepsorszama + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
                print(len(buttons))
                buttons[0].click()
                if driver.current_url == varurl + 'ticketsearch':
                    teszteset_sikeres = False
                    hibalista.append('Jegyvásárlás gomb megnyomása után az url nem jó.')
                if varkepet_keszit:
                    varkepsorszama = varkepsorszama + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A jegyvásárlás gomb nem található')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A kereső gomb nem található')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * ido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        id = tisztavege - kezdet2
        # print(id.min)
        # print(id.seconds)
        if id.total_seconds() > varslaido:
            # print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            teszteset_sikeres = False
            # print(id.total_seconds())
        # print(tisztavege - kezdet2)
        # print(id)
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad2 = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                              kezdet2, vege2, ido, id, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad2, hibalista

def ujelsokereso(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                 varslaido, var_index, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    global kepek_helye, seged_cs, teszteset_sikeres, kezdet2, varidodb, datetime, hibalista, varkepsorszama
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        from selenium.webdriver.support.select import Select
        import file_muveletek
        import seged_cs
        from selenium.common.exceptions import NoSuchElementException
        from selenium.webdriver import ActionChains
        print(varteszteset_neve + ' elindult')
        hibalista = []
        varidodb = 0
        kezdet2 = datetime.datetime.now()
        # teszteset sikerességét true-ra állítjuk.
        teszteset_sikeres = True
        # Megnézzük, hogy kell-e képet készíteni a teszteset során.
        if varkepet_keszit:
            varkepsorszama = 0
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
        # maximumra állítjuk a képernyőt
        driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome4\chromedriver.exe')
        driver.maximize_window()
        # meghívjuk a kapott url-t.
        driver.get(varurl)
        if ido > 0:
            varidodb = varidodb + 1
            time.sleep(ido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        elem = driver.find_element_by_id('searchCity_chosen')
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(elem).perform()
        actions.click(elem).perform()
        resz = driver.find_element_by_xpath('//*[@id="searchCity_chosen"]/div/ul/li[3]')
        resz.click()
        time.sleep(3)

    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * ido
        tisztavege = vege2 - datetime.timedelta(seconds=masodperc)
        id = tisztavege - kezdet2
        # print(id.min)
        # print(id.seconds)
        if id.total_seconds() > varslaido:
            # print('túlléptük az időt')
            hibalista.append('Túlléptük az SLA időt')
            teszteset_sikeres = False
            # print(id.total_seconds())
        # print(tisztavege - kezdet2)
        # print(id)
        if teszteset_sikeres:
            eredmeny = 'Sikeres'
        else:
            eredmeny = 'Sikertelen'
        visszaad2 = seged_cs.lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, eredmeny, varbongeszo,
                                              kezdet2, vege2, ido, id, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad2, hibalista