def cookiemegnyom(driver):
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    eredmeny = True
    hibalista = []
    try:
        cookie = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button.accept_cookiee")))
    except:
        eredmeny = False
        hibalista.append('A cookie nem jelent meg, vagy az Id alapján nem található')
    if eredmeny:
        try:
            cookie.click()
        except:
            eredmeny = False
            hibalista.append("Nem sikerült kattintani a cookie combra")
    return eredmeny, hibalista
    # driver.find_element_by_class_name("a.button.accept_cookie")

def hirlevel_feliratkozas_felulv2(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras,
                                  varteszteset_kepek,
                                  varslaido, email, irszam, vnev, knev,
                                  tooltipp1, tooltipp2, tooltipp3, varkepet_keszit=True, kepek_path='c:/kepek/kepek/', varcookief= True):
    '''
    Hírlevél feliratkozást csinál az oldal tetején lévő hírlevél feliratkozás ikonon keresztül.

    :param driver: Az inicializált böngésző
    :param varbongeszo: String. Az inicializált böngésző neve
    :param ido: Integer. Bizonyos pontokon ennyi időt vár a program
    :param varurl: String. http/https kell megadni az oldal url címét.
    :param varteszteset_neve: String. A teszteset rövid neve.
    :param varteszteset_leiras: String. A teszteset hosszabb leírása.
    :param varteszteset_kepek: String. A teszteset képeinek a neve-
    :param varslaido: Integer. A függvény futásának az SLA ideje.
    :param email: String. Ezzel az email címmel történik a regisztráció.
    :param irszam: String. Az irányítószám amit a regisztráció során megadunk.
    :param vnev: String. A vezetéknév amit a regisztráció során megadunk.
    :param knev: String. A keresztnév amit a regisztráció során megadunk.
    :param tooltipp1:
    :param tooltipp2:
    :param tooltipp3:
    :param varkepet_keszit:
    :param kepek_path:
    :return:
    '''
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
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
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
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome5\chromedriver.exe')
        driver.get(varurl)
        if varcookief:
            try:
                seged_cs.cookiemegnyom(driver, True)
            except:
                print('nincs cooki')
        if ido > 0:
            time.sleep(ido)
            varidodb = varidodb + 1
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            # driver.get_screenshot_as_file(varteszteset_kepek + '_1.png')
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megnézzük, hogy a hírlevél feliratkozásra felül tudunk-e kattintani.
        try:
            driver.find_element_by_id('newsletterLink').click()
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append("A hírlevél feliratkozás felül nem található")
        # Megnézzük, hogy képet kell-e csinálni miután a hírlevélre kattintottunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük az email mezőt és átadjuk neki az email-t.
        try:
            driver.find_element_by_id('email').send_keys(email)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Email mező nem található az oldalon')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük az email 2. mezőt az oldalon.
        try:
            driver.find_element_by_id('emailconfirm').send_keys(email)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Email 2. mező nem található az oldalon')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük az irányítószámet mezőt és átadjuk neki az irányítószámot.
        try:
            driver.find_element_by_id('zip').send_keys(irszam)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Irányítószám mező nem található az oldalon')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük a vezetéknév mezőt és átadjuk neki a vezetéknevet
        try:
            driver.find_element_by_id('lastname').send_keys(vnev)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Vezetéknév mező nem található')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük a keresztnév mezőt és átadjuk neki a keresztnevet
        try:
            driver.find_element_by_id('firstname').send_keys(knev)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Keresztnév mező nem található')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük a checkbox mezőt az oldalon és belekattintunk.
        try:
            checkbox = driver.find_element_by_id("consent")
            actions = webdriver.ActionChains(driver)
            actions.move_to_element(checkbox).click().perform()
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A checkbox mező nem található')
        except:
            teszteset_sikeres = False
            hibalista.append('A checkbox mező kijelölésénél valami probléma lépett fel')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük a hírlevél feliratkozás gombot és rákattintunk
        try:
            # gomb2 = driver.find_elements_by_css_selector('.submit.moreIcon.right')
            gomb2 = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[13]/div/button')
            pozicio_szoveg = "window.scrollTo(0," + str(gomb2.location['y'] - 200) + ");"
            # legörgetünk a hírlevélhez
            driver.execute_script(pozicio_szoveg)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
            gomb2.click()
            # time.sleep(4)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Hírlevél feliratkozáshoz a gomb nem jelenik meg')
        except:
            teszteset_sikeres = False
            hibalista.append('Hírlevél feliratkozása gomb megnyomása soárn valami probléma történt')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megnézzük, hogy a sikerességről szóló szöveg megjelenik-e.
        try:
            # hibaszoveg = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[3]/div/div/h2')
            hibaszoveg = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[4]/div/div/h2')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A feliratkozó szöveg nem jelenik meg')
        # Megnézzük, hogy a feliratkozás sikeres volt-e.
        if hibaszoveg.text != 'Már csak egy kattintás és kész!':
            teszteset_sikeres = False
            hibaszoveg2 = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[7]/div/div/h2')
            if hibaszoveg2.text == 'Már feliratkozott':
                hibalista.append('Az email cím már fel van iratkozva')
            else:
                hibalista.append('Sikeres feliratkozás szöveggel probléma van.')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + "hiba", varkepindex, True)
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


