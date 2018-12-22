def aszf(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                      varslaido, varurllista, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
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
        aszfresz = '/html/body/div[1]/footer[2]/div/div[1]/ul/li[1]/a'
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
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome4\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        seged_cs.cookiemegnyom(driver)
        '''
        try:
            driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p/a[2]').click()
            time.sleep(1)
        except NoSuchElementException:
            # print('nincs cooki')
            pass
        '''
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük az ÁSZF szöveget
        # elem = driver.find_element_by_xpath(aszfresz)
        try:
            elem = driver.find_element_by_partial_link_text('Általános Szerződési Feltételek')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az általános szerződési feltételek szöveg/link nem található')
        # Összerakjuk a görgetéshez a szöveget
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 200) + ");"
            # Legörgetünk az ÁSZF részhez
            driver.execute_script(pozicio_szoveg)
            # Beállítjuk a segéd változókat a ciklushoz
            k = -1
            meddig = 2
            # Elindítjuk a ciklust
            while k != meddig - 1:
                k = k + 1
                # újból megkeressük az ASZF részt
                # elem = driver.find_element_by_xpath(aszfresz)
                elem = driver.find_element_by_partial_link_text('Általános Szerződési Feltételek')
                # Rákattintunk az ÁSZF linkre
                elem.click()
                time.sleep(2)
                # Megnézzük, hogy kell-e képet csinálni
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                #  Legyűjtjük a linkeket.
                lista = driver.find_elements_by_partial_link_text('Megnyitás')
                meddig = len(lista)
                lista[k].click()
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                # Ha az url nem egyezik, akkor hibás a teszteset.
                if driver.current_url != varurllista[k]:
                    teszteset_sikeres = False
                    hibalista.append('Az ÁSZF URL-je nem jó. Ez jelent meg: ' + driver.current_url \
                                     +', de ennek kellett volna:' + varurllista[k])
                # Visszalépünk az oldalon.
                driver.back()
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
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
        else:
            driver.close()
        print(varteszteset_neve + ' lefutott')
    return visszaad, hibalista


