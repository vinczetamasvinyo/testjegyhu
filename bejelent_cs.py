def bejelent_v2(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                   varslaido, varlogin, varjelszo, varnev, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    """
    A eljárás a sikeres bejelentkezést teszteli. A teszteset, akkro ad vissza sikeres értékes ha a megadott adatokkal
    sikerült bejelentkezni és az SLA időn belül maradt a futási idő.
    :param driver: Az adott böngészőnek a drivere.
    :param varbongeszo: String. Milyen böngészőn futtatjuk a tesztet. Ez a szöveg fog bekerülni a visszaadott értékbe.
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varlogin:
    :param varjelszo:
    :param varkepet_keszit:
    :param kepek_path:
    :return:
    """
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
        #driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        # A program futási idejét eltároljuk.
        kezdet2 = datetime.datetime.now()
        # Hibalistát létrehozzunk.
        hibalista = []
        # A várakozási idő darabszámát 0-ra állítjuk. Ebben számoljuk, hogy hányszor várakozott a program.
        varidodb = 0
        # teszteset sikerességét true-ra állítjuk.
        teszteset_sikeres = True
        # Megnézzük, hogy kell-e képet készíteni a teszteset során.
        if varkepet_keszit:
            # A képek sorszámát 0-ra állítjuk. Ezzel számoljuk, hogy hanyadik képnél tartunk.
            varkepsorszama = 0
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
        # maximumra állítjuk a képernyőt
        driver.maximize_window()
        # meghívjuk a kapott url-t.
        driver.get(varurl)
        # Megnézzük, hogy kell-e plusz várakozni.
        if varido > 0:
            # Növeljük a várkozási számot.
            varidodb = varidodb + 1
            # Várakozunk
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        elm = driver.find_elements_by_link_text("Bejelentkezés")
        elm[0].click()
        driver.find_element_by_id('email').send_keys(varlogin)
        if varido > 0:
            # Növeljük a várkozási számot.
            varidodb = varidodb + 1
            # Várakozunk
            time.sleep(varido)
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        driver.find_element_by_id('password1').send_keys(varjelszo)
        if varido > 0:
            # Növeljük a várkozási számot.
            varidodb = varidodb + 1
            # Várakozunk
            time.sleep(varido)
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        driver.find_element_by_id('submitReg').click()
        if varido > 0:
            # Növeljük a várkozási számot.
            varidodb = varidodb + 1
            # Várakozunk
            time.sleep(varido)
        time.sleep(3)
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        if driver.current_url != varurl:
            teszteset_sikeres = False
            hibalista.append('Bejelentkezés után az URL oldal nem stímmel')
        oldal = driver.find_element_by_tag_name('body').text
        if varnev not in oldal:
            teszteset_sikeres = False
            hibalista.append('A név nem jelenik meg az oldalon')
        try:
            elem3 = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/nav/section/ul[2]/li[3]/a')
        except NoSuchElementException:
            print('hiba van a kiírással')
    except:
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepsorszama, True)
        teszteset_sikeres = False
        hibalista.append('Technikai hiba történt')
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
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
                                            kezdet2,vege2,varido,id,varslaido,kepek_helye)

        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad2, hibalista