def hirlevel_feliratkozas_felul(ido, url, teszteset_nev, teszteset_leiras, teszteset_nevkepek, kepet_keszit, kepek_path,
                                email,
                                irszam, vnev, knev, tooltipp1, tooltipp2, tooltipp3):
    try:
        from selenium import webdriver
        import time
        import datetime
        import file_muveletek
        l_teszteset = True
        lista = []
        hibalista = []
        lista.append(teszteset_nev)
        lista.append(teszteset_leiras)
        lista.append(url)

        # ke = datetime.datetime.now()
        kezdet = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        lista.append(kezdet)
        driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome2\chromedriver.exe')
        # Megnézzük, hogy kell-e képet készíteni.
        if kepet_keszit:
            # Ha képet kell készíteni, akkor létrehozzuk a könyvtárat a képeknek.
            kepekh = file_muveletek.kepekhez_konyvtarat(teszteset_nevkepek, kepek_path)
        driver.maximize_window()
        driver.get(url)
        time.sleep(ido)
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_nevkepek + '_1.png')
        driver.find_element_by_id('newsletterLink').click()
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_nevkepek + '_2.png')
        driver.find_element_by_id('email').send_keys(email)
        time.sleep(ido)
        driver.find_element_by_id('emailconfirm').send_keys(email)
        time.sleep(ido)
        driver.find_element_by_id('zip').send_keys(irszam)
        time.sleep(ido)
        driver.find_element_by_id('lastname').send_keys(vnev)
        time.sleep(ido)
        driver.find_element_by_id('firstname').send_keys(knev)
        time.sleep(ido)
        checkbox = driver.find_element_by_id("consent")
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(checkbox).click().perform()
        time.sleep(ido)
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_nevkepek + '_3.png')
        gomb2 = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[12]/div/button')
        pozicio_szoveg = "window.scrollTo(0," + str(gomb2.location['y'] - 200) + ");"
        # legörgetünk a hírlevélhez
        driver.execute_script(pozicio_szoveg)
        time.sleep(ido)
        gomb2.click()
        time.sleep(4)
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_nevkepek + '_4.png')
        hibaszoveg = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[3]/div/div/h2')
        vege = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        if hibaszoveg.text != 'Sikeres feliratkozás!':
            l_teszteset = False
            hibalista.append('Sikeres feliratkozás szöveggel probléma van.')

        if l_teszteset:
            lista.insert(3, 'Sikeres')
        else:
            lista.insert(3, 'Sikertelen')
        lista.append(vege)
        if kepet_keszit:
            lista.append(kepekh)
        driver.close()
        return lista
    except:
        lista.insert(3, 'Sikertelen')
        vege = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        lista.append(vege)
        if kepet_keszit:
            lista.append(kepekh)
        driver.close()
        return lista