def oldallinkmegnez(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                      varslaido, vartipus, varhely, varszoveg, varerurl, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    '''
    Oldalon megnézi az aktuális linket, hogy működik-e.

    Az adott oldalon megnézi az adott linket, hogy megtalálható-e. Ellenőrzi a szöveget, és megnézi hogyha a linkre kattintunk akkor jó URL jelenik-e meg. Az függvénnyel lehet keresni id, szöveg és Xpath alapján.

    :param driver2: (driver). Az elindított böngésző drive-re
    :param varbongeszo:
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param vartipus:
    :param varhely:
    :param varszoveg:
    :param varerurl:
    :param varkepet_keszit:
    :param kepek_path:
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
        # driver.maximize_window()
        driver.get(varurl)
        seged_cs.cookiemegnyom(driver)
        '''
        try:
            driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p/a[2]').click()
            time.sleep(1)
        except NoSuchElementException:
            pass
            # print('nincs cooki')
        '''
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            if vartipus == 1:
                hely = driver.find_element_by_id(varhely)
            elif vartipus == 2:
                # print(varhely)
                # hely = driver.find_elements_by_link_text(varhely)
                hely = driver.find_element_by_partial_link_text(varhely)
                # print(hely.location)
            elif vartipus == 3:
                hely = driver.find_element_by_xpath(varhely)
            pozicio_szoveg = "window.scrollTo(0," + str(hely.location['y'] - 200) + ");"
            driver.execute_script(pozicio_szoveg)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            if hely.text != varszoveg:
                teszteset_sikeres = False
                hibalista.append('Az elem szövege nem egyezik')
            hely.click()
            # time.sleep(4)
            time.sleep(3)
            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[1])
                print('több ablak van')
                if driver.current_url != varerurl:
                    teszteset_sikeres = False
                    hibalista.append('Az oldal url-je nem stímmel. Ennek kellett volna megjelennie: '
                                     + varerurl + ', de ez jelent meg:' + driver.current_url)
            else:
                if driver.current_url != varerurl:
                    print('Egy ablak van')
                    teszteset_sikeres = False
                    hibalista.append('Az oldal url-je nem stímmel. Ennek kellett volna megjelennie: '
                                     + varerurl + ', de ez jelent meg:' + driver.current_url)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A keresett elem nem található')
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
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
        else:
            driver.close()
        print(varteszteset_neve + ' lefutott')
    return visszaad, hibalista

def tobboldallinkes(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                      varslaido, varurllista, varkeres, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
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
        aszfresz = '/html/body/div[1]/footer[2]/div/div[1]/ul/li[1]/a'
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
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome4\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        seged_cs.cookiemegnyom(driver)
        '''
        try:
            driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p/a[2]').click()
            time.sleep(1)
        except NoSuchElementException:
            # print('nincs cooki')
            pass
        '''
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük az ÁSZF szöveget
        # elem = driver.find_element_by_xpath(aszfresz)
        try:
            elem = driver.find_element_by_partial_link_text(varkeres)
        except NoSuchElementException:
            teszteset_sikeres = False
            # hibalista.append('Az általános szerződési feltételek szöveg/link nem található')
            hibalista.append('A megadott szöveg amire kattintani kell az nem található.')
        # Összerakjuk a görgetéshez a szöveget
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 200) + ");"
            # Legörgetünk az ÁSZF részhez
            driver.execute_script(pozicio_szoveg)
            # Beállítjuk a segéd változókat a ciklushoz
            k = -1
            meddig = 2
            # Elindítjuk a ciklust
            while k != meddig - 1:
                k = k + 1
                # újból megkeressük az ASZF részt
                # elem = driver.find_element_by_xpath(aszfresz)
                elem = driver.find_element_by_partial_link_text(varkeres)
                # Rákattintunk azadatkezelési linkre
                elem.click()
                time.sleep(2)
                # Megnézzük, hogy kell-e képet csinálni
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                #  Legyűjtjük a linkeket.
                lista = driver.find_elements_by_partial_link_text('Megnyitás')
                meddig = len(lista)
                lista[k].click()
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                # Ha az url nem egyezik, akkor hibás a teszteset.
                if driver.current_url != varurllista[k]:
                    teszteset_sikeres = False
                    hibalista.append('Az ÁSZF URL-je nem jó. Ez jelent meg: ' + driver.current_url \
                                     +', de ennek kellett volna:' + varurllista[k])
                # Visszalépünk az oldalon.
                driver.back()
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
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
        else:
            driver.close()
        print(varteszteset_neve + ' lefutott')
    return visszaad, hibalista

'''
u0 = 'https://www.jegy.hu/articles/625/az-interticket-kft-altalanos-szerzodesi-feltetelei'
u1 = 'https://www.jegy.hu/articles/625/az-interticket-kft-altalanos-szerzodesi-feltetelei/3'
u2 = 'https://www.jegy.hu/articles/625/az-interticket-kft-altalanos-szerzodesi-feltetelei/2'
u3 = 'https://www.jegy.hu/articles/625/az-interticket-kft-altalanos-szerzodesi-feltetelei/1'
lista = [u0, u1, u2, u3]
print(aszf(driver=chrome,varbongeszo='chrome',varido=0,varurl='https://www.jegy.hu/',varteszteset_neve='t1', varteszteset_leiras='t2',
           varteszteset_kepek='t3', varslaido=30, varurllista=lista))
'''
'''
teszt1 = 'Kapcsolat'
teszt2 = 'Teszt során azt nézzük, hogy a Kapcsolat link jól működik-e'
oldal = 'https://www.jegy.hu/'
u = 'https://www.jegy.hu/articles/557/kapcsolat'
oldallinkmegnez(driver='chrome', varbongeszo='chrome', varido=0, varurl=oldal, varteszteset_neve=teszt1,
                              varteszteset_leiras=teszt2, varteszteset_kepek='kapcsolat', varslaido=20, vartipus=2,
                              varhely='Kapcsolat', varszoveg='Kapcsolat', varerurl=u)

import bongeszo
chrome = bongeszo.chrome_inditasa()
# firefox = bongeszo.firefox_inditasa()
teszt1 = 'Kiemelt ajánlat 1'
teszt2 = 'Teszt során azt nézzük, hogy a kiemelt ajánló 1 megjelenik-e az oldalon.'
kornyezet='https://www.jegy.hu'
u0 = 'https://www.jegy.hu/articles/655/adatkezelesi-tajekoztato'
u1 = 'https://www.jegy.hu/articles/655/adatkezelesi-tajekoztato/1'
lista = [u0, u1]
print(tobboldallinkes(driver=chrome,varbongeszo='chrome',varido=0,varurl='https://www.jegy.hu/',varteszteset_neve='t1',
        varteszteset_leiras='t2',varkeres='Adatkezelési tájékoztató',
           varteszteset_kepek='t3', varslaido=30, varurllista=lista))
'''