def bejelent_v3(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                   varslaido, varlogin, varjelszo, varnev, varkepet_keszit=True, kepek_path='c:/kepek/kepek/', varcookief=True):
    """
    A kezdés időpont mérése máshol van.

    A eljárás a sikeres bejelentkezést teszteli. A teszteset, akkro ad vissza sikeres értékes ha a megadott adatokkal
    sikerült bejelentkezni és az SLA időn belül maradt a futási idő.
    :param driver: Az adott böngészőnek a drivere.
    :param varbongeszo: String. Milyen böngészőn futtatjuk a tesztet. Ez a szöveg fog bekerülni a visszaadott értékbe.
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varlogin:
    :param varjelszo:
    :param varkepet_keszit:
    :param kepek_path:
    :return:
    """
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
        #driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        # A program futási idejét eltároljuk.
        # kezdet2 = datetime.datetime.now()
        # Hibalistát létrehozzunk.
        hibalista = []
        # A várakozási idő darabszámát 0-ra állítjuk. Ebben számoljuk, hogy hányszor várakozott a program.
        varidodb = 0
        # teszteset sikerességét true-ra állítjuk.
        teszteset_sikeres = True
        # Megnézzük, hogy kell-e képet készíteni a teszteset során.
        if varkepet_keszit:
            # A képek sorszámát 0-ra állítjuk. Ezzel számoljuk, hogy hanyadik képnél tartunk.
            varkepsorszama = 0
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
        # maximumra állítjuk a képernyőt
        driver.maximize_window()
        # meghívjuk a kapott url-t.
        kezdet2 = datetime.datetime.now()
        driver.get(varurl)
        # Megnézzük, hogy kell-e plusz várakozni.
        if varido > 0:
            # Növeljük a várkozási számot.
            varidodb = varidodb + 1
            # Várakozunk
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        if varcookief:
            try:
                seged_cs.cookiemegnyom(driver, True)
            except:
                print('nincs cooki')
        elm = driver.find_elements_by_link_text("Bejelentkezés")
        elm[0].click()
        driver.find_element_by_id('email').send_keys(varlogin)
        if varido > 0:
            # Növeljük a várkozási számot.
            varidodb = varidodb + 1
            # Várakozunk
            time.sleep(varido)
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        driver.find_element_by_id('password1').send_keys(varjelszo)
        if varido > 0:
            # Növeljük a várkozási számot.
            varidodb = varidodb + 1
            # Várakozunk
            time.sleep(varido)
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        driver.find_element_by_id('submitReg').click()
        if varido > 0:
            # Növeljük a várkozási számot.
            varidodb = varidodb + 1
            # Várakozunk
            time.sleep(varido)
        time.sleep(3)
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        if driver.current_url != varurl:
            teszteset_sikeres = False
            hibalista.append('Bejelentkezés után az URL oldal nem stímmel')
        oldal = driver.find_element_by_tag_name('body').text
        if varnev not in oldal:
            teszteset_sikeres = False
            hibalista.append('A név nem jelenik meg az oldalon')
        try:
            elem3 = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/nav/section/ul[2]/li[3]/a')
        except NoSuchElementException:
            print('hiba van a kiírással')
    except:
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepsorszama, True)
        teszteset_sikeres = False
        hibalista.append('Technikai hiba történt')
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
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
                                            kezdet2,vege2,varido,id,varslaido,kepek_helye)

        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad2, hibalista