def hirlevel_feliratkozas_foglalt_felulv2(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras,
                                          varteszteset_kepek,
                                          varslaido, email, irszam, vnev, knev,
                                          tooltipp1, tooltipp2, tooltipp3, varkepet_keszit=True,
                                          kepek_path='c:/kepek/kepek/', varcookief = True):
    '''
    Hírlevél feliratkozást teszteli foglalt email címmel. Ha megfelelő hibaüzenet jelenik meg, akkor sikeres a teszt.

    :param driver: Az inicializált böngésző
    :param varbongeszo: String. Az inicializált böngésző neve
    :param ido: Integer. Bizonyos pontokon ennyi időt vár a program
    :param varurl: String. http/https kell megadni az oldal url címét.
    :param varteszteset_neve: String. A teszteset rövid neve.
    :param varteszteset_leiras: String. A teszteset hosszabb leírása.
    :param varteszteset_kepek: String. A teszteset képeinek a neve-
    :param varslaido: Integer. A függvény futásának az SLA ideje.
    :param email: String. Ezzel az email címmel történik a regisztráció.
    :param irszam: String. Az irányítószám amit a regisztráció során megadunk.
    :param vnev: String. A vezetéknév amit a regisztráció során megadunk.
    :param knev: String. A keresztnév amit a regisztráció során megadunk.
    :param tooltipp1:
    :param tooltipp2:
    :param tooltipp3:
    :param varkepet_keszit:
    :param kepek_path:
    :return:
    '''
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
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
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
        driver.get(varurl)
        if varcookief:
            try:
                seged_cs.cookiemegnyom(driver, True)
            except:
                print('nincs cooki')
        if ido > 0:
            time.sleep(ido)
            varidodb = varidodb + 1
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            # driver.get_screenshot_as_file(varteszteset_kepek + '_1.png')
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megnézzük, hogy a hírlevél feliratkozásra felül tudunk-e kattintani.
        try:
            driver.find_element_by_id('newsletterLink').click()
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append("A hírlevél feliratkozás felül nem található")
        # Megnézzük, hogy képet kell-e csinálni miután a hírlevélre kattintottunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük az email mezőt és átadjuk neki az email-t.
        try:
            driver.find_element_by_id('email').send_keys(email)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Email mező nem található az oldalon')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük az email 2. mezőt az oldalon.
        try:
            driver.find_element_by_id('emailconfirm').send_keys(email)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Email 2. mező nem található az oldalon')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük az irányítószámet mezőt és átadjuk neki az irányítószámot.
        try:
            driver.find_element_by_id('zip').send_keys(irszam)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Irányítószám mező nem található az oldalon')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük a vezetéknév mezőt és átadjuk neki a vezetéknevet
        try:
            driver.find_element_by_id('lastname').send_keys(vnev)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Vezetéknév mező nem található')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük a keresztnév mezőt és átadjuk neki a keresztnevet
        try:
            driver.find_element_by_id('firstname').send_keys(knev)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Keresztnév mező nem található')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük a checkbox mezőt az oldalon és belekattintunk.
        try:
            checkbox = driver.find_element_by_id("consent")
            actions = webdriver.ActionChains(driver)
            actions.move_to_element(checkbox).click().perform()
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A checkbox mező nem található')
        except:
            teszteset_sikeres = False
            hibalista.append('A checkbox mező kijelölésénél valami probléma lépett fel')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megkeressük a hírlevél feliratkozás gombot és rákattintunk
        try:
            gomb2 = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[13]/div/button')
            pozicio_szoveg = "window.scrollTo(0," + str(gomb2.location['y'] - 200) + ");"
            # legörgetünk a hírlevélhez
            driver.execute_script(pozicio_szoveg)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
            gomb2.click()
            # time.sleep(4)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Hírlevél feliratkozáshoz a gomb nem jelenik meg')
        except:
            teszteset_sikeres = False
            hibalista.append('Hírlevél feliratkozása gomb megnyomása soárn valami probléma történt')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megnézzük, hogy a már feliratkozott szöveg megjelenik-e.
        try:
            hibaszoveg = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[9]/div/div/h2')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A már feliratkozott szöveg nem jelenik meg.')
        # Megnézzük, hogy a feliratkozás elbukott-e.
        if hibaszoveg.text != 'Már feliratkozott':
            teszteset_sikeres = False
            hibalista.append('A már feliratkozott szöveg nem jelent meg.')

    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + "hiba", varkepindex, True)
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


