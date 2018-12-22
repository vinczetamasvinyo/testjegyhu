def ajandekutalvany(driver1, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras,
                    varteszteset_kepek, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    """

    :param driver1:
    :param varbongeszo:
    :param ido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varkepet_keszit:
    :param kepek_path:
    :return:
    """
    from selenium import webdriver
    from selenium.webdriver.support.select import Select
    import time
    from selenium.common.exceptions import NoSuchElementException
    try:
        driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        driver.get(varurl)
        driver.maximize_window()
        varhibalista = []
        teszteset_sikeres = True
        try:
            elso_tipus = driver.find_element_by_id('gift_card_type')
            pozicio_szoveg = "window.scrollTo(0," + str(elso_tipus.location['y'] - 200) + ");"
            driver.execute_script(pozicio_szoveg)
            s1 = Select(driver.find_element_by_id('gift_card_type'))
            print(len(s1.options))
            for lista in range(len(s1.options)):
                print(s1.options[lista].text)
            s1.select_by_index(2)
            valami = s1.first_selected_option.text
            print(valami)
            time.sleep(4)
            driver.find_element_by_class_name('gift_card_increment').click()
            time.sleep(3)
        except NoSuchElementException:
            teszteset_sikeres = False
            varhibalista.append('Utalvány típusa nem található')
        masodik_tipus = driver.find_element_by_xpath('//*[@id="amount-normal"]/select')
        s1 = Select(driver.find_element_by_xpath('//*[@id="amount-normal"]/select'))
        s1.select_by_index(2)
        time.sleep(3)
        varhibalista.append('Utalvány pénzértéke nem választható')
    except:
        pass
    finally:
        return varhibalista


def ajandekutalvanyszoveg1(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                           varteszteset_kepek,
                           varslaido, varlista, varkepet_keszit=True, kepek_path='c:/kepek/kepek/', varcookief=True):
    """
    Megnézi, hogy az ajándékutalványban az előírt választható opciók vannak-e.

    :param driver:
    :param varbongeszo:
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varlista: Ez az a lista amivel a megjelenítendő elemek összehasonlításra kerülnek.
    :param varkepet_keszit:
    :param kepek_path:
    :return:
    """
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.webdriver.support.select import Select
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
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
        if varcookief:
            try:
                seged_cs.cookiemegnyom(driver,True)
            except:
                print('nincs cooki')
        try:
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            elem.click()
            try:
                lista = driver.find_element_by_id('gift_card_type')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Az ajándékkártya típusa nem található')
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            if teszteset_sikeres:
                s = Select(lista)
                # print(len(s.options))
                if len(s.options) == len(varlista):
                    # print(s.options[0].text)
                    for i in range(0, len(varlista)):
                        if s.options[i].text != varlista[i]:
                            teszteset_sikeres = False
                            hibalista.append('A ' + str(i) + ' szövege nem egyezik. Ez jelent meg:' + s.options[
                                i].text + ', de ennek kellett volna megjelennie:' + varlista[i])
                else:
                    teszteset_sikeres = False
                    hibalista.append('Az ajándékkártya típusában nem az előírt ' + str(len(varlista)) +
                                     ' típus van, mert ' + str(len(s.options)) + ' db van.')
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


def ajandekutalvanyszoveg2(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                           varteszteset_kepek,
                           varslaido, varindex1, varlista, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.webdriver.support.select import Select
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        lista = []
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
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            elem.click()
            try:
                lista = driver.find_element_by_id('gift_card_type')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Az ajándékkártya típusa nem található')
            if teszteset_sikeres:
                s = Select(lista)
                # print(len(s.options))
                s.select_by_index(varindex1)
                if varindex1 == 1:
                    hely = '//*[@id="amount-normal"]/select'
                elif varindex1 == 2:
                    hely = '//*[@id="amount-birthday"]/select'
                else:
                    hely = '//*[@id="amount-nameday"]/select'
                s2 = Select(driver.find_element_by_xpath(hely))
                # print(len(s2.options))
                if len(s2.options) == len(varlista):
                    for i in range(0, len(varlista)):
                        if s2.options[i].text != varlista[i]:
                            teszteset_sikeres = False
                            hibalista.append('A ' + str(i) + ' szövege nem egyezik. Ez jelent meg:' + s2.options[
                                i].text + ', de ennek kellett volna megjelennie:' + varlista[i])
                else:
                    teszteset_sikeres = False
                    hibalista.append('A 2.típusban lévő választható mennyiség nem eggyezik a megadottal')
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


def ajandekutalvanyszoveg3(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                           varteszteset_kepek,
                           varslaido, varindex1, varlista, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.webdriver.support.select import Select
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        lista = []
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
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            elem.click()
            try:
                lista = driver.find_element_by_id('gift_card_type')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Az ajándékkártya típusa nem található')
            if teszteset_sikeres:
                s = Select(lista)
                # print(len(s.options))
                s.select_by_visible_text(varindex1)
                # s.select_by_index(varindex1)
                if varindex1 == "Jegy.hu ajándékutalvány":
                    hely = '//*[@id="amount-normal"]/select'
                elif varindex1 == "Boldog születésnapot!":
                    hely = '//*[@id="amount-birthday"]/select'
                else:
                    hely = '//*[@id="amount-nameday"]/select'
                s2 = Select(driver.find_element_by_xpath(hely))
                # print(len(s2.options))
                if len(s2.options) == len(varlista):
                    for i in range(0, len(varlista)):
                        if s2.options[i].text != varlista[i]:
                            teszteset_sikeres = False
                            hibalista.append('A ' + str(i) + ' szövege nem egyezik. Ez jelent meg:' + s2.options[
                                i].text + ', de ennek kellett volna megjelennie:' + varlista[i])
                else:
                    teszteset_sikeres = False
                    hibalista.append('A 2.típusban lévő választható mennyiség nem eggyezik a megadottal')
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

def ajandekutalvanykeprol(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                           varteszteset_kepek, varslaido, varkepkattint, varlista, varkepet_keszit=True,
                          kepek_path='c:/kepek/kepek/'):
    '''
    Ajándékutalvány oldalon képeről indulva indítja el a vásárlást és megnéz, hogy a listbox jól állítódik-e.

    :param driver:
    :param varbongeszo:
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varkepkattint: Melyik képre kell kattintani
    :param varlista:
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
        from selenium.webdriver.support.select import Select
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
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            elem.click()

            if varkepkattint == 1:
                kattinthely = '//*[@id="thumb-normal"]/a'
                elvartszoveg = 'Jegy.hu ajándékutalvány'
                kattinthely2 = 'amount-normal'
                kattintselect = '//*[@id="amount-normal"]/select'
                try:
                    kep = driver.find_element_by_xpath('//*[@id="thumb-normal"]/a/img')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('Az ajándékutalvány kép nem található az oldalon')
            elif varkepkattint == 2:
                kattinthely ='//*[@id="thumb-birthday"]/a'
                elvartszoveg = 'Boldog születésnapot!'
                kattinthely2 = 'amount-birthday'
                kattintselect = '//*[@id="amount-birthday"]/select'
                try:
                    kep = driver.find_element_by_xpath('//*[@id="thumb-birthday"]/a/img')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A Boldog születésnapot kép nem található')
            elif varkepkattint == 3:
                kattinthely = '//*[@id="thumb-nameday"]/a'
                elvartszoveg = 'Boldog névnapot!'
                kattinthely2 = 'amount-nameday'
                kattintselect = '//*[@id="amount-nameday"]/select'
                try:
                    kep = driver.find_element_by_xpath('//*[@id="thumb-nameday"]/a/img')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A boldog névnapot kép nem található az oldalon')
            else:
                teszteset_sikeres = False
                hibalista.append('A kattintashoz szükséges képindex rosszl lett megadva. Ez az érték nem megfelelő:' +
                                 str(varkepkattint))
            if teszteset_sikeres:
                try:
                    ikon = driver.find_element_by_xpath(kattinthely)
                    pozicio_szoveg = "window.scrollTo(0," + str(kep.location['y'] - 100) + ");"
                    driver.execute_script(pozicio_szoveg)
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A megadott ikon nem található az oldalon')
                if teszteset_sikeres:
                    pozicio_szoveg = "window.scrollTo(0," + str(ikon.location['y'] - 100) + ");"
                    driver.execute_script(pozicio_szoveg)
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    ikon.click()
                    try:
                        aj_tipus = driver.find_element_by_id('gift_card_type')
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    except NoSuchElementException:
                        teszteset_sikeres = False
                        hibalista.append('Az ajándékkártya típusválasztó nem található')
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    if teszteset_sikeres:
                        pozicio_szoveg = "window.scrollTo(0," + str(aj_tipus.location['y'] - 100) + ");"
                        driver.execute_script(pozicio_szoveg)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                        aj_tilus_lista = Select(aj_tipus)
                        kijelolt = aj_tilus_lista.first_selected_option
                        # print(kijelolt.text)
                        # print(elvartszoveg)
                        if kijelolt.text != elvartszoveg:
                            teszteset_sikeres = False
                            hibalista.append('Ajándékkártya típusa nem megfelelő')
                    if teszteset_sikeres:
                        li = Select(driver.find_element_by_xpath(kattintselect))
                        masodikvalaszto = driver.find_element_by_id(kattinthely2)
                        ActionChains(driver).move_to_element(masodikvalaszto).click().perform()
                        time.sleep(3)
                        # ActionChains(driver).move_to_element(masodikvalaszto).click_and_hold().perform()
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                        # masodikvalaszto.click()
                        time.sleep(1)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                        print(len(li.options))
                        for i in range(0,len(li.options)):
                            # print(li.options[i].text)
                            if li.options[i].text != varlista[i]:
                                teszteset_sikeres = False
                                hibalista.append('A ' + str(i) + ' szövege nem egyezik. Ez jelent meg:' + li.options[
                                    i].text + ', de ennek kellett volna megjelennie:' + varlista[i])
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


def ajandekutalvanykeprol2(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                           varteszteset_kepek, varslaido, varkepkattint, varlista, varkepet_keszit=True,
                           kepek_path='c:/kepek/kepek/'):
    '''
    Ajándékutalvány oldalon képeről indulva indítja el a vásárlást és megnéz, hogy a listbox jól állítódik-e.

    :param driver:
    :param varbongeszo:
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varkepkattint: Melyik képre kell kattintani
    :param varlista:
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
        from selenium.webdriver.support.select import Select
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
        seged_cs.cookiemegnyom(driver, True)
        if varido > 0:
            varidodb = varidodb + 1
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            elem.click()
            osszeskep = driver.find_elements_by_class_name('mTSThumb')
            mennikell = True
            i = 0
            while (mennikell == True) and (i< len(osszeskep)):
                if osszeskep[i].get_attribute('alt') == varkepkattint:
                    mennikell = False
                else:
                    i = i+1
            if mennikell == True:
                teszteset_sikeres = False
                hibalista.append('A megadott kép nem található')
            if teszteset_sikeres:
                kellkattintani = (i+1)-3
                if kellkattintani > 0:
                    jobbragomb = driver.find_element_by_id('mTS_1_buttonRight')
                    pozicio_szoveg = "window.scrollTo(0," + str(jobbragomb.location['y'] - 200) + ");"
                    driver.execute_script(pozicio_szoveg)
                    time.sleep(1)
                    for kattint in range(0, kellkattintani):
                        jobbragomb.click()
                        time.sleep(1)
                if varkepkattint == 'Jegy.hu ajándékutalvány':
                    kattinthely = '//*[@id="thumb-normal"]/a'
                    elvartszoveg = 'Jegy.hu ajándékutalvány'
                    kattinthely2 = 'amount-normal'
                    kattintselect = '//*[@id="amount-normal"]/select'
                    try:
                        kep = driver.find_element_by_xpath('//*[@id="thumb-normal"]/a/img')
                    except NoSuchElementException:
                        teszteset_sikeres = False
                        hibalista.append('Az ajándékutalvány kép nem található az oldalon')
                elif varkepkattint == 'Boldog születésnapot!':
                    kattinthely = '//*[@id="thumb-birthday"]/a'
                    elvartszoveg = 'Boldog születésnapot!'
                    kattinthely2 = 'amount-birthday'
                    kattintselect = '//*[@id="amount-birthday"]/select'
                    try:
                        kep = driver.find_element_by_xpath('//*[@id="thumb-birthday"]/a/img')
                    except NoSuchElementException:
                        teszteset_sikeres = False
                        hibalista.append('A Boldog születésnapot kép nem található')
                elif varkepkattint == 'Boldog névnapot!':
                    kattinthely = '//*[@id="thumb-nameday"]/a'
                    elvartszoveg = 'Boldog névnapot!'
                    kattinthely2 = 'amount-nameday'
                    kattintselect = '//*[@id="amount-nameday"]/select'
                    try:
                        kep = driver.find_element_by_xpath('//*[@id="thumb-nameday"]/a/img')
                    except NoSuchElementException:
                        teszteset_sikeres = False
                        hibalista.append('A boldog névnapot kép nem található az oldalon')
                else:
                    teszteset_sikeres = False
                    hibalista.append('A kattintashoz szükséges képindex rosszl lett megadva. Ez az érték nem megfelelő:' +
                                     str(varkepkattint))
                if teszteset_sikeres:
                    try:
                        ikon = driver.find_element_by_xpath(kattinthely)
                        pozicio_szoveg = "window.scrollTo(0," + str(kep.location['y'] - 100) + ");"
                        driver.execute_script(pozicio_szoveg)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    except NoSuchElementException:
                        teszteset_sikeres = False
                        hibalista.append('A megadott ikon nem található az oldalon')
                    if teszteset_sikeres:
                        pozicio_szoveg = "window.scrollTo(0," + str(ikon.location['y'] - 100) + ");"
                        driver.execute_script(pozicio_szoveg)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                        ikon.click()
                        time.sleep(3)
                        try:
                            aj_tipus = driver.find_element_by_id('gift_card_type')
                            if varkepet_keszit:
                                varkepindex = varkepindex + 1
                                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                        except NoSuchElementException:
                            teszteset_sikeres = False
                            hibalista.append('Az ajándékkártya típusválasztó nem található')
                            if varkepet_keszit:
                                varkepindex = varkepindex + 1
                                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                        if teszteset_sikeres:
                            pozicio_szoveg = "window.scrollTo(0," + str(aj_tipus.location['y'] - 100) + ");"
                            driver.execute_script(pozicio_szoveg)
                            if varkepet_keszit:
                                varkepindex = varkepindex + 1
                                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                            aj_tilus_lista = Select(aj_tipus)
                            kijelolt = aj_tilus_lista.first_selected_option
                            # print(kijelolt.text)
                            # print(elvartszoveg)
                            if kijelolt.text != elvartszoveg:
                                teszteset_sikeres = False
                                hibalista.append('Ajándékkártya típusa nem megfelelő')
                        if teszteset_sikeres:
                            li = Select(driver.find_element_by_xpath(kattintselect))
                            masodikvalaszto = driver.find_element_by_id(kattinthely2)
                            ActionChains(driver).move_to_element(masodikvalaszto).click().perform()
                            time.sleep(2)
                            # ActionChains(driver).move_to_element(masodikvalaszto).click_and_hold().perform()
                            if varkepet_keszit:
                                varkepindex = varkepindex + 1
                                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                            # masodikvalaszto.click()
                            time.sleep(1)
                            if varkepet_keszit:
                                varkepindex = varkepindex + 1
                                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                            print(len(li.options))
                            for i in range(0, len(li.options)):
                                # print(li.options[i].text)
                                if li.options[i].text != varlista[i]:
                                    teszteset_sikeres = False
                                    hibalista.append('A ' + str(i) + ' szövege nem egyezik. Ez jelent meg:' + li.options[
                                        i].text + ', de ennek kellett volna megjelennie:' + varlista[i])
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

def ajandekutalvanymegrendel(driver2, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                             varteszteset_kepek, varslaido, varindex1, varindex2, varajegynovel, varajegycsokkent,
                             varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.webdriver.support.select import Select
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
        driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome5\chromedriver.exe')
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
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
            print(elem.location['y'])
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            elem.click()
            try:
                lista = driver.find_element_by_id('gift_card_type')
                pozicio_szoveg = "window.scrollTo(0," + str(lista.location['y'] - 100) + ");"
                driver.execute_script(pozicio_szoveg)
                s = Select(lista)
                print(len(s.options))
                s.select_by_index(varindex1)
                elsoszoveg = s.first_selected_option.text
                # print(elsoszoveg)
                if varindex1 == 1:
                    hely = '//*[@id="amount-normal"]/select'
                elif varindex1 == 2:
                    hely = '//*[@id="amount-birthday"]/select'
                else:
                    hely = '//*[@id="amount-nameday"]/select'
                s2 = Select(driver.find_element_by_xpath(hely))
                s2.select_by_index(varindex2)
                masodikszoveg = s2.first_selected_option.text
                gombnovel = driver.find_element_by_class_name('gift_card_increment')
                gombcsokkent = driver.find_element_by_class_name('gift_card_decrement')
                for elad in range(1, varajegynovel):
                    gombnovel.click()
                    if varido > 0:
                        varidodb = varidodb + 1
                        time.sleep(varido)
                for elad in range(0, varajegycsokkent):
                    gombcsokkent.click()
                    if varido > 0:
                        varidodb = varidodb + 1
                        time.sleep(varido)
                driver.find_element_by_id('gift_cards_to_basket').click()
                time.sleep(2)
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                szoveg = driver.find_element_by_xpath('//*[@id="basket-succeed"]/div/div')
                print(szoveg.text)
                teljesszoveg = '''Sikeres kosárba rakás\nÖn a következő ajándékutalványokat helyezte a kosárba:\n'''
                print(teljesszoveg)
                teljesszoveg = teljesszoveg + elsoszoveg + ' - ' + masodikszoveg + ' - ' + str(
                    varajegynovel - varajegycsokkent) + ' db\n×'
                print(teljesszoveg)
                if szoveg.text != teljesszoveg:
                    teszteset_sikeres = False
                    hibalista.append('Sikeres eladás után a megjelenő szöveg nem megfelelő.')
                    # print('sikeres a szöveg')
                print(len(s2.options))

            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Az ajándékkártya típusa nem található')

        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
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

def ajandekutalvanymegrendel2(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                             varteszteset_kepek, varslaido, varindex1, varindex2, varajegynovel, varajegycsokkent,
                             varkepet_keszit=True, kepek_path='c:/kepek/kepek/', varcookief=True):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.webdriver.support.select import Select
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        #driver.implicitly_wait(10)
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
        if varcookief:
            try:
                cookie = driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p/a[2]')
                cookie.click()
            except:
                print('nincs cooki')
        try:
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            elem.click()
            try:
                lista = driver.find_element_by_id('gift_card_type')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Az ajándékkártya típusa nem található')
            if teszteset_sikeres:
                pozicio_szoveg = "window.scrollTo(0," + str(lista.location['y'] - 100) + ");"
                driver.execute_script(pozicio_szoveg)
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                s = Select(lista)
                # print(len(s.options))
                try:
                    s.select_by_index(varindex1)
                except:
                    teszteset_sikeres = False
                    hibalista.append('Az ajándékutalvány típusának a kiválasztása nem sikerült')
                if teszteset_sikeres:
                    elsoszoveg = s.first_selected_option.text
                    # print(elsoszoveg)
                    if varindex1 == 1:
                        hely = '//*[@id="amount-normal"]/select'
                    elif varindex1 == 2:
                        hely = '//*[@id="amount-birthday"]/select'
                    else:
                        hely = '//*[@id="amount-nameday"]/select'
                    s2 = Select(driver.find_element_by_xpath(hely))
                    s2.select_by_index(varindex2)
                    masodikszoveg = s2.first_selected_option.text
                    gombnovel = driver.find_element_by_class_name('gift_card_increment')
                    gombcsokkent = driver.find_element_by_class_name('gift_card_decrement')
                    for elad in range(1, varajegynovel):
                        gombnovel.click()
                        if varido > 0:
                            varidodb = varidodb + 1
                            time.sleep(varido)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    for elad in range(0, varajegycsokkent):
                        gombcsokkent.click()
                        if varido > 0:
                            varidodb = varidodb + 1
                            time.sleep(varido)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    driver.find_element_by_id('gift_cards_to_basket').click()
                    time.sleep(7)
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    szoveg = driver.find_element_by_xpath('//*[@id="basket-succeed"]/div/div')
                    # print(szoveg.text)
                    teljesszoveg = '''Sikeres kosárba rakás\nÖn a következő ajándékutalványokat helyezte a kosárba:\n'''
                    # print(teljesszoveg)
                    teljesszoveg = teljesszoveg + elsoszoveg + ' - ' + masodikszoveg + ' - ' + str(
                        varajegynovel - varajegycsokkent) + ' db\n×'
                    # print(teljesszoveg)
                    if szoveg.text != teljesszoveg:
                        teszteset_sikeres = False
                        hibalista.append('Sikeres eladás után a megjelenő szöveg nem megfelelő.')
                        # print('sikeres a szöveg')
                    # print(len(s2.options))
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

def ajandekutalvanymegrendel3(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                             varteszteset_kepek, varslaido, varindex1, varindex2, varajegynovel, varajegycsokkent,
                             varkepet_keszit=True, kepek_path='c:/kepek/kepek/', varcookief=True):
    try:
        from selenium import webdriver
        import time
        from selenium.webdriver import ActionChains
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.webdriver.support.select import Select
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        #driver.implicitly_wait(10)
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
        if varcookief:
            try:
                seged_cs.cookiemegnyom(driver=driver,megnyom=True)
            except:
                print('nincs cooki')
        try:
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            elem.click()
            try:
                lista = driver.find_element_by_id('gift_card_type')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Az ajándékkártya típusa nem található')
            if teszteset_sikeres:
                pozicio_szoveg = "window.scrollTo(0," + str(lista.location['y'] - 100) + ");"
                driver.execute_script(pozicio_szoveg)
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                s = Select(lista)
                # print(len(s.options))
                try:
                    #s.select_by_index(varindex1)
                    # print(s.options[4].text)
                    #s.select_by_value(varindex1)
                    s.select_by_visible_text(varindex1)
                except:
                    teszteset_sikeres = False
                    hibalista.append('Az ajándékutalvány típusának a kiválasztása nem sikerült')
                if teszteset_sikeres:
                    elsoszoveg = s.first_selected_option.text
                    # print(elsoszoveg)
                    if varindex1 == "Jegy.hu ajándékutalvány":
                        hely = '//*[@id="amount-normal"]/select'
                    elif varindex1 == "Boldog születésnapot!":
                        hely = '//*[@id="amount-birthday"]/select'
                    elif varindex1 == "Boldog névnapot!":
                        hely = '//*[@id="amount-nameday"]/select'
                    s2 = Select(driver.find_element_by_xpath(hely))
                    s2.select_by_index(varindex2)
                    masodikszoveg = s2.first_selected_option.text
                    gombnovel = driver.find_element_by_class_name('gift_card_increment')
                    gombcsokkent = driver.find_element_by_class_name('gift_card_decrement')
                    for elad in range(1, varajegynovel):
                        gombnovel.click()
                        if varido > 0:
                            varidodb = varidodb + 1
                            time.sleep(varido)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    for elad in range(0, varajegycsokkent):
                        gombcsokkent.click()
                        if varido > 0:
                            varidodb = varidodb + 1
                            time.sleep(varido)
                        if varkepet_keszit:
                            varkepindex = varkepindex + 1
                            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    driver.find_element_by_id('gift_cards_to_basket').click()
                    time.sleep(7)
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    szoveg = driver.find_element_by_xpath('//*[@id="basket-succeed"]/div/div')
                    # print(szoveg.text)
                    teljesszoveg = '''Sikeres kosárba rakás\nÖn a következő ajándékutalványokat helyezte a kosárba:\n'''
                    # print(teljesszoveg)
                    teljesszoveg = teljesszoveg + elsoszoveg + ' - ' + masodikszoveg + ' - ' + str(
                        varajegynovel - varajegycsokkent) + ' db\n×'
                    # print(teljesszoveg)
                    if szoveg.text != teljesszoveg:
                        teszteset_sikeres = False
                        hibalista.append('Sikeres eladás után a megjelenő szöveg nem megfelelő.')
                        # print('sikeres a szöveg')
                    # print(len(s2.options))
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



def ajandekutalvanykep(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                          varteszteset_kepek, varslaido, varkepsorszam, varkepurl, varaltszoveg, varkepet_keszit=True,
                          kepek_path='c:/kepek/kepek/', varcookief=True):
    """
    Megnézi, hogy az ajándékutalvány oldalon megjelenik-e az adott kép.

    :param driver:
    :param varbongeszo:
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varkepsorszam: A képek közül melyik nézze. 0,1,2 lehet.
    :param varkepurl: Mi a kép url-je.
    :param varaltszoveg: Milyen szövegnek kellene megjelenni a képnél.
    :param varkepet_keszit:
    :param kepek_path:
    :param varcookief:
    :return:
    """
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
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                elem.click()
            except:
                teszteset_sikeres = False
                hibalista.append('Az ajándékkártyára linkre nem sikerült rákattintani.')
            try:
                kepeklistaja = driver.find_elements_by_class_name('mTSThumb')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Képek nem találhatóak az oldalon')
            if len(kepeklistaja) == 0:
                teszteset_sikeres = False
                hibalista.append('Kép nem található az oldalon')
            if teszteset_sikeres:
                pozicio_szoveg = "window.scrollTo(0," + str(kepeklistaja[varkepsorszam].location['y'] - 100) + ");"
                driver.execute_script(pozicio_szoveg)
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                megjelenik = kepeklistaja[varkepsorszam].is_displayed()
                megjelenik2 = driver.execute_script("return arguments[0].complete && typeof arguments[0].naturalWidth != "
                                       "\"undefined\" && arguments[0].naturalWidth > 0", kepeklistaja[varkepsorszam])
                if megjelenik2 == False:
                    teszteset_sikeres = False
                    hibalista.append('A kép nem jelenik meg.')
                if kepeklistaja[varkepsorszam].get_attribute('alt') != varaltszoveg:
                    print(varkepsorszam)
                    print(kepeklistaja[varkepsorszam].get_attribute('alt'))
                    teszteset_sikeres = False
                    hibalista.append('A képhez nem a megfelelő szöveg jelent meg. Ez jelen meg:'
                                     + kepeklistaja[varkepsorszam].get_attribute('alt')
                                     + ', de ennek kellett volna megjelennie:' + varaltszoveg)
                if kepeklistaja[varkepsorszam].get_attribute('src') != (varurl+varkepurl):
                    print(kepeklistaja[varkepsorszam].get_attribute('src'))
                    print(varurl+varkepurl)
                    teszteset_sikeres = False
                    hibalista.append('A képnek nem jó az URL-je. Ez jelent meg:'
                                     + kepeklistaja[varkepsorszam].get_attribute('src') + ', de ennek kellett volna:'
                                     + varurl+varkepurl)
                # print('kép megjelenik-e: ', megjelenik2)
                # print(str(kepeklistaja[varkepsorszam].size['height']))
                #print(str(kepeklistaja[varkepsorszam].size['width']))
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

def ajandekutalvany_gomb_inaktiv(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
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
                cookie = driver.find_element_by_xpath('//*[@id="cookieWrapper"]/p/a[2]')
                cookie.click()
            except:
                print('nincs cooki')
        try:
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                elem.click()
            except:
                teszteset_sikeres = False
                hibalista.append('Az ajándékkártyára linkre nem sikerült rákattintani.')
            if teszteset_sikeres:
                try:
                    gomb = driver.find_element_by_id('gift_cards_to_basket')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A kosár gomb nem található')
                if teszteset_sikeres:
                    pozicio_szoveg = "window.scrollTo(0," + str(gomb.location['y'] - 200) + ");"
                    driver.execute_script(pozicio_szoveg)
                    time.sleep(1)
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    if gomb.is_enabled():
                        teszteset_sikeres = False
                        hibalista.append('A kosár gomb aktív, pedig inaktívnak kellene lennie')
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


def ajandekutalvany_gombneve(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                          varteszteset_kepek, varslaido, vargombneve, varkepet_keszit=True,
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
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                elem.click()
            except:
                teszteset_sikeres = False
                hibalista.append('Az ajándékkártyára linkre nem sikerült rákattintani.')
            if teszteset_sikeres:
                try:
                    gomb = driver.find_element_by_id('gift_cards_to_basket')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A kosár gomb nem található')
                if teszteset_sikeres:
                    pozicio_szoveg = "window.scrollTo(0," + str(gomb.location['y'] - 200) + ");"
                    driver.execute_script(pozicio_szoveg)
                    time.sleep(1)
                    print(gomb.text)
                    if gomb.text != vargombneve:
                        teszteset_sikeres = False
                        hibalista.append('A kosár gomb neve nem megfelelő. Ez a szöveg jelent meg:'+ gomb.text
                                         + ',de ennek a szövegnek kellett volna:'+ vargombneve)

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
        driver.close()
        print(varteszteset_neve + ' lefutott')
    return visszaad, hibalista

def ajandekutalvanylink(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                           varteszteset_kepek, varslaido, varszoveg, varurl2, varkepet_keszit=True,
                        kepek_path='c:/kepek/kepek/'):
    '''
    Ajándékutalvány oldalon lévő link megnézése

    :param driver:
    :param varbongeszo:
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varszoveg: A link szövege amit keresnie kell a programnak.
    :param varurl2: URL ahova a link vezet.
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
        from selenium.webdriver.support.select import Select
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
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            elem.click()
            try:
                szoveg = driver.find_element_by_link_text(varszoveg)
            except:
                teszteset_sikeres = False
                hibalista.append('A megadott link nem található.')
            if teszteset_sikeres:
                pozicio_szoveg = "window.scrollTo(0," + str(szoveg.location['y'] - 100) + ");"
                driver.execute_script(pozicio_szoveg)
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                szoveg.click()
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                teljes_url = varurl + varurl2
                # print(driver.current_url)
                if driver.current_url != teljes_url:
                    teszteset_sikeres = False
                    hibalista.append('Nem a megadott url jelent meg. Ez jelent meg:'+ driver.current_url +
                                     'de ennek kellett volna:' + varurl + varurl2)
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


def ajandekutalvanygombaktiv(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                          varteszteset_kepek, varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/',
                               varcookief=True):
    '''
    Az nézi meg, hogyha kiválasztunk elemeket, akkor a kosárba rak gomb aktív lesz-e.

    :param driver:
    :param varbongeszo:
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
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
        from selenium.webdriver.support.select import Select
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
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                elem.click()
            except:
                teszteset_sikeres = False
                hibalista.append('Az ajándékkártyára linkre nem sikerült rákattintani.')
            if teszteset_sikeres:
                try:
                    gomb = driver.find_element_by_id('gift_cards_to_basket')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A kosár gomb nem található')
                if teszteset_sikeres:
                    pozicio_szoveg = "window.scrollTo(0," + str(gomb.location['y'] - 200) + ");"
                    driver.execute_script(pozicio_szoveg)
                    time.sleep(1)
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    if gomb.is_enabled():
                        teszteset_sikeres = False
                        hibalista.append('A kosár gomb aktív, pedig inaktívnak kellene lennie')
                    if teszteset_sikeres:
                        try:
                            ajandekkartyatipus = driver.find_element_by_id('gift_card_type')
                        except NoSuchElementException:
                            teszteset_sikeres = False
                            hibalista.append('Ajándékkártya típusa nem található')
                        if teszteset_sikeres:
                            selectajandekkartyatipus = Select(ajandekkartyatipus)
                            try:
                                selectajandekkartyatipus.select_by_visible_text('Jegy.hu ajándékutalvány')
                                # selectajandekkartyatipus.select_by_index(1)
                            except NoSuchElementException:
                                teszteset_sikeres = False
                                hibalista.append('Ajándékkártya típusának a kiválasztása nem sikerült')
                            time.sleep(2)
                            if teszteset_sikeres:
                                try:
                                    osszeg = driver.find_element_by_xpath('//*[@id="amount-normal"]/select')
                                except NoSuchElementException:
                                    teszteset_sikeres = False
                                    hibalista.append('A összegválasztó nem található')
                                if teszteset_sikeres:
                                    tipusosszeg = Select(osszeg)
                                    tipusosszeg.select_by_index(1)
                                    time.sleep(2)
                                    if gomb.is_enabled() == False:
                                        teszteset_sikeres = False
                                        hibalista.append('A gomb nem lett aktív')
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
        driver.close()
        print(varteszteset_neve + ' lefutott')
    return visszaad, hibalista


def ajandekutalvanyvissza(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                          varteszteset_kepek, varslaido, varszoveg, varkepet_keszit=True, kepek_path='c:/kepek/kepek/',
                               varcookief=True):
    '''
    Kiválaszt egy ajándékutalványt, majd elnavigál az oldalról és visszajön. Megnézi, hogy a típusok nullázódtak-e.

    :param driver:
    :param varbongeszo:
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varszoveg: A oldalon megjelenő szövegre kattint.
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
        from selenium.webdriver.support.select import Select
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
            elem = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/h4/span/a')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Ajándékkártya link nem található')
        if teszteset_sikeres:
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 100) + ");"
            driver.execute_script(pozicio_szoveg)
            if varido > 0:
                varidodb = varidodb + 1
                time.sleep(varido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                elem.click()
            except:
                teszteset_sikeres = False
                hibalista.append('Az ajándékkártyára linkre nem sikerült rákattintani.')
            if teszteset_sikeres:
                try:
                    gomb = driver.find_element_by_id('gift_cards_to_basket')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append('A kosár gomb nem található')
                if teszteset_sikeres:
                    pozicio_szoveg = "window.scrollTo(0," + str(gomb.location['y'] - 200) + ");"
                    driver.execute_script(pozicio_szoveg)
                    time.sleep(1)
                    if varkepet_keszit:
                        varkepindex = varkepindex + 1
                        seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                    if gomb.is_enabled():
                        teszteset_sikeres = False
                        hibalista.append('A kosár gomb aktív, pedig inaktívnak kellene lennie')
                    if teszteset_sikeres:
                        try:
                            ajandekkartyatipus = driver.find_element_by_id('gift_card_type')
                        except NoSuchElementException:
                            teszteset_sikeres = False
                            hibalista.append('Ajándékkártya típusa nem található')
                        if teszteset_sikeres:
                            selectajandekkartyatipus = Select(ajandekkartyatipus)
                            selectajandekkartyatipus.select_by_visible_text('Jegy.hu ajándékutalvány')
                            # selectajandekkartyatipus.select_by_index(1)
                            time.sleep(2)
                            try:
                                osszeg = driver.find_element_by_xpath('//*[@id="amount-normal"]/select')
                            except NoSuchElementException:
                                teszteset_sikeres = False
                                hibalista.append('A összegválasztó nem található')
                            if teszteset_sikeres:
                                tipusosszeg = Select(osszeg)
                                tipusosszeg.select_by_index(1)
                                time.sleep(2)
                                if varkepet_keszit:
                                    varkepindex = varkepindex + 1
                                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                                driver.find_element_by_link_text(varszoveg).click()
                                time.sleep(2)
                                driver.back()
                                time.sleep(1)
                                try:
                                    ajandekkartyatipus = driver.find_element_by_id('gift_card_type')
                                except NoSuchElementException:
                                    teszteset_sikeres = False
                                    hibalista.append('Ajándékkártya típusa nem található')
                                if teszteset_sikeres:
                                    selectajandekkartyatipus = Select(ajandekkartyatipus)
                                    if selectajandekkartyatipus.first_selected_option.text != 'Válasszon':
                                        teszteset_sikeres = False
                                        hibalista.append('Oldalra való visszatérés után nem nullázódott az '
                                                         'ajándékkártya típus')
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