def bejelentrosszjelszo(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                   varslaido, varlogin, varjelszo, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    """
    A eljárás a sikeres bejelentkezést teszteli. A teszteset, akkro ad vissza sikeres értékes ha a megadott adatokkal
    sikerült bejelentkezni és az SLA időn belül maradt a futási idő.

    :param driver: Az adott böngészőnek a drivere.
    :param varbongeszo: String. Milyen böngészőn futtatjuk a tesztet. Ez a szöveg fog bekerülni a visszaadott értékbe.
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varlogin:
    :param varjelszo:
    :param varkepet_keszit:
    :param kepek_path:
    :return:
    """
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        import difflib
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        # A program futási idejét eltároljuk.
        kezdet2 = datetime.datetime.now()
        # Hibalistát létrehozzunk.
        hibalista = []
        # A várakozási idő darabszámát 0-ra állítjuk. Ebben számoljuk, hogy hányszor várakozott a program.
        varidodb = 0
        # teszteset sikerességét true-ra állítjuk.
        teszteset_sikeres = True
        # Megnézzük, hogy kell-e képet készíteni a teszteset során.
        if varkepet_keszit:
            # A képek sorszámát 0-ra állítjuk. Ezzel számoljuk, hogy hanyadik képnél tartunk.
            varkepsorszama = 0
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
        # maximumra állítjuk a képernyőt
        driver.maximize_window()
        # meghívjuk a kapott url-t.
        driver.get(varurl)
        # Megnézzük, hogy kell-e plusz várakozni.
        if varido > 0:
            # Növeljük a várkozási számot.
            varidodb = varidodb + 1
            # Várakozunk
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        try:
            elm = driver.find_elements_by_link_text("Bejelentkezés")
            elm[0].click()
            driver.find_element_by_id('email').send_keys(varlogin)
            if varido > 0:
                # Növeljük a várkozási számot.
                varidodb = varidodb + 1
                # Várakozunk
                time.sleep(varido)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            driver.find_element_by_id('password1').send_keys(varjelszo)
            if varido > 0:
                # Növeljük a várkozási számot.
                varidodb = varidodb + 1
                # Várakozunk
                time.sleep(varido)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            driver.find_element_by_id('submitReg').click()
            if varido > 0:
                # Növeljük a várkozási számot.
                varidodb = varidodb + 1
                # Várakozunk
                time.sleep(varido)
            time.sleep(3)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if driver.current_url != varurl + 'registration/doLogin':
                teszteset_sikeres = False
                hibalista.append('A hibaoldal url-je nem stímmel. Ez jelent meg: ' + driver.current_url)
            try:
                elem = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/h1')
                if elem.text != 'Sikertelen belépés':
                    teszteset_sikeres = False
                    hibalista.append('A \"Sikertelen belépés\" szövege rossz')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A \"Sikertelen belépés\" szöveg nem jelent meg.')
            try:
                # elem = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/p')
                elem = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/p[2]')
                # print(elem.text)
                szoveg ='''A megadott belépési adatok(E-mail cím és/vagy jelszó) nem megfelelőek. Kérjük, ellenőrizze az e-mail címet és a jelszót! Amennyiben nem emlékszik a jelszóra, akkor javasoljuk az új jelszó megadását.

Új jelszót adok meg'''
                if elem.text != szoveg:
                    #output_list = [li for li in list(difflib.ndiff(a, b)) if li[0] != ' ']
                    #print(output_list)
                    teszteset_sikeres = False
                    hibalista.append('Hibaszöveg nem egyezik meg.')
                    #print('szöveg nem egyezik')
                    #print(szoveg)
                try:
                    elem = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/a')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append()
            except NoSuchElementException:
                teszteset_sikeres = False
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A bejelentkezés nem található')
    except:
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepsorszama, True)
        teszteset_sikeres = False
        hibalista.append('Technikai hiba történt')
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
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
                                            kezdet2,vege2,varido,id,varslaido,kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad2, hibalista