def hirlevel_feliratkozas_foglalt_felul(ido, url, teszteset_nev, teszteset_leiras, teszteset_nevkepek, kepet_keszit,
                                        kepek_path, email,
                                        irszam, vnev, knev, tooltipp1, tooltipp2, tooltipp3):
    try:
        from selenium import webdriver
        import time
        import datetime
        import file_muveletek
        l_teszteset = True
        lista = []
        hibalista = []
        lista.append(teszteset_nev)
        lista.append(teszteset_leiras)
        lista.append(url)

        # ke = datetime.datetime.now()
        kezdet = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        lista.append(kezdet)
        driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome2\chromedriver.exe')
        # Megnézzük, hogy kell-e képet készíteni.
        if kepet_keszit:
            # Ha képet kell készíteni, akkor létrehozzuk a könyvtárat a képeknek.
            kepekh = file_muveletek.kepekhez_konyvtarat(teszteset_nevkepek, kepek_path)
        driver.maximize_window()
        driver.get(url)
        time.sleep(ido)
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_nevkepek + '_1.png')
        driver.find_element_by_id('newsletterLink').click()
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_nevkepek + '_2.png')
        driver.find_element_by_id('email').send_keys(email)
        time.sleep(ido)
        driver.find_element_by_id('emailconfirm').send_keys(email)
        time.sleep(ido)
        driver.find_element_by_id('zip').send_keys(irszam)
        time.sleep(ido)
        driver.find_element_by_id('lastname').send_keys(vnev)
        time.sleep(ido)
        driver.find_element_by_id('firstname').send_keys(knev)
        time.sleep(ido)
        checkbox = driver.find_element_by_id("consent")
        actions = webdriver.ActionChains(driver)
        actions.move_to_element(checkbox).click().perform()
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_nevkepek + '_3.png')
        gomb2 = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[12]/div/button')
        pozicio_szoveg = "window.scrollTo(0," + str(gomb2.location['y'] - 200) + ");"
        # legörgetünk a hírlevélhez
        driver.execute_script(pozicio_szoveg)
        time.sleep(ido)
        gomb2.click()
        time.sleep(4)
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_nevkepek + '_4.png')
        hibaszoveg = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[7]/div/div/h2')
        vege = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        if hibaszoveg.text != 'Már feliratkozott':
            l_teszteset = False
            hibalista.append('Már feliratkozott szöveggel probléma van.')

        if l_teszteset:
            lista.insert(3, 'Sikeres')
        else:
            lista.insert(3, 'Sikertelen')
        lista.append(vege)
        if kepet_keszit:
            lista.append(kepekh)
        driver.close()
        return lista
    except:
        lista.insert(3, 'Sikertelen')
        vege = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        lista.append(vege)
        if kepet_keszit:
            lista.append(kepekh)
        driver.close()
        return lista


