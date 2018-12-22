def toltippnez(vardriver, vartoolid, varkellekep, varkepekneve, varkepindex, vartimestamp):
    from selenium.webdriver import ActionChains
    from selenium.common.exceptions import NoSuchElementException
    import time
    import seged_cs
    hlista = []
    teset = True
    try:
        tooltipid = vardriver.find_element_by_xpath(vartoolid)
        # print(tooltipid.location)
        pozicio_szoveg = "window.scrollTo(0," + str(tooltipid.location['y'] - 160) + ");"
        vardriver.execute_script(pozicio_szoveg)
        if varkellekep:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(vardriver, varkepekneve, varkepindex, vartimestamp)
    except NoSuchElementException:
        if varkellekep:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(vardriver, varkepekneve + 'hiba', varkepindex, vartimestamp)
        teset = False
        hlista.append('Nem található a megadott tooltipp')
    if teset:
        ActionChains(vardriver).click_and_hold(tooltipid).perform()
        time.sleep(2)
        if varkellekep:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(vardriver, varkepekneve, varkepindex, vartimestamp)
        time.sleep(1)
        ujid = tooltipid.get_attribute('aria-describedby')
        # print(ujid)
        try:
            valami = vardriver.find_element_by_id(ujid)
            # print(valami.text)
        except:
            teszteset_sikeres = False
            hlista.append('A tooltipphez tartozó 2. kódrész nem található')
    return teset, hlista, valami.text, varkepindex


def tooltipp_regisztracio(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                          varteszteset_kepek,
                          varslaido, vartooltippid, vartooltippszoveg, varkepet_keszit=True,
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
                seged_cs.cookiemegnyom(driver,True)
            except:
                print('nincs cooki')
        try:
            driver.find_element_by_link_text('Bejelentkezés').click()
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az oldalon a Bejelentkezés link nem található, így a teszt hamarább megszakadt')
        if teszteset_sikeres:
            try:
                driver.find_element_by_link_text('Regisztráció').click()
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A regisztrációs link nem található az oldalon')
            if teszteset_sikeres:
                teszteset_sikeres, hiblista, tszoveg, varkepindex = toltippnez(driver, vartooltippid, varkepet_keszit,
                                                                               varteszteset_kepek, varkepindex, True)
                if len(hiblista) > 0:
                    hibalista = hibalista + hiblista
                '''
                try:
                    tooltipid = driver.find_element_by_xpath(vartooltippid)
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('Nem található a megadott tooltipp')
                if teszteset_sikeres == True:
                    # ujid = tooltipid.get_attribute('aria-describedby')
                    ActionChains(driver).click_and_hold(tooltipid).perform()
                    time.sleep(1)
                    ujid = tooltipid.get_attribute('aria-describedby')
                    try:
                        valami = driver.find_element_by_id(ujid)
                        print(valami.text)
                    except:
                        teszteset_sikeres = False
                        hibalista.append('A tooltipphez tartozó 2. kódrész nem található')
                '''
                if teszteset_sikeres:
                    if tszoveg != vartooltippszoveg:
                        teszteset_sikeres = False
                        hibalista.append('A tooltipp szövege nem egyezik a megadott. Ennek kellett volna:"'
                                         + vartooltippszoveg + '", de ez jelent meg:"' + tszoveg + '".')
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


def tooltipp2(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
              varslaido, vartooltippid, vartooltippszoveg, varkepet_keszit=True,
              kepek_path='c:/kepek/kepek/', varcookie=True):
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
        hiblista = []
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
        time.sleep(3)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        if varcookie:
            try:
                cookie = driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p/a[2]')
                cookie.click()
            except:
                print('nincs cooki')
        if teszteset_sikeres:
            teszteset_sikeres, hiblista, tszoveg, varkepindex = toltippnez(driver, vartooltippid, varkepet_keszit,
                                                                           varteszteset_kepek, varkepindex, True)
            if len(hiblista) > 0:
                hibalista = hibalista + hiblista

            '''                
            try:
                tooltipid = driver.find_element_by_xpath(vartooltippid)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Nem található a megadott tooltipp')
            if teszteset_sikeres == True:
                ActionChains(driver).click_and_hold(tooltipid).perform()
                time.sleep(1)
                ujid = tooltipid.get_attribute('aria-describedby')
                print(ujid)
                try:
                    valami = driver.find_element_by_id(ujid)
                    print(valami.text)
                except:
                    teszteset_sikeres = False
                    hibalista.append('A tooltipphez tartozó 2. kódrész nem található')
            '''
            if teszteset_sikeres:
                if tszoveg != vartooltippszoveg:
                    teszteset_sikeres = False
                    hibalista.append('A tooltipp szövege nem egyezik a megadott. Ennek kellett volna:"'
                                     + vartooltippszoveg + '", de ez jelent meg:"' + tszoveg + '".')
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


def tooltipp_ujjelszo(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                      varslaido, vartooltippid, vartooltippszoveg, varkepet_keszit=True,
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
            driver.find_element_by_link_text('Bejelentkezés').click()
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az oldalon a Bejelentkezés link nem található, így a teszt hamarább megszakadt.')
        if teszteset_sikeres:
            try:
                driver.find_element_by_link_text('Új jelszó megadása').click()
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append(
                    'Az "új jelszó megadása" link nem található az oldalon, így a teszt hamarább megszakadt.')
            if teszteset_sikeres:
                teszteset_sikeres, hiblista, tszoveg, varkepindex = toltippnez(driver, vartooltippid, varkepet_keszit,
                                                                               varteszteset_kepek, varkepindex, True)
                if len(hiblista) > 0:
                    hibalista = hibalista + hiblista
                if teszteset_sikeres:
                    if tszoveg != vartooltippszoveg:
                        teszteset_sikeres = False
                        hibalista.append('A tooltipp szövege nem egyezik a megadott. Ennek kellett volna:"'
                                         + vartooltippszoveg + '", de ez jelent meg:"' + tszoveg + '".')
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


def tooltipp_hirlevel(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                      varslaido, vartooltippid, vartooltippszoveg, varkepet_keszit=True,
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
            except:
                print('nincs cooki')
        try:
            driver.find_element_by_id('newsletterLink').click()
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Oldalon a hírlevél ikon nem található')
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek + 'hiba', varkepindex, True)
        if teszteset_sikeres:
            teszteset_sikeres, hiblista, tszoveg, varkepindex = toltippnez(driver, vartooltippid, varkepet_keszit,
                                                                           varteszteset_kepek, varkepindex, True)
            if len(hiblista) > 0:
                hibalista = hibalista + hiblista
            if teszteset_sikeres:
                if tszoveg != vartooltippszoveg:
                    teszteset_sikeres = False
                    hibalista.append('A tooltipp szövege nem egyezik a megadott. Ennek kellett volna:"'
                                     + vartooltippszoveg + '", de ez jelent meg:"' + tszoveg + '".')
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