def bejelentnemletezologin(driver, varbongeszo, varido, varurl, varteszteset_neve, varteszteset_leiras, varteszteset_kepek,
                   varslaido, varlogin, varjelszo, varkepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    """
    A eljárás a sikeres bejelentkezést teszteli. A teszteset, akkro ad vissza sikeres értékes ha a megadott adatokkal
    sikerült bejelentkezni és az SLA időn belül maradt a futási idő.

    :param driver: Az adott böngészőnek a drivere.
    :param varbongeszo: String. Milyen böngészőn futtatjuk a tesztet. Ez a szöveg fog bekerülni a visszaadott értékbe.
    :param varido:
    :param varurl:
    :param varteszteset_neve:
    :param varteszteset_leiras:
    :param varteszteset_kepek:
    :param varslaido:
    :param varlogin:
    :param varjelszo:
    :param varkepet_keszit:
    :param kepek_path:
    :return:
    """
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        import seged_cs
        import file_muveletek
        import difflib
        from selenium.common.exceptions import NoSuchElementException
        print(varteszteset_neve + ' elindult')
        # driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome3\chromedriver.exe')
        # A program futási idejét eltároljuk.
        kezdet2 = datetime.datetime.now()
        # Hibalistát létrehozzunk.
        hibalista = []
        # A várakozási idő darabszámát 0-ra állítjuk. Ebben számoljuk, hogy hányszor várakozott a program.
        varidodb = 0
        # teszteset sikerességét true-ra állítjuk.
        teszteset_sikeres = True
        # Megnézzük, hogy kell-e képet készíteni a teszteset során.
        if varkepet_keszit:
            # A képek sorszámát 0-ra állítjuk. Ezzel számoljuk, hogy hanyadik képnél tartunk.
            varkepsorszama = 0
            kepek_helye = file_muveletek.kepekhez_konyvtarat(varteszteset_kepek, kepek_path)
        # maximumra állítjuk a képernyőt
        driver.maximize_window()
        # meghívjuk a kapott url-t.
        driver.get(varurl)
        # Megnézzük, hogy kell-e plusz várakozni.
        if varido > 0:
            # Növeljük a várkozási számot.
            varidodb = varidodb + 1
            # Várakozunk
            time.sleep(varido)
        # Megnézzük, hogy kell a képet készíteni. Ha kell akkor csinálunk.
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
        try:
            elm = driver.find_elements_by_link_text("Bejelentkezés")
            elm[0].click()
            driver.find_element_by_id('email').send_keys(varlogin)
            if varido > 0:
                # Növeljük a várkozási számot.
                varidodb = varidodb + 1
                # Várakozunk
                time.sleep(varido)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            driver.find_element_by_id('password1').send_keys(varjelszo)
            if varido > 0:
                # Növeljük a várkozási számot.
                varidodb = varidodb + 1
                # Várakozunk
                time.sleep(varido)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            driver.find_element_by_id('submitReg').click()
            if varido > 0:
                # Növeljük a várkozási számot.
                varidodb = varidodb + 1
                # Várakozunk
                time.sleep(varido)
            time.sleep(3)
            if varkepet_keszit:
                varkepsorszama = varkepsorszama + 1
                seged_cs.kepet_keszit(driver, varteszteset_kepek, varkepsorszama, True)
            if driver.current_url != varurl + 'registration/doLogin':
                teszteset_sikeres = False
                hibalista.append('A hibaoldal url-je nem stímmel. Ez jelent meg: ' + driver.current_url)
            try:
                elem = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/h1')
                if elem.text != 'Sikertelen belépés':
                    teszteset_sikeres = False
                    hibalista.append('A \"Sikertelen belépés\" szövege rossz')
            except NoSuchElementException:
                teszteset_sikeres = False
                hibalista.append('A \"Sikertelen belépés\" szöveg nem jelent meg.')
            try:
                # elem = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/p')
                elem = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/p[2]')
                print(elem.text)
                szoveg = '''A megadott belépési adatok(E-mail cím és/vagy jelszó) nem megfelelőek. Kérjük, ellenőrizze az e-mail címet és a jelszót! Amennyiben nem emlékszik a jelszóra, akkor javasoljuk az új jelszó megadását.

Új jelszót adok meg'''
                if elem.text != szoveg:
                    #print(elem.text)
                    output_list = [li for li in list(difflib.ndiff(elem.text, szoveg)) if li[0] != ' ']
                    print(output_list)
                    teszteset_sikeres = False
                    hibalista.append('Hibaszöveg nem egyezik meg.')
                    #print('szöveg nem egyezik')
                    #print(szoveg)
                try:
                    elem = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/a')
                except NoSuchElementException:
                    teszteset_sikeres = False
                    hibalista.append()
            except NoSuchElementException:
                teszteset_sikeres = False
        except NoSuchElementException:
            teszteset_sikeres = False
            hibalista.append('A bejelentkezés nem található')
    except:
        if varkepet_keszit:
            varkepsorszama = varkepsorszama + 1
            seged_cs.kepet_keszit(driver, varteszteset_kepek+'hiba', varkepsorszama, True)
        teszteset_sikeres = False
        hibalista.append('Technikai hiba történt')
    finally:
        vege2 = datetime.datetime.now()
        masodperc = varidodb * varido
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
                                            kezdet2,vege2,varido,id,varslaido,kepek_helye)
        driver.close()
        print(varteszteset_neve + ' lefutott')
        return visszaad2, hibalista