def hirlevel_feliratkozas_alul(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras,
                               varteszteset_kepek,
                               varslaido, email, irszam, vnev, knev,
                               tooltipp1, tooltipp2, tooltipp3, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    '''
    Hírlevél feliratkozást csinál az oldal tetején lévő hírlevél feliratkozás ikonon keresztül.

    :param driver: Az inicializált böngésző
    :param varbongeszo: String. Az inicializált böngésző neve
    :param ido: Integer. Bizonyos pontokon ennyi időt vár a program
    :param varurl: String. http/https kell megadni az oldal url címét.
    :param varteszteset_neve: String. A teszteset rövid neve.
    :param varteszteset_leiras: String. A teszteset hosszabb leírása.
    :param varteszteset_kepek: String. A teszteset képeinek a neve-
    :param varslaido: Integer. A függvény futásának az SLA ideje.
    :param email: String. Ezzel az email címmel történik a regisztráció.
    :param irszam: String. Az irányítószám amit a regisztráció során megadunk.
    :param vnev: String. A vezetéknév amit a regisztráció során megadunk.
    :param knev: String. A keresztnév amit a regisztráció során megadunk.
    :param tooltipp1:
    :param tooltipp2:
    :param tooltipp3:
    :param varkepet_keszit:
    :param kepek_path:
    :return:
    '''
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
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
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
        driver.maximize_window()
        driver.get(varurl)
        if ido > 0:
            time.sleep(ido)
            varidodb = varidodb + 1
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            # driver.get_screenshot_as_file(varteszteset_kepek + '_1.png')
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            elem = driver.find_element_by_xpath("//*[@id='footer_newsletter_form']/div[2]/button")
            # összerakjuk a görgetéshez szükséges szöveget
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 200) + ");"
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
            # legörgetünk a hírlevélhez
            driver.execute_script(pozicio_szoveg)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A hírlevélhez kapcsolódó mehet gomb nem található.')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megadjuk az email címet amivel fel szeretnénk iratkozni.
        try:
            driver.find_element_by_id("subsc_email").send_keys(email)
        except NoSuchElementException:
            teszteset_sikeres = False
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megnyomjuk a mehet gombot.
        try:
            driver.find_element_by_xpath("//*[@id='footer_newsletter_form']/div[2]/button").click()
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('mehet gomb nem jelenik meg.')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            a = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[7]/div/div')
            if a.is_displayed() == True:
                teszteset_sikeres = False
                hibalista.append('Email valószínűleg már fel van iratkozva')
        except NoSuchElementException:
            pass
        if teszteset_sikeres:
            # Megkeressük az email 2. mezőt az oldalon.
            try:
                driver.find_element_by_id('emailconfirm').send_keys(email)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Email 2. mező nem található az oldalon')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megkeressük az irányítószámet mezőt és átadjuk neki az irányítószámot.
            try:
                driver.find_element_by_id('zip').send_keys(irszam)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Irányítószám mező nem található az oldalon')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megkeressük a vezetéknév mezőt és átadjuk neki a vezetéknevet
            try:
                driver.find_element_by_id('lastname').send_keys(vnev)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Vezetéknév mező nem található')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megkeressük a keresztnév mezőt és átadjuk neki a keresztnevet
            try:
                driver.find_element_by_id('firstname').send_keys(knev)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Keresztnév mező nem található')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megkeressük a checkbox mezőt az oldalon és belekattintunk.
            try:
                checkbox = driver.find_element_by_id("consent")
                actions = webdriver.ActionChains(driver)
                actions.move_to_element(checkbox).click().perform()
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A checkbox mező nem található')
            except:
                teszteset_sikeres = False
                hibalista.append('A checkbox mező kijelölésénél valami probléma lépett fel')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megkeressük a hírlevél feliratkozás gombot és rákattintunk
            try:
                # gomb2 = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[12]/div/button')
                gomb2 = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[12]/div/button')
                pozicio_szoveg = "window.scrollTo(0," + str(gomb2.location['y'] - 200) + ");"
                # legörgetünk a hírlevélhez
                driver.execute_script(pozicio_szoveg)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
                gomb2.click()
                # time.sleep(4)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Hírlevél feliratkozáshoz a gomb nem jelenik meg')
            except:
                teszteset_sikeres = False
                hibalista.append('Hírlevél feliratkozása gomb megnyomása soárn valami probléma történt')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megnézzük, hogy a sikerességről szóló szöveg megjelenik-e.
            try:
                hibaszoveg = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[3]/div/div/h2')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A feliratkozó szöveg nem jelenik meg')
            # Megnézzük, hogy a feliratkozás sikeres volt-e.
            if hibaszoveg.text != 'Már csak egy kattintás és kész!':
                teszteset_sikeres = False
                hibaszoveg2 = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[7]/div/div/h2')
                if hibaszoveg2.text == 'Már feliratkozott':
                    hibalista.append('Az email cím már fel van iratkozva')
                else:
                    hibalista.append('Sikeres feliratkozás szöveggel probléma van.')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + "hiba", varkepindex, True)
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


