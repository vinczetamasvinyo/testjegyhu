def top10v2(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                  varslaido, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    '''
    Megnézi, hogy a TOP10-es választó megjelenik-e az oldalon.

    :param driver: Az inicalizált böngésző.
    :param varbongeszo: String. A böngésző neve amin futtatjuk.
    :param ido: Integer.
    :param varurl: String. Az oldal címe ahol futtatjuk a tesztesetet.
    :param varteszteset_neve: String. Teszteset rövid neve.
    :param varteszteset_leiras: String. A teszteset hosszabb leírása
    :param varteszteset_kepek:  String. A képek neve
    :param varslaido: Integer. SLA idő ami alatt végig kell futtnia a programnak.
    :param varkepet_keszit: Boolean. Kell-e képet készíteni a programnak.
    :param kepek_path: Hova készítsen képet a program.
    :return: Két listát az vissza. Egy alap listát illetve egy hibalistát.
    '''
    global kepek_helye, teszteset_sikeres, kezdet2, varidodb, datetime, seged_cs, hibalista, varkepindex, varkepindex
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
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindex-ét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        driver.maximize_window()
        driver.get(varurl)
        if ido > 0:
            varidodb = varidodb + 1
            time.sleep(ido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            # driver.get_screenshot_as_file(varteszteset_kepek + '_1.png')
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            a = driver.find_element_by_class_name('rateValue')
            # összerakjuk a görgetéshez szükséges szöveget
            pozicio_szoveg = "window.scrollTo(0," + str(a.location['y'] - 200) + ");"
            # legörgetünk a TOP10-es listához
            driver.execute_script(pozicio_szoveg)
            if ido > 0:
                varidodb = varidodb + 1
                time.sleep(ido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A top10 nem jelenik meg.')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
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
        print(varteszteset_neve + ' lefutott')
        return visszaad, hibalista

def top10selectv2(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                  varslaido, varindex, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    '''
    Megnézi, hogy a TOP10-es választó megjelenik-e az oldalon.

    :param driver: Az inicalizált böngésző.
    :param varbongeszo: String. A böngésző neve amin futtatjuk.
    :param ido: Integer.
    :param varurl: String. Az oldal címe ahol futtatjuk a tesztesetet.
    :param varteszteset_neve: String. Teszteset rövid neve.
    :param varteszteset_leiras: String. A teszteset hosszabb leírása
    :param varteszteset_kepek:  String. A képek neve
    :param varslaido: Integer. SLA idő ami alatt végig kell futtnia a programnak.
    :param varkepet_keszit: Boolean. Kell-e képet készíteni a programnak.
    :param kepek_path: Hova készítsen képet a program.
    :return: Két listát az vissza. Egy alap listát illetve egy hibalistát.
    '''
    global kepek_helye, teszteset_sikeres, kezdet2, varidodb, datetime, seged_cs, hibalista, varkepindex, varkepindex
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        print(varteszteset_neve + ' elindult')

        #driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        # driver.implicitly_wait(6)
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindex-ét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        driver.maximize_window()
        driver.get(varurl)
        if ido > 0:
            varidodb = varidodb + 1
            time.sleep(ido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            # driver.get_screenshot_as_file(varteszteset_kepek + '_1.png')
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            a = driver.find_element_by_id('toplist_type_select')
            # a = driver.find_element_by_class_name('rateValue')
            # összerakjuk a görgetéshez szükséges szöveget
            pozicio_szoveg = "window.scrollTo(0," + str(a.location['y'] - 200) + ");"
            # legörgetünk a TOP10-es listához
            driver.execute_script(pozicio_szoveg)
            if ido > 0:
                varidodb = varidodb + 1
                time.sleep(ido)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A top10 nem jelenik meg.')
        if teszteset_sikeres:
            s1 = Select(driver.find_element_by_id('toplist_type_select'))
            # print(len(s1.options))
            # print(len(s1.options))
            s1.select_by_index(varindex)

            time.sleep(2)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                a = driver.find_element_by_class_name('rateValue')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A 10-es lista nem jelenik meg.')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * ido
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
        kezdet2, vege2, ido, tiszta_futasi_ido, varslaido, kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad, hibalista


def top10_select (url, teszteset_neve, teszteset_leiras, teszteset_kepek, l_index, kepet_keszit=True, kepek_path='c://kepek/kepek/'):
    """
    A függvény megnézi, hogy a top10 elérhető-e az adott oldalon. Ha megtalálható a top10-es lista, akkor sikeres értékkel tér viszsa.
    Ha nem található meg, akkor Sikertelen értékkel tér vissza

    :param url: Az oldal url-je ahol a prog futni fog.
    :param teszteset_neve: A teszteset rövid neve kerül ide.
    :param teszteset_leiras: A teszteset hosszabb leírása kerül ide. Ez olyan mint a summary mező a tesztesetnél.
    :param teszteset_kepek: teszteset során a képek neve lesz.
    :param l_index: A dropdown listban hanyadik index-et kell megnézni.
    :param kepet_keszit: A teszt során kell-e képet készíteni.
    :param kepek_path: Hova készüljenek a képe.
    :return: Egy listát ad vissza aminek az első eleme a teszteset neve=TOP10, második a tesztesetehez kapcsolódó leírás. A harmadik rész, hogy sikeres vagy sikertelen volt. A negyedik a képek helye ha készült.

    """
    global kezdet, visszaad, datetime, kepek_helye
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        kezdet = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        # függvény visszatérési listája lesz ez
        visszaad = []
        visszaad.append(teszteset_neve)
        visszaad.append(teszteset_leiras)
        if kepet_keszit == True:
            kepek_helye = kepekhez_konyvtarat(teszteset_kepek)
        driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome2\chromedriver.exe')
        # maximalizálom az ablakot
        driver.maximize_window()
        # betöltjük a weboldalt
        driver.get(url)
        if kepet_keszit == True:
            driver.get_screenshot_as_file(teszteset_kepek + '_1.png')
        # Megkeresseük, hogy a top10-es elem megtalálható az oldalon.
        a = driver.find_element_by_class_name('rateValue')
        # print(a.location['y'])
        # összerakjuk a görgetéshez szükséges szöveget
        pozicio_szoveg = "window.scrollTo(0," + str(a.location['y'] - 200) + ");"
        # print(pozicio_szoveg)
        # legörgetünk a TOP10-es listához
        driver.execute_script(pozicio_szoveg)
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_kepek + '_2.png')
        # print(a)
        s1 = Select(driver.find_element_by_id('toplist_type_select'))
        print(len(s1.options))

        s1.select_by_index(int(l_index))

        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_kepek + '_3.png')
        # time.sleep(2)
        a = driver.find_element_by_class_name('rateValue')
        visszaad.append('Sikeres')
        vege = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        visszaad.append(kezdet)
        visszaad.append(vege)
        if kepet_keszit:
            visszaad.append(kepek_helye)
        return visszaad
    except:
        vege = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        visszaad.append(kezdet)
        visszaad.append(vege)
        visszaad.append('Sikertelen')
        if kepet_keszit:
            visszaad.append(kepek_helye)
        return visszaad

def top10nyilak(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                    varteszteset_kepek, varslaido, varkepet_keszit=True,
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
            ajanlodarab = driver.find_elements_by_class_name('toplistBox')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Az oldalon nem található top10-es lista')
            pozicio_szoveg = "window.scrollTo(0," + str(800 - 100) + ");"
            driver.execute_script(pozicio_szoveg)
        if teszteset_sikeres:
            try:
                listanyilfel = driver.find_elements_by_class_name('up')
                nyilfeldb = len(listanyilfel)
            except NoSuchElementException:
                nyilfeldb = 0

            try:
                listanyille = driver.find_elements_by_class_name('down')
                nyilledb = len(listanyille)
            except NoSuchElementException:
                nyilledb = 0
            try:
                listavonal = driver.find_elements_by_class_name('noChange')
                vonaldb = len(listavonal)
            except NoSuchElementException:
                vonaldb = 0
            if len(ajanlodarab) != nyilfeldb + nyilledb + vonaldb:
                print(nyilfeldb, nyilledb, vonaldb)
                teszteset_sikeres = False
                hibalista.append('A nyilak, vonalak száma nem megfelelő. Összes top10(' + str(len(ajanlodarab)) +
                                 '). Felnyilak=' + str(nyilfeldb)+ ', Lenyilak=' + str(nyilledb)
                                 + ', Vonal=' + str(vonaldb) + '.')

            if varkepet_keszit:
                for i in range(0, len(ajanlodarab)):
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


def top10nyilakalmenu(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
                    varteszteset_kepek, varslaido, varindex, varkepet_keszit=True,
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
            valaszto = driver.find_element_by_id('toplist_type_select')
        except:
            hibalista.append('Nem található a top10-es választó')
            teszteset_sikeres = False
        if teszteset_sikeres:
            svalaszto = Select(valaszto)
            svalaszto.select_by_index(varindex)
            time.sleep(2)
            try:
                ajanlodarab = driver.find_elements_by_class_name('toplistBox')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Az oldalon nem a top10-es lista')
                pozicio_szoveg = "window.scrollTo(0," + str(800 - 100) + ");"
                driver.execute_script(pozicio_szoveg)
            if teszteset_sikeres:
                try:
                    listanyilfel = driver.find_elements_by_class_name('up')
                    nyilfeldb = len(listanyilfel)
                except NoSuchElementException:
                    nyilfeldb = 0
                try:
                    listanyille = driver.find_elements_by_class_name('down')
                    nyilledb = len(listanyille)
                except NoSuchElementException:
                    nyilledb = 0
                try:
                    listavonal = driver.find_elements_by_class_name('noChange')
                    vonaldb = len(listavonal)
                except NoSuchElementException:
                    vonaldb = 0
                if len(ajanlodarab) != nyilfeldb + nyilledb + vonaldb:
                    print(nyilfeldb, nyilledb, vonaldb)
                    teszteset_sikeres = False
                    hibalista.append('A nyilak, vonalak száma nem megfelelő. Összes top10(' + str(len(ajanlodarab)) +
                                     '). Felnyilak=' + str(nyilfeldb)+ ', Lenyilak=' + str(nyilledb)
                                     + ', Vonal=' + str(vonaldb) + '.')

                if varkepet_keszit:
                    for i in range(0, len(ajanlodarab)):
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