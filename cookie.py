def cookie_megnez(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                      varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    '''
    Megnézi, hogy a cookie megjelenik-e az oldal megnyitása során.

    A függvény megnézi, hogy az oldalon megjelenik-e a cookie banner. Ha megjelenik, akkor sikeres volt a teszt.

    :param webdriver driver: valami
    :param driver: Az inicializált böngésző.
    :type driver: webdriver

    Args:
        driver: [webdriver] Az inicializált böngésző.
        varbongeszo (string): Az átadott böngésző neve. Chrome, Firefox, IE11
        varido (int): Az egyes helyeken mennyit kell várakoznia.
        varurl: []
    Types:
        diver
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
        from selenium.webdriver.common.keys import Keys
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
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome4\chromedriver.exe')
        # driver.maximize_window()
        driver.get(varurl)
        time.sleep(6)
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            driver.find_element_by_xpath('//*[@id="cookieWrapper"]')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A cookie banner nem található')
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

def cookie_mukodese (driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                      varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    'Ellenőrzi a cookei működését. Cookie elfogadása után még egyszer nem jelenthet meg a cookie.'
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.webdriver.common.keys import Keys
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
        teszteset_vege = True
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome4\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        time.sleep(2)
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            driver.find_element_by_xpath('//*[@id="cookieWrapper"]')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A cookie banner nem található')
            teszteset_vege = False
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        if teszteset_vege != False:
            try:
                cookie = driver.find_element_by_css_selector('a.button.accept_cookie')
                cookie.click()
                '''
                a = driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p/a[2]')
                a.click()
                '''
                time.sleep(2)
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            except NoSuchElementException:
                teszteset_vege = False
                teszteset_sikeres = False
                hibalista.append('A cookie elfogadásához szükséges gomb nem található')
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            if teszteset_vege != False:
                nincs = driver.find_element_by_xpath('//*[@id="cookieWrapper"]')
                if nincs.is_displayed() == True:
                    teszteset_sikeres = False
                    hibalista.append('A cookie továbbra is megjelenik az elfogadás után.')
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                driver.execute_script("window.open('https://www.jegy.hu');")
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                try:
                    cookie2 = driver.find_element_by_xpath('//*[@id="cookieWrapper"]')
                    if cookie2.is_displayed() == True:
                        teszteset_sikeres = False
                        hibalista.append('A cookie továbbra is megjelenik.')
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                except NoSuchElementException:
                    pass
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



def cookie_szovege(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                      varslaido, varcookieszovege, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    '''
    Megnézi, hogy a cookie szövege jó-e.

    :param webdriver driver: Az inicializált böngésző.
    :param varbongeszo:
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varcookieszovege:
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
        from selenium.webdriver.common.keys import Keys
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
        teszteset_vege = True
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindexét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome4\chromedriver.exe')
        driver.maximize_window()
        driver.get(varurl)
        time.sleep(2)
        #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        #driver.execute_script("window.open('https://www.google.com');")
        try:
            driver.find_element_by_xpath('//*[@id="cookieWrapper"]')
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A cookie banner nem található')
            teszteset_vege = False
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        if teszteset_vege != False:
            try:
                cookie_szoveg = driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p')
                print(cookie_szoveg.text)

                if cookie_szoveg.text != varcookieszovege:
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    teszteset_sikeres = False
                    hibalista.append('A cookie szövege nem egyezik a megadottal. Ennek \"' + varcookieszovege + \
                                     '\" kellett volan megjelennie, de ez \"'+ cookie_szoveg.text + '\" jelent meg.')
            except NoSuchElementException:
                teszteset_vege = False
                teszteset_sikeres = False
                hibalista.append('A cookie elfogadásához szükséges gomb nem található')
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


def cookiebanlink(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                      varslaido, varcookilink, varcookieurl, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    '''
    Megnézi, hogy a cookiben az adatvédelmi link megjelenik-e.

    Megnézi, hogy a cookiban az adatvédelmire vezető link megjelenik-e.
    :param driver:
    :param varbongeszo:
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varcookilink: path elérési út a cookiban lévő adatvédelmi linknek.
    :param varcookieurl: az adatvédelmi link url-je. Ennek kell megjelennie, ha rákattintunk a linkre.
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
        from selenium.webdriver.common.keys import Keys
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
        time.sleep(2)
        try:
            driver.find_element_by_xpath('//*[@id="cookieWrapper"]')
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A cookie banner nem található')
            teszteset_vege = False
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        if teszteset_sikeres:
            try:
                cookielink = driver.find_element_by_xpath(varcookilink)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A cookie-ban lévő link nem található.')
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            if teszteset_sikeres:
                cookielink.click()
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                if driver.current_url != varcookieurl:
                    teszteset_sikeres = False
                    hibalista.append('A cookie-ban lévő linkre kattintva nem a megadott(' + varcookieurl + ') jelent '
                                    'meg hanem ez:' + driver.current_url)
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