def hirlevel_foglalt_alulv2(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras,
                            varteszteset_kepek,
                            varslaido, email, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        from selenium.common.exceptions import NoSuchElementException
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        # driver.implicitly_wait(6)
        print(varteszteset_neve + 'elindult')
        varidodb = 0
        # Teszteset sikerességét ezzel a logikai változóval viszgáljuk. True-ra állítjuk.
        teszteset_sikeres = True
        # Beállítjuk, hogy mikor indult a teszteset
        kezdet2 = datetime.datetime.now()
        # A teszteset futása után egy listát adunk vissza aminek az eredményét fájlba lehet írni.
        visszaad = []
        # A teszteset során ha hiba történik, akkor azt a hibalista-ban adjuk vissza
        hibalista = []
        # Megnézzük, hogy kell-e képet készíteni. Ha kell, akkor létrehozzuk a könyvtárszerkezetet.
        if varkepet_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
            # képindex-ét 0-ra állítjuk
            varkepindex = 0
        else:
            kepek_helye = ''
        # Maximalizáljuk az ablakot
        driver.maximize_window()
        # Betöltjük az url-t.
        driver.get(varurl)
        # Várakozunk ha szükséges
        if ido > 0:
            time.sleep(ido)
            varidodb = varidodb + 1
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            elem = driver.find_element_by_xpath("//*[@id='footer_newsletter_form']/div[2]/button")
            # összerakjuk a görgetéshez szükséges szöveget
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 200) + ");"
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
            # legörgetünk a hírlevélhez
            driver.execute_script(pozicio_szoveg)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A hírlevélhez kapcsolódó mehet gomb nem található.')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megadjuk az email címet amivel fel szeretnénk iratkozni.
        try:
            driver.find_element_by_id("subsc_email").send_keys(email)
        except NoSuchElementException:
            teszteset_sikeres = False
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megnyomjuk a mehet gombot.
        try:
            driver.find_element_by_xpath("//*[@id='footer_newsletter_form']/div[2]/button").click()
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('mehet gomb nem jelenik meg.')
        try:
            driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[7]/div/div')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('Allert hibabox nem jelent meg')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            szoveg = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[9]/div/div/h2')
            if szoveg.text != 'Már feliratkozott':
                teszteset_sikeres = False
                hibalista.append('A már feliratkozott szöveggel probléma van.')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A már feliratkozott szöveg nem jelent meg.')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + "hiba", varkepindex, True)

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


def hirlevel_foglalt_alul(ido, url, email, teszteset_neve, teszteset_leiras, kepek_neve, kepeket_keszit=True,
                          kepek_path='c://kepek/kepek/'):
    '''Egy hírlevél feliratkozást csinál'''
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        import file_muveletek
        # A függvény ezt a visszatérési listát fogja visszaadni.
        visszaad = []
        # A Listához hozzáadjuk a teszteset nevét
        visszaad.append(teszteset_neve)
        # A listához hozzáadjuk a teszteset leírását.
        visszaad.append(teszteset_leiras)
        # send_email('scvinyo@gmail.com','Vinyo734890','vincze.tamas.vinyo@gmail.com','teszt_auto','body szövege')
        # A listához hozzáadjuk az url-t, hogy lássuk hol futtattuk a tesztet.
        visszaad.append(url)
        if kepeket_keszit:
            kepek_helye = file_muveletek.kepekhez_konyvtarat('hirlevel_foglalt', kepek_path)
            # visszaad.append(kepek_helye)
        driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome2\chromedriver.exe')
        # maximalizálom az ablakot
        driver.maximize_window()
        # betöltjük a weboldalt
        kezdet = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        visszaad.append(kezdet)
        driver.get(url)
        time.sleep(ido)
        if kepeket_keszit:
            driver.get_screenshot_as_file('hirlevel_foglalt_1.png')
        # Megkeressük, hogy hol van a hírlevél gomb.
        elem = driver.find_element_by_xpath("//*[@id='footer_newsletter_form']/div[2]/button")
        # print(elem.location['y'])
        # összerakjuk a görgetéshez szükséges szöveget
        pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 200) + ");"
        time.sleep(ido)
        # legörgetünk a hírlevélhez
        driver.execute_script(pozicio_szoveg)
        if kepeket_keszit:
            driver.get_screenshot_as_file('hirlevel_foglalt_2.png')
        # hírlevél mezőbe beírom az emailt
        hirlevel = driver.find_element_by_id("subsc_email").send_keys(email)
        if kepeket_keszit:
            driver.get_screenshot_as_file('hirlevel_foglalt_3.png')
        elem.click()
        if kepeket_keszit:
            driver.get_screenshot_as_file('hirlevel_foglalt_4.png')
        time.sleep(5)
        # email_foglalt = driver.find_elements_by_xpath('//div[contains(text(), "Már feliratkozott")]')
        email_foglalt = driver.find_element_by_tag_name('body').text
        vege = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        visszaad.append(vege)
        if "Már feliratkozott" in email_foglalt:
            # print("fel van iratkozva")
            visszaad.insert(3, 'Sikeres')
            # visszaad[len(visszaad)-1] = visszaad[len(visszaad)-1] + '\n'

        else:
            visszaad.insert(3, 'Sikertelen')
            # visszaad[len(visszaad) - 1] = visszaad[len(visszaad) - 1] + '\n'
        visszaad.append(kepek_helye)
        driver.close()
        return visszaad
    except:
        visszaad.insert(3, 'Sikertelen')
        # visszaad[len(visszaad) - 1] = visszaad[len(visszaad) - 1] + '\n'
        visszaad.append(kepek_helye)
        driver.close()
        return visszaad

def hirlevel_feliratkozas_alul_arena(driver, varbongeszo, ido, varurl, varteszteset_neve, varteszteset_leiras,
                               varteszteset_kepek,
                               varslaido, email, irszam, vnev, knev,
                               tooltipp1, tooltipp2, tooltipp3, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    '''
    Hírlevél feliratkozást csinál az oldal tetején lévő hírlevél feliratkozás ikonon keresztül.

    :param driver: Az inicializált böngésző
    :param varbongeszo: String. Az inicializált böngésző neve
    :param ido: Integer. Bizonyos pontokon ennyi időt vár a program
    :param varurl: String. http/https kell megadni az oldal url címét.
    :param varteszteset_neve: String. A teszteset rövid neve.
    :param varteszteset_leiras: String. A teszteset hosszabb leírása.
    :param varteszteset_kepek: String. A teszteset képeinek a neve-
    :param varslaido: Integer. A függvény futásának az SLA ideje.
    :param email: String. Ezzel az email címmel történik a regisztráció.
    :param irszam: String. Az irányítószám amit a regisztráció során megadunk.
    :param vnev: String. A vezetéknév amit a regisztráció során megadunk.
    :param knev: String. A keresztnév amit a regisztráció során megadunk.
    :param tooltipp1:
    :param tooltipp2:
    :param tooltipp3:
    :param varkepet_keszit:
    :param kepek_path:
    :return:
    '''
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
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
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
        driver.maximize_window()
        driver.get(varurl)
        if ido > 0:
            time.sleep(ido)
            varidodb = varidodb + 1
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            # driver.get_screenshot_as_file(varteszteset_kepek + '_1.png')
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            #elem = driver.find_element_by_xpath("//*[@id='footer_newsletter_form']/div[2]/button")
            elem = driver.find_element_by_id('nl_signup')
            # összerakjuk a görgetéshez szükséges szöveget
            pozicio_szoveg = "window.scrollTo(0," + str(elem.location['y'] - 200) + ");"
            if ido > 0:
                time.sleep(ido)
                varidodb = varidodb + 1
            # legörgetünk a hírlevélhez
            driver.execute_script(pozicio_szoveg)
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A hírlevélhez kapcsolódó mehet gomb nem található.')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megadjuk az email címet amivel fel szeretnénk iratkozni.
        try:
            driver.find_element_by_id('nl_signup').send_keys(email)
        except NoSuchElementException:
            teszteset_sikeres = False
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        # Megnyomjuk a mehet gombot.
        try:
            driver.find_element_by_xpath("/html/body/section[3]/section/footer/div[1]/article[4]/div[2]/form/input").click()
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('mehet gomb nem jelenik meg.')
        finally:
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
        try:
            a = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[7]/div/div')
            if a.is_displayed() == True:
                teszteset_sikeres = False
                hibalista.append('Email valószínűleg már fel van iratkozva')
        except NoSuchElementException:
            pass
        if teszteset_sikeres:
            # Megkeressük az email 2. mezőt az oldalon.
            try:
                driver.find_element_by_id('emailconfirm').send_keys(email)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Email 2. mező nem található az oldalon')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megkeressük az irányítószámet mezőt és átadjuk neki az irányítószámot.
            try:
                driver.find_element_by_id('zip').send_keys(irszam)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Irányítószám mező nem található az oldalon')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megkeressük a vezetéknév mezőt és átadjuk neki a vezetéknevet
            try:
                driver.find_element_by_id('lastname').send_keys(vnev)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Vezetéknév mező nem található')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megkeressük a keresztnév mezőt és átadjuk neki a keresztnevet
            try:
                driver.find_element_by_id('firstname').send_keys(knev)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Keresztnév mező nem található')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megkeressük a checkbox mezőt az oldalon és belekattintunk.
            try:
                checkbox = driver.find_element_by_id("consent")
                actions = webdriver.ActionChains(driver)
                actions.move_to_element(checkbox).click().perform()
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A checkbox mező nem található')
            except:
                teszteset_sikeres = False
                hibalista.append('A checkbox mező kijelölésénél valami probléma lépett fel')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megkeressük a hírlevél feliratkozás gombot és rákattintunk
            try:
                gomb2 = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[12]/div/button')
                pozicio_szoveg = "window.scrollTo(0," + str(gomb2.location['y'] - 200) + ");"
                # legörgetünk a hírlevélhez
                driver.execute_script(pozicio_szoveg)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
                if ido > 0:
                    time.sleep(ido)
                    varidodb = varidodb + 1
                gomb2.click()
                # time.sleep(4)
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('Hírlevél feliratkozáshoz a gomb nem jelenik meg')
            except:
                teszteset_sikeres = False
                hibalista.append('Hírlevél feliratkozása gomb megnyomása soárn valami probléma történt')
            finally:
                if varkepet_keszit:
                    varkepindex = varkepindex + 1
                    seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            # Megnézzük, hogy a sikerességről szóló szöveg megjelenik-e.
            try:
                hibaszoveg = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[3]/div/div/h2')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A feliratkozó szöveg nem jelenik meg')
            # Megnézzük, hogy a feliratkozás sikeres volt-e.
            if hibaszoveg.text != 'Sikeres feliratkozás!':
                teszteset_sikeres = False
                hibaszoveg2 = driver.find_element_by_xpath('//*[@id="formCustomerData"]/div/article/div[7]/div/div/h2')
                if hibaszoveg2.text == 'Már feliratkozott':
                    hibalista.append('Az email cím már fel van iratkozva')
                else:
                    hibalista.append('Sikeres feliratkozás szöveggel probléma van.')
    except:
        teszteset_sikeres = False
        hibalista.append('Egyéb technikai hiba volt')
        if varkepet_keszit:
            varkepindex = varkepindex + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek + "hiba", varkepindex, True)
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


def hirlevel_checkbox(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras,
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
                seged_cs.cookiemegnyom(driver, True)
            except:
                print('nincs cooki')
        try:
            hirlevelikon = driver.find_element_by_id('newsletterLink')
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A hírlevél ikon nem található')
        except:
            teszteset_sikeres = False
            hibalista.append('A hírlevél ikon keresése során valami technikai hiba történt.')
        if teszteset_sikeres:
            # time.sleep(3)
            hirlevelikon.click()
            time.sleep(3)
            if varkepet_keszit:
                varkepindex = varkepindex + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepindex, True)
            try:
                checkbox = driver.find_element_by_id('consent')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A checkbox nem található')
            except:
                teszteset_sikeres = False
                hibalista.append('A checkbx keresése során valami probléma lépett fel')
            if teszteset_sikeres:
                if checkbox.is_selected() == True:
                    teszteset_sikeres = False
                    hibalista.append('A jogi szöveghez tartozó checkbxo be van pipálva.')
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
        print(varteszteset_neve + ' lefutott')
    return visszaad, hibalista