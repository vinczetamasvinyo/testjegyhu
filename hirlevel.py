def csv_keszito(lista, elvalaszto=';', sorveg=True):
    '''
    A listából egy csv formátumot készít, hogy be tudjuk szúrni a fájlba csv formátumként.
    :param lista: Lista amivel dolgozik a függvény
    :param elvalaszto: Milyen elválasztó karakter kerüljön a csv fájl-ba. Alapértelmezette ; karaktert használja,
    :param sorveg: Szükséges-e sortörést beszúrni. Alapesetben sortörést szúrunk be.
    :return: Visszaad egy csv fájl számára hasznos listát.
    '''
    list2 = []
    for listaelem in lista:
        list2.append(listaelem + elvalaszto)
    if sorveg:
        list2[len(list2) - 1] = list2[len(list2) - 1] + '\n'
    return list2


def kepekhez_konyvtarat(teszteset_neve, kepek_path='c:/kepek/kepek/'):
    '''
    Létrehozza és beállítja a könyvtárstruktúrát ahova a teszteset során a képeket készít a teszteset.
    :param teszteset_neve: Teszteset neve amihez a képeket készíti majd a program. Ez a név belekerül a könyvtárnévbe.
    :param kepek_path: Képek készítésének a foldere. Ha nem adjuk meg, akkor az alapérték c:/kepek/kepek
    :return: A függvény visszaadja a létrehozott könyvtár elérési útját.
    '''
    import time
    import os
    import datetime
    path = kepek_path + datetime.date.today().strftime("%Y_%m_%d")
    ido = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    if os.path.exists(path) != True:
        os.makedirs(path)
    os.chdir(path)
    alkonyvtar = teszteset_neve + '_' + ido
    os.makedirs(alkonyvtar)
    os.chdir(alkonyvtar)
    return path + '/' + alkonyvtar


def top10(url, kepet_keszit=True, kepek_path='c://kepek/kepek/'):
    '''
    A függvény megnézi, hogy a top10 elérhető-e az adott oldalon. Ha megtalálható a top10-es lista, akkor sikeres értékkel tér viszsa.
    Ha nem található meg, akkor Sikertelen értékkel tér vissza

    :param url: Az oldal url-je ahol a prog futni fog.
    :param kepet_keszit: A teszt során kell-e képet készíteni.
    :param kepek_path: Hova készüljenek a képe.
    :return: Egy listát ad vissza aminek az első eleme a teszteset neve=TOP10, második a tesztesetehez kapcsolódó leírás. A harmadik rész, hogy sikeres vagy sikertelen volt. A negyedik a képek helye ha készült.

    '''
    global visszaad, kepek_helye
    try:
        from selenium import webdriver
        from selenium.webdriver.support.select import Select
        import time
        import os
        import datetime
        # függvény visszatérési listája lesz ez
        visszaad = []
        visszaad.append('Top10 megnézése')
        visszaad.append('Teszt során azt nézzük, hogy a Top10-es lista megjelenik-e')
        # A listához hozzáadjuk az url-t, hogy lássuk hol futtattuk a tesztet.
        visszaad.append(url)
        if kepet_keszit == True:
            kepek_helye = kepekhez_konyvtarat('top10')
        driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome2\chromedriver.exe')
        # maximalizálom az ablakot
        driver.maximize_window()
        # betöltjük a weboldalt
        driver.get(url)
        if kepet_keszit == True:
            driver.get_screenshot_as_file('top10_1.png')
        # Megkeresseük, hogy a top10-es elem megtalálható az oldalon.
        a = driver.find_element_by_class_name('rateValue')
        print(a.location['y'])
        # összerakjuk a görgetéshez szükséges szöveget
        pozicio_szoveg = "window.scrollTo(0," + str(a.location['y'] - 200) + ");"
        print(pozicio_szoveg)
        # legörgetünk a TOP10-es listához
        driver.execute_script(pozicio_szoveg)
        if kepet_keszit:
            driver.get_screenshot_as_file('top10_2.png')
        print(a)
        visszaad.append('Sikeres')
        if kepet_keszit:
            visszaad.append(kepek_helye)
        # visszaad[len(visszaad)-1] = visszaad[len(visszaad)-1]+'\n'
        return visszaad
    except:
        visszaad.append('Sikertelen')
        if kepet_keszit:
            visszaad.append(kepek_helye)
        # visszaad[len(visszaad) - 1] = visszaad[len(visszaad) - 1] + '\n'
        return visszaad


class teszteset():
    nev = ""
    eredmeny = ""
    kepek_elerese = ""


def send_email(user, pwd, recipient, subject, body):
    import smtplib
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, 'valami')
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")


def regisztraico_rovid_jelszo(url, email, jelszo, hiba_szoveg, kepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    global driver, visszaad, kepekh
    try:
        from selenium import webdriver
        driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome2\chromedriver.exe')
        # Megnézzük, hogy kell-e képet készíteni.
        if kepet_keszit:
            kepekh = kepekhez_konyvtarat('Regisztracio_rovid_jelszo')
        driver.maximize_window()
        driver.get(url)
        if kepet_keszit:
            driver.get_screenshot_as_file('reg_rovid_jelszo1.png')
        elm = driver.find_elements_by_link_text("Bejelentkezés")
        elm[0].click()
        if kepet_keszit:
            driver.get_screenshot_as_file('reg_rovid_jelszo2.png')
        elm = driver.find_elements_by_link_text('Regisztráció')
        elm[0].click()
        if kepet_keszit:
            # Csinálunk egy
            driver.get_screenshot_as_file('reg_rovid_jelszo3.png')
        # A visszaad listát inicializáljuk.
        # Ebben adjuk vissza a teszteset eredményeit.
        visszaad = []
        # A teszteset nevét megadjuk a listába
        visszaad.append('Regisztráció rövid jelszó')
        # A teszteset leírását megadjuk a listába
        visszaad.append('A teszt során azt nézzük, hogy rövid jelszó megadása során megfelelő hibaüzenet jelenik-e meg')
        visszaad.append(url)
        # Ha képet kell készítni, akkor a képek helyét beszűrjuk a listába
        if kepet_keszit:
            kepek_helye = kepek_path
            visszaad.append(kepekh)
        # Az email mezőbe beírjuk az email változó tartalmát.
        driver.find_element_by_id('email').send_keys(email)
        # A jelszó mezőbe beírjuk a jelszo változó tartalmát.
        driver.find_element_by_id('password1').send_keys(jelszo)

        driver.find_element_by_id('submitReg').click()
        # Megnézzük, hogy kell-e képet készíteni. Ha kell akkor csinálunk.
        if kepet_keszit:
            # Képet csinálunk mikor megnyomtuk a regisztrációs gombot.
            driver.get_screenshot_as_file('reg_rovid_jelszo4.png')
        if driver.find_element_by_class_name('validation_errors').text == hiba_szoveg:
            visszaad.insert(3, 'Sikeres')
            print(len(visszaad))
        else:
            visszaad.insert(3, 'Sikertelen')
        # visszaad[len(visszaad)-1] = visszaad[len(visszaad)-1] + '\n'
        driver.close()
        return visszaad
    except:
        visszaad.insert(3, 'Sikertelen')
        # visszaad[(visszaad) - 1] = visszaad[(visszaad) - 1] + '\n'
        driver.close()
        return visszaad


def regisztraico_jelszo_ellenorzes(url, teszteset_nev, teszteset_leiras, teszteset_nevk, email, jelszo, hiba_szoveg,
                                   kepet_keszit=True, kepek_path='c:/kepek/kepek/'):
    '''
    A teszt a jelszó erősségéhez kapcsolódó teszteket végzi el amikor a hiba szövege egy külön oldalon jelenik meg.
    Ezek a tesztesetek amikor minimum 8 karakter hosszú jelszót adunk meg, de csak betűt, számot, betűt és számot.
    :param url: Az oldal url-je ahol a tesztet kell végezni. Például http://www.jegy.hu
    :param teszteset_nev: String változó. A teszteset nevét kell ide beleírni. Ez fog a tesztelési fájlba belekerülni.
    :param teszteset_leiras: String változó. A tesztesethez tartozó hosszabb leírást kell ideírni. Ez fog a tesztelési fájlba belekerülni.
    :param teszteset_nevk: String változó. A képek nevét kell itt megadni.
    :param email: String változó. A regisztráció során ez az email kerül beírásra.
    :param jelszo: String változó. A regisztráció során ez a jelszó kerül megadásra.
    :param hiba_szoveg: string változó. A regisztráció során ez a hibaüzenet jelenik meg.
    :param kepet_keszit: Logikai változó. Kell-e képet készíteni a teszt során. Alapesetben True a változó értéke.
    :param kepek_path: Képek elérési helye ahova ezek készülnek. Alapesetben c:/kepek/kepek könyvtárba készülnek.
    :return:
    '''
    global driver, visszaad, kepekh
    try:
        from selenium import webdriver
        teszt_sikeres = True
        driver = webdriver.Chrome('C:\python\selenium\webdriver\chrome2\chromedriver.exe')
        # Megnézzük, hogy kell-e képet készíteni.
        if kepet_keszit:
            # Ha képet kell készíteni, akkor létrehozzuk a könyvtárat a képeknek.
            kepekh = kepekhez_konyvtarat(teszteset_nevk)
        driver.maximize_window()
        driver.get(url)
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_nevk + '_jelszo1.png')
        elm = driver.find_elements_by_link_text("Bejelentkezés")
        elm[0].click()
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_nevk + '_jelszo2.png')
        elm = driver.find_elements_by_link_text('Regisztráció')
        elm[0].click()
        if kepet_keszit:
            # Csinálunk egy
            driver.get_screenshot_as_file(teszteset_nevk + '_jelszo3.png')
        # A visszaad listát inicializáljuk.
        # Ebben adjuk vissza a teszteset eredményeit.
        visszaad = []
        # A teszteset nevét megadjuk a listába
        visszaad.append(teszteset_nev)
        # A teszteset leírását megadjuk a listába
        visszaad.append(teszteset_leiras)
        visszaad.append(url)
        # Ha képet kell készítni, akkor a képek helyét beszűrjuk a listába
        if kepet_keszit:
            visszaad.append(kepekh)
        # Az email mezőbe beírjuk az email változó tartalmát.
        driver.find_element_by_id('email').send_keys(email)
        # A jelszó mezőbe beírjuk a jelszo változó tartalmát.
        driver.find_element_by_id('password1').send_keys(jelszo)
        if kepet_keszit:
            # Képet csinálunk mikor megnyomtuk a regisztrációs gombot.
            driver.get_screenshot_as_file(teszteset_nevk + '_jelszo4.png')
        driver.find_element_by_id('submitReg').click()
        # Megnézzük, hogy kell-e képet készíteni. Ha kell akkor csinálunk.
        if kepet_keszit:
            # Képet csinálunk mikor megnyomtuk a regisztrációs gombot.
            driver.get_screenshot_as_file(teszteset_nevk + '_jelszo5.png')
        elem = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/p')
        driver.find_element_by_xpath(("//button[contains(.,'Új jelszó megadása')]"))
        if elem.text == hiba_szoveg:
            visszaad.insert(3, 'Sikeres')
        else:
            visszaad.insert(3, 'Sikertelen')
        # visszaad[len(visszaad)-1] = visszaad[len(visszaad)-1] + '\n'
        driver.close()
        return visszaad
    except:
        visszaad.insert(3, 'Sikertelen')
        # visszaad[(visszaad) - 1] = visszaad[(visszaad) - 1] + '\n'
        driver.close()
        return visszaad


def top10_select(url, teszteset_neve, teszteset_leiras, teszteset_kepek, l_index, kepet_keszit=True,
                 kepek_path='c://kepek/kepek/'):
    '''
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

    '''
    global driver, kezdet, visszaad, datetime, kepek_helye
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
        visszaad.append(url)
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
        print(a.location['y'])
        # összerakjuk a görgetéshez szükséges szöveget
        pozicio_szoveg = "window.scrollTo(0," + str(a.location['y'] - 200) + ");"
        print(pozicio_szoveg)
        # legörgetünk a TOP10-es listához
        driver.execute_script(pozicio_szoveg)
        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_kepek + '_2.png')
        print(a)
        s1 = Select(driver.find_element_by_id('toplist_type_select'))
        s1.select_by_index(int(l_index))

        if kepet_keszit:
            driver.get_screenshot_as_file(teszteset_kepek + '_3.png')
        time.sleep(2)
        # time.sleep(4)
        a = driver.find_element_by_class_name('rateValue')
        visszaad.append('Sikeres')
        vege = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        visszaad.append(kezdet)
        visszaad.append(vege)
        if kepet_keszit:
            visszaad.append(kepek_helye)
        driver.close()
        return visszaad
    except:
        vege = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S.%f")
        visszaad.append(kezdet)
        visszaad.append(vege)
        visszaad.insert(3, 'Sikertelen')
        if kepet_keszit:
            visszaad.append(kepek_helye)
        driver.close()
        return visszaad


if __name__ == "__main__":
    import time
    import os
    import datetime
    import hirlevel_cs
    import bongeszo
    import kereso_cs
    import top10_select
    import gyakorlat
    import seged_cs
    import kiemelt_ajanlat_cs
    import bejelent_cs
    import regisztracio_cs
    import requests
    import cookie
    import tooltipp_cs
    import ajandekutalvany_cs
    # kornyezet = "https://acceptance.jegy.hu/"
    ajandeknormal = "Jegy.hu ajándékutalvány"
    ajandekszul =  "Boldog születésnapot!"
    ajandeknevnap = "Boldog névnapot!"
    most = datetime.datetime.now()
    ajandekkezdet = datetime.datetime(2018, 11, 5)
    ajandekvege = datetime.datetime(2019, 1, 5)
    kornyezet = 'https://www.jegy.hu/'
    sla_ajandekutalvany = 27
    # kornyezet = 'https://mobiletest.jegy.hu/'
    # kornyezet = 'https://mobiletestlive.jegy.hu/'
    """
    ***************************************************************************
    Email összeállítása
    ***************************************************************************
    """
    szoveg1 = """\
        <html>
          <head></head>
          <body>
            <table border 1px solid black;>
            <tr>
                <th style="min-width: 200px;">Teszteset neve</th>
                <th style="min-width: 600px;">Teszteset leírása</th> 
                <th>Hely_URL</th>
                <th>Eredmény</th>
                <th>Bongeszo</th>
                <th>Kezdes</th>
                <th>Vege</th>
                <th>Osszes_futasi_ido</th>
                <th>Varakozas_ido</th>
                <th>Tiszta_futasi_ido</th>
                <th>SLA_ido</th>
                <th>Kepek_helye</th>
                <th>Hibak</th>
            </tr>
            """
    szoveg3 = """</table>        
          </body>
        </html>
        """
    filelokhelye = "C:/Vinyo/test_jelszavak/eles/"
    emaillista = []
    # emaillista.append("vincze.tamas.vinyo@gmail.com")
    emaillista.append("tamas.vincze@interticket.net")
    # emailszoveg = szoveg1
    emailszoveg = ""
    tesztesetek = []
    tesztesetek.append(0)
    tesztesetek.append(0)
    tesztesetek.append(0)
    # print(str(tesztesetek[0])+'/'+str(tesztesetek[1])+'/'+str(tesztesetek[2]))
    teszt = teszteset()
    # Lekérjuk az adott nap dátumát, és az aktuális időt, majd ezt eltároljuk az idő változóban.
    ido = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # Létrehozzuk egy fájlt amibe a futási eredményeket fugjuk eltárolni.
    post_fields = {'address': 'scvinyo9%40gmail.com'}
    r = requests.post('https://www.jegy.hu/admin/newsletter/unsubscribe', data=post_fields)
    print(r.status_code, r.reason)
    print(r.text)
    file = open('C:/auto_teszt/automata_teszt' + ido + '.csv', 'w')
    file.writelines(
        "Teszteset neve;Teszteset leírása;Hely_URL;Eredmény;Bongeszo;Kezdes;Veged;Osszes_futasi_ido;Varakozas_ido;Tiszta_futasi_ido;SLA_ido;Kepek_helye\n")


    '''     
    *****************************************************************************************
    Hírlevél checkbox
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Hírlevél feliratkozás checkbox megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy a hírlevél feliratkozásnál a checkbox ne legyen bepipálva.'
    kep = 'hirlevel_chekcbox'
    lista, hibalista = \
        hirlevel_cs.hirlevel_checkbox(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'hirlevelcheckbox', 20)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))


    '''     
    *****************************************************************************************
    Top10 nyilak múzeum, kiállítás
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'TOP 10 nyilak múzeum, kiállítás'
    teszt2 = 'Teszt során azt nézzük, hogy a nyilak megjelennek-e TOP10-es múzeum, kiállításnál'
    kep = 'top10nyilakmuzeum'
    lista, hibalista = \
        top10_select.top10nyilakalmenu(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, kep, 16, 4)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Top10 nyilak fesztival
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'TOP 10 nyilak fesztival'
    teszt2 = 'Teszt során azt nézzük, hogy a nyilak megjelennek-e TOP10-es fesztival'
    kep = 'top10nyilakfesztival'
    lista, hibalista = \
        top10_select.top10nyilakalmenu(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, kep, 16, 3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Top10 nyilak koncert, zene
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'TOP 10 nyilak koncert, zene'
    teszt2 = 'Teszt során azt nézzük, hogy a nyilak megjelennek-e TOP10-es koncert, zene'
    kep = 'top10nyilakkoncert'
    lista, hibalista = \
        top10_select.top10nyilakalmenu(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, kep, 16, 2)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Top10 nyilak színház
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'TOP 10 nyilak színház'
    teszt2 = 'Teszt során azt nézzük, hogy a nyilak megjelennek-e TOP10-es színháznál'
    kep = 'top10nyilakszinhaz'
    lista, hibalista = \
        top10_select.top10nyilakalmenu(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, kep, 16, 1)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Top10 nyilak össze kategória
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'TOP 10 nyilak összes kategória'
    teszt2 = 'Teszt során azt nézzük, hogy a nyilak megjelennek-e a TOP10 összes-ben.'
    lista, hibalista = \
        top10_select.top10nyilak(chrome,'chrome',0,kornyezet,teszt1,teszt2,'top10nyilak',16)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajánló db soráng gomb inaktív
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándlók darabszáma'
    teszt2 = 'Teszt során azt nézzük, hogy az ajánlók darabszáma megfelelő-e.'
    lista, hibalista = \
        kiemelt_ajanlat_cs.ajanlodb(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'ajanlodb', 15, 8, 16)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Cookieban lévő link megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Cookieban lévő link megfelelő-e'
    teszt2 = 'Teszt során azt nézzük, hogy a cookieban lévő link megfelelően működik-e.'
    linkhelye = '//*[@id="cookieWrapper"]/p/a[1]'
    cooklink = 'https://www.jegy.hu/articles/655/adatkezelesi-szabalyzat'
    lista, hibalista = \
        cookie.cookiebanlink(chrome,'chrome',0,'https://www.jegy.hu/',teszt1,teszt2,'cooklink',17,linkhelye,cooklink)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Regisztráció soráng gomb inaktív
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Regisztráció során gomb inaktív'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztrációs gomb inaktív-e'
    lista, hibalista = \
        regisztracio_cs.regisztraciogombinaktiv(chrome, 'chrome', 0, kornyezet, teszt1, teszt2,
                                                    'regisztinaktiv', 14,)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Regisztráció során megjelenő jogi szöveg
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    teszt1 = 'Regisztráció során megjelenő jogi szöveg'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztrációs oldalon lévő szöveg megfelelő-e'
    szoveg = 'Tudomásul veszem, hogy az InterTicket számomra releváns, személyre szabott ajánlatokat igyekszik ' \
             'összeállítani, amelyhez számos személyes adatot használ fel. Az adatkezelés szabályait az Adatkezelési Tájékoztatóban megismertem, azokat elfogadom.'
    lista, hibalista = \
        regisztracio_cs.regisztraciogcheckboxszoveg(chrome, 'chrome', 0, kornyezet, teszt1, teszt2,
                                                    'regisztcheckszoveg', 20, szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Regisztráció szövegben lévő link
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Regisztráció szövegben lévő link'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztrációs oldalon lévő jogi szövegben a link megtalálható-e.'
    link = 'https://www.jegy.hu/adatkezelesi-szabalyzat'
    szoveg = 'Adatkezelési Tájékoztatóban'
    lista, hibalista = \
        regisztracio_cs.regisztraciolinkszoveg(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'regisztszoveglink',
                                               20, szoveg, link)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Jegyhu logo működése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Jegyhu logo működése'
    teszt2 = 'Teszt során azt nézzük, hogy a főoldalon a jegy.hu logo jól működik-e'
    elem = 'newsletterLink'
    lista, hibalista = \
        kiemelt_ajanlat_cs.oldafokepvisszahoz(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'jegyhulogo', 20, elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Események számának a megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Főoldalon események számának a megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy a főoldalon az események száma a megadott értékek közé esik-e.'
    elem = '/html/body/div[1]/div[4]/div[1]/div/div/section/p[2]/a/span[1]'
    minimum = 7000
    maximum = 14000
    lista, hibalista = \
        kiemelt_ajanlat_cs.megnezprogramjegydb(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'jegyszam', 13, elem,
                                               minimum,
                                               maximum)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Jegyek számának a megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Főoldalon jegyek számának a megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy a főoldalon a jegyek száma a megadott értékek közé esik-e.'
    elem = '/html/body/div[1]/div[4]/div[1]/div/div/section/p[2]/a/span[2]'
    minimum = 6000000
    maximum = 11000000
    lista, hibalista = \
        kiemelt_ajanlat_cs.megnezprogramjegydb(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'jegyszam', 13, elem,
                                               minimum,
                                               maximum)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány linket megnéz
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány oldalon lévő link megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy az ajándékoldalon található link jól működik-e.'
    szoveg = 'Kattintson ide a további információkhoz.'
    url = 'articles/19/vasarlasi-tajekoztato#gift-card'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanylink(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'ajandeklink', 13,
                                               szoveg, url)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány linket használ majd visszajön
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány oldalról elnavigálás'
    teszt2 = 'Teszt során azt nézzük, hogy az ajándékoldalról elnavigálunk és visszatéréskor jól működik-e.'
    szoveg = 'Kattintson ide a további információkhoz.'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanyvissza(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'ajandeklinkvissza',
                                                 20,
                                                 szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel kép 1-ról
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése normál képről'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e normál képről elidulva megrendelni az ajándékutalványt'
    list = ['Válasszon', '1 000 Ft', '3 000 Ft', '5 000 Ft', '10 000 Ft', '15 000 Ft', '20 000 Ft']
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanykeprol2(chrome, 'chrome', 0, kornyezet, teszt1, teszt2,
                                                 'ajandekkeprolszuletesnap', sla_ajandekutalvany,
                                                  'Jegy.hu ajándékutalvány', list)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel kép 2-ról
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése születésnapi képről'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e születésnapi kéről elidulva megrendelni az ajándékutalványt'
    list = ['Válasszon', '1 000 Ft', '3 000 Ft', '5 000 Ft', '10 000 Ft', '15 000 Ft', '20 000 Ft']
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanykeprol2(chrome, 'chrome', 0, kornyezet, teszt1, teszt2,
                                                 'ajandekkeprolszuletesnap', sla_ajandekutalvany,
                                                  'Boldog születésnapot!', list)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel kép 3-ról
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése névnapi képről'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e névnapi kéről elidulva megrendelni az ajándékutalványt'
    lista2 = ['Válasszon', '1 000 Ft', '3 000 Ft', '5 000 Ft', '10 000 Ft', '15 000 Ft', '20 000 Ft']
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanykeprol2(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'ajandekkeprolnevnap',
                                                 sla_ajandekutalvany, 'Boldog névnapot!', lista2)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel normal, 1000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése normal, 1000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 1000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='ajandek1000ft', varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandeknormal,
                                                     varindex2=1, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel normal, 3000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése normal, 3000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 3000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='ajandek3000ft', varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandeknormal,
                                                     varindex2=2, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel normal, 5000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése normal, 5000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 5000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='ajandek5000ft', varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandeknormal,
                                                     varindex2=3, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel normal, 10000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése normal, 10000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 10000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='ajandek10000ft', varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandeknormal,
                                                     varindex2=4, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel normal, 15000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése normal, 15000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 15000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='ajandek15000ft', varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandeknormal,
                                                     varindex2=5, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel normal, 20000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése normal, 20000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 20000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='ajandek20000ft', varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandeknormal,
                                                     varindex2=6, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel születésnap, 1000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése születésnap, 1000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 1000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='szuletesnap1000ft',
                                                     varslaido=sla_ajandekutalvany, varindex1=ajandekszul,
                                                     varindex2=1, varajegynovel=1, varajegycsokkent=0)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel születésnap, 3000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése születésnap, 3000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 3000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='szuletesnap3000ft',
                                                     varslaido=sla_ajandekutalvany, varindex1=ajandekszul,
                                                     varindex2=2, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel születésnap, 5000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése népvnap, 5000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 5000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='szuletesnap5000ft',
                                                     varslaido=sla_ajandekutalvany, varindex1=ajandekszul,
                                                     varindex2=3, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel születésnap, 100000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése névnap, 10000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 10000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='szuletesnap10000ft',
                                                     varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandekszul,
                                                     varindex2=4, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel születésnap, 150000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése születésnap, 15000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 15000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='szuletesnap15000ft',
                                                     varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandekszul,
                                                     varindex2=5, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel születésnap, 20000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése születésnap, 20000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 20000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='szuletesnap20000ft',
                                                     varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandekszul,
                                                     varindex2=6, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    """    
    *****************************************************************************************
    Ajándékutalvány megrendel névnap, 1000Ft
    *****************************************************************************************    
    """
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése névnap, 1000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 1000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='nevnapi3000ft', varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandeknevnap,
                                                     varindex2=1, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel névnap, 3000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése névnap, 3000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 3000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='nevnapi3000ft', varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandeknevnap,
                                                     varindex2=2, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel névnap, 5000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése névnap, 5000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 5000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='nevnapi5000ft', varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandeknevnap,
                                                     varindex2=3, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel névnap, 10000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése névnap, 10000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 10000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='nevnapi10000ft', varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandeknevnap,
                                                     varindex2=4, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    # print(teljes_lista)
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel névnap, 15000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése névnap, 15000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 15000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(driver=chrome, varbongeszo='chome', varido=0, varurl=kornyezet,
                                                     varteszteset_neve=teszt1, varteszteset_leiras=teszt2,
                                                     varteszteset_kepek='nevnapi15000ft', varslaido=sla_ajandekutalvany,
                                                     varindex1=ajandeknevnap,
                                                     varindex2=5, varajegynovel=6, varajegycsokkent=3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány megrendel névnap, 20000Ft
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány megrendelése névnap, 20000ft'
    teszt2 = 'Teszt során azt nézzük, hogy sikerül-e megrendelni névnapi 20000ft-os ajándékutalványt'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanymegrendel3(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'nevnapi2000ft',
                                                     sla_ajandekutalvany, ajandeknevnap, 6,
                                                     6, 3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány kép3 megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    teszt1 = 'Ajándékutalvány kép3 megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy az ajándékutalvány oldalon a harmadik kép megjelenik-e'
    kepurl = 'design/img/gift_cards/boldog_nevnapot_new.jpg'
    altszoveg = 'Boldog névnapot!'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanykep(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'ajandekkep3',
                                              sla_ajandekutalvany, 2,
                                              kepurl, altszoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány kép2 megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány kép2 megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy az ajándékutalvány oldalon a második kép megjelenik-e'
    kepurl = 'design/img/gift_cards/boldog_szuletesnapot_new.jpg'
    altszoveg = 'Boldog születésnapot!'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanykep(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'ajandekkep2', 16, 1,
                                              kepurl, altszoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány kép1 megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány kép1 megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy az ajándékutalvány oldalon az első kép megjelenik-e'
    kepurl = 'design/img/gift_cards/jegyhu_ajandekutalvany_new.jpg'
    altszoveg = 'Jegy.hu ajándékutalvány'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanykep(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'ajandekkep1', 16, 0,
                                              kepurl, altszoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány kosár gomb neve
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány kosár gomb neve'
    teszt2 = 'Teszt során azt nézzük, hogy az ajándékutalvány oldalon a kosár gomb neve megfelelő-e'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvany_gombneve(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'ajandekgombnev',
                                                    16, 'kosárba rak')

    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Ajándékutalvány kosár gomja aktív lesz-e
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    teszt1 = 'Ajándékutalvány kosár gomb aktív'
    teszt2 = 'Teszt során azt nézzük, hogy az ajándékutalvány oldalon a kosár gomb aktív lesz-e'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanygombaktiv(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'gombaktív',
                                                    13)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Ajándékutalvány kosár gomjának megnézése, hogy inaktív-e
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány kosár gomb inaktív'
    teszt2 = 'Teszt során azt nézzük, hogy az ajándékutalvány oldalon a gomb inaktív-e'
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvany_gomb_inaktiv(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'gombinaktiv',
                                                        13)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Névnapi ajándékutalvány címleteinek ellenőrzése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    teszt1 = 'Névnapi ajándékutalvány címletei'
    teszt2 = 'Teszt során azt nézzük, hogy a Névnapi ajándutalvány-on belül megfelelő címletek jelennek-e meg.'
    ftlist = ['Válasszon', '1 000 Ft', '3 000 Ft', '5 000 Ft', '10 000 Ft', '15 000 Ft', '20 000 Ft']
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanyszoveg3(chrome, 'chrome', 0, 'http://www.jegy.hu/', teszt1, teszt2,
                                                  'szuletesnapcimlet', 13, ajandeknevnap, ftlist)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Születésnapi ajándékutalvány címleteinek megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Születésnapi ajándékutalvány címletei'
    teszt2 = 'Teszt során azt nézzük, hogy a Születésnapi ajándutalvány-on belül megfelelő címletek jelennek-e meg.'
    ftlist = ['Válasszon', '1 000 Ft', '3 000 Ft', '5 000 Ft', '10 000 Ft', '15 000 Ft', '20 000 Ft']
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanyszoveg3(chrome, 'chrome', 0, 'http://www.jegy.hu/', teszt1, teszt2,
                                                  'szuletesnapcimlet', 13, ajandekszul, ftlist)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Normál ajándékutalvány címleteinek megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Normál ajándékutalvány címletei'
    teszt2 = 'Teszt során azt nézzük, hogy a normál ajándutalvány-on belül megfelelő címletek jelennek-e meg.'
    ftlist = ['Válasszon', '1 000 Ft', '3 000 Ft', '5 000 Ft', '10 000 Ft', '15 000 Ft', '20 000 Ft']
    lista, hibalista = \
        ajandekutalvany_cs.ajandekutalvanyszoveg3(chrome, 'chrome', 0, 'http://www.jegy.hu/', teszt1, teszt2,
                                                  'ajandekcimlet', 13, ajandeknormal, ftlist)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Ajándékutalvány típusainak megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajándékutalvány típusainak megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy az ajándutalványnak megfelelőek-e a típusai'
    if ajandekvege > most > ajandekkezdet:
        tipusok = ['Válasszon', 'Hóember', 'Díszek', 'Télapó','Jegy.hu ajándékutalvány', 'Boldog születésnapot!', 'Boldog névnapot!']
    else:
        tipusok = ['Válasszon', 'Jegy.hu ajándékutalvány', 'Boldog születésnapot!', 'Boldog névnapot!']
    lista, hibalista = ajandekutalvany_cs.ajandekutalvanyszoveg1(chrome, 'chrome', 0, kornyezet, teszt1, teszt2,
                                                                 'ajandektipus', 20, tipusok)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''     
    *****************************************************************************************
    Hírlevél feliratkozása oldalon található 2-es tooltip megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Hírlevél feliratkozás 3-es tooltip'
    teszt2 = 'Teszt során azt nézzük, hogy a hírlevél feliratkozás oldalán található 3-es tooltip jól működik-e.'
    toolid = '//*[@id="formCustomerData"]/div/article/div[10]/div/div[2]/fieldset/div/div/div/div[1]/div[1]/div[' \
             '3]/div[2]/span'
    szoveg = 'Személyre szabott hirlevelekhez szükséges megadnia az irányítószámot.'
    lista, hibalista = \
        tooltipp_cs.tooltipp_hirlevel(driver=chrome, varbongeszo='chrome', varido=0,
                                      varurl=kornyezet,
                                      varteszteset_neve=teszt1,
                                      varteszteset_leiras=teszt2,
                                      varteszteset_kepek='hirleveltooltip3',
                                      varslaido=16,
                                      vartooltippid=toolid,
                                      vartooltippszoveg=szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Hírlevél feliratkozása oldalon található 2-es tooltip megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Hírlevél feliratkozás 2-es tooltip'
    teszt2 = 'Teszt során azt nézzük, hogy a hírlevél feliratkozás oldalán található 2-es tooltip jól működik-e.'
    toolid = '//*[@id="formCustomerData"]/div/article/div[10]/div/div[2]/fieldset/div/div/div/div[1]/div[1]/div[' \
             '2]/div[2]/span'
    szoveg = 'Ellenőrzésként adja meg újra az e-mail címet.'
    lista, hibalista = \
        tooltipp_cs.tooltipp_hirlevel(driver=chrome, varbongeszo='chrome', varido=0,
                                      varurl=kornyezet,
                                      varteszteset_neve=teszt1,
                                      varteszteset_leiras=teszt2,
                                      varteszteset_kepek='hirleveltooltip2',
                                      varslaido=16,
                                      vartooltippid=toolid,
                                      vartooltippszoveg=szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''     
    *****************************************************************************************
    Hírlevél feliratkozása oldalon található 1-es tooltip megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Hírlevél feliratkozás 1-es tooltip'
    teszt2 = 'Teszt során azt nézzük, hogy a hírlevél feliratkozás oldalán található 1-es tooltip jól működik-e.'
    toolid = '//*[@id="formCustomerData"]/div/article/div[10]/div/div[2]/ \
    fieldset/div/div/div/div[1]/div[1]/div[1]/div[2]/span'
    szoveg = 'Kérjük, adjon meg egy valódi e-mail címet! A cím létezését a rendszer megvizsgálja.'
    lista, hibalista = \
        tooltipp_cs.tooltipp_hirlevel(driver=chrome, varbongeszo='chrome', varido=0,
                                      varurl=kornyezet,
                                      varteszteset_neve=teszt1,
                                      varteszteset_leiras=teszt2,
                                      varteszteset_kepek='hirleveltooltip1',
                                      varslaido=16,
                                      vartooltippid=toolid,
                                      vartooltippszoveg=szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Új jelszó megadása oldalon található tooltip megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Új jelszónál található tooltip megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy az új jelszó megadása oldalon található tooltip jól működik-e.'
    toolid = '/html/body/div[1]/div[4]/div/form/div/div/fieldset/div/div[2]/div/div/div[2]/span'
    szoveg = 'Kérjük adja meg azt az e-mail címet, amivel regisztrált'
    lista, hibalista = \
        tooltipp_cs.tooltipp_ujjelszo(driver=chrome, varbongeszo='chrome', varido=0,
                                      varurl=kornyezet,
                                      varteszteset_neve=teszt1,
                                      varteszteset_leiras=teszt2,
                                      varteszteset_kepek='ujjelszotooltip',
                                      varslaido=16,
                                      vartooltippid=toolid,
                                      vartooltippszoveg=szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Regisztráción belül található 2-es tooltip megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Regisztráció 2-es tooltip megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztráción belül az 2-es tooltip jól működik-e.'
    toolid = '//*[@id="registration"]/div/div/fieldset/div/div[2]/div/div/div[2]/span'
    szoveg = 'A jelszónak legalább nyolc karakter hosszúságúnak kell lenni és kis-, nagybetűket, valamint számjegyet ' \
             'kell tartalmazni.'
    lista, hibalista = \
        tooltipp_cs.tooltipp_regisztracio(driver=chrome, varbongeszo='chrome', varido=0,
                                          varurl=kornyezet,
                                          varteszteset_neve=teszt1,
                                          varteszteset_leiras=teszt2,
                                          varteszteset_kepek='regisztraciotooltip2',
                                          varslaido=16,
                                          vartooltippid=toolid,
                                          vartooltippszoveg=szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Regisztráción belül található 1-es tooltip megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Regisztráció 1-es tooltip megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztráción belül az 1-es tooltip jól működik-e.'
    toolid = '//*[@id="registration"]/div/div/fieldset/div/div[1]/div/div/div[2]/span'
    szoveg = 'Kérjük adja meg az e-mail címét! A cím létezését a rendszer megvizsgálja.'
    lista, hibalista = \
        tooltipp_cs.tooltipp_regisztracio(driver=chrome, varbongeszo='chrome', varido=0,
                                          varurl=kornyezet,
                                          varteszteset_neve=teszt1,
                                          varteszteset_leiras=teszt2,
                                          varteszteset_kepek='regisztraciotooltip1',
                                          varslaido=16,
                                          vartooltippid=toolid,
                                          vartooltippszoveg=szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Nyelvválasztó ikonhoz tartozó tooltip megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó ikon tooltipp'
    teszt2 = 'Teszt során azt nézzük, hogy a nyelvválasztó tooltip-ben jó szöveg van-e'
    toolid = '//*[@id="main_lang_select2"]'
    szoveg = 'Magyar'
    lista, hibalista = tooltipp_cs.tooltipp2(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                             varteszteset_neve=teszt1,
                                             varteszteset_leiras=teszt2, varteszteset_kepek='nyelvvalasztotooltip',
                                             varslaido=16,
                                             vartooltippid=toolid,
                                             vartooltippszoveg=szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Üres kosárhoz ikonhoz tartozó tooltip megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Üres kosár ikon tooltipp'
    teszt2 = 'Teszt során azt nézzük, hogy az Üres kosárhoz tartozó tooltip-ben jó szöveg van-e'
    toolid = '//*[@id="basket_holder"]'
    szoveg = 'Üres kosár'
    lista, hibalista = tooltipp_cs.tooltipp2(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                             varteszteset_neve=teszt1,
                                             varteszteset_leiras=teszt2, varteszteset_kepek='ureskosar',
                                             varslaido=16,
                                             vartooltippid=toolid,
                                             vartooltippszoveg=szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Instagram ikonhoz tartozó tooltip megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Instagram ikon tooltipp'
    teszt2 = 'Teszt során azt nézzük, hogy az Instagram ikon-hoz tartozó tooltip-ben jó szöveg van-e'
    toolid = '//*[@id="instagramLink"]'
    szoveg = 'Instagram'
    lista, hibalista = tooltipp_cs.tooltipp2(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                             varteszteset_neve=teszt1,
                                             varteszteset_leiras=teszt2, varteszteset_kepek='instagramtooltipp',
                                             varslaido=16,
                                             vartooltippid=toolid,
                                             vartooltippszoveg=szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Hírlevél ikonhoz tartozó tooltip megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Hírlevél ikon tooltipp'
    teszt2 = 'Teszt során azt nézzük, hogy a Hírlevél ikon-hoz tartozó tooltip-ben jó szöveg van-e'
    toolid = '//*[@id="newsletterLink"]'
    szoveg = 'Hírlevél feliratkozás'
    lista, hibalista = tooltipp_cs.tooltipp2(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                             varteszteset_neve=teszt1,
                                             varteszteset_leiras=teszt2, varteszteset_kepek='tooltipp', varslaido=16,
                                             vartooltippid=toolid,
                                             vartooltippszoveg=szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Cookie megnéz
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Cookie megnézése'
    teszt2 = 'Teszt során azt nézzük, hogy a cookie rendben megjelenik-e az oldalon.'
    lista, hibalista = \
        cookie.cookie_megnez(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet, varteszteset_neve=teszt1,
                             varteszteset_leiras=teszt2, varteszteset_kepek='cookie_megjelenik', varslaido=20)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Cookie működése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Cookie működése'
    teszt2 = 'Teszt során azt nézzük, hogy a cookie működése rendben van-e. Elfogadása után nem jelenik meg újból.'
    lista, hibalista = \
        cookie.cookie_mukodese(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                               varteszteset_neve=teszt1,
                               varteszteset_leiras=teszt2, varteszteset_kepek='cookie_mukodese', varslaido=20)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Cookie szovege
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Cookie szövege'
    teszt2 = 'Teszt során azt nézzük, hogy a cookie szövege megfelelően jelenik-e meg.'
    szoveg = """Mint a legtöbb weboldal, a Jegy.hu is cookie-kat használ a működéséhez. Tudomásul veszem, hogy az InterTicket számomra releváns, személyre szabott ajánlatokat igyekszik összeállítani, amelyhez számos személyes adatot használ fel. Az adatkezelés szabályait az Adatkezelési Tájékoztatóban megismertem, azokat elfogadom."""
    lista, hibalista = \
        cookie.cookie_szovege(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet, varteszteset_neve=teszt1,
                              varteszteset_leiras=teszt2, varteszteset_kepek='cookie_szovege', varslaido=20,
                              varcookieszovege=szoveg)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    # file.close()
    '''
    *****************************************************************************************
    Nyelvválasztó Német
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó Német'
    teszt2 = 'Teszt során azt nézzük, hogy a Német nyelvválasztó jól működik-e.'

    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                         varteszteset_neve=teszt1,
                                         varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                         varnyelv=6, varszoveg='HERVORGEHOBENE ANGEBOTE',
                                         varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Nyelvválasztó alul Angol
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    teszt1 = 'Nyelvválasztó alul Angol'
    teszt2 = 'Teszt során azt nézzük, hogy az Angol nyelvválasztó alul jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto_alul(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                              varteszteset_neve=teszt1,
                                              varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                              varnyelv=1, varszoveg='FEATURED EVENTS',
                                              varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    # print(teljes_lista)

    '''
    *****************************************************************************************
    ÁSZF megnézése
    *****************************************************************************************    
    '''
    import lablec_cs

    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'ÁSZF'
    teszt2 = 'Teszt során azt nézzük, hogy az ÁSZF link rendben működik-e.'
    u0 = 'https://www.jegy.hu/articles/625/az-interticket-kft-altalanos-szerzodesi-feltetelei'
    u1 = 'https://www.jegy.hu/articles/625/az-interticket-kft-altalanos-szerzodesi-feltetelei/4'
    u2 = 'https://www.jegy.hu/articles/625/az-interticket-kft-altalanos-szerzodesi-feltetelei/3'
    u3 = 'https://www.jegy.hu/articles/625/az-interticket-kft-altalanos-szerzodesi-feltetelei/2'
    u4 = 'https://www.jegy.hu/articles/625/az-interticket-kft-altalanos-szerzodesi-feltetelei/1'
    # u5 = 'https://www.jegy.hu/articles/625/az-interticket-kft-altalanos-szerzodesi-feltetelei/1'
    lista = [u0, u1, u2, u3, u4]
    lista, hibalista = \
        lablec_cs.aszf(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet, varteszteset_neve=teszt1,
                       varteszteset_leiras=teszt2,
                       varteszteset_kepek='aszf', varslaido=40, varurllista=lista)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Adatkezelési szabályzat
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ádatkezelési szabályzat'
    teszt2 = 'Teszt során azt nézzük, hogy az adatkezelési szabályzat link jól működik-e'
    u0 = 'https://www.jegy.hu/articles/655/adatkezelesi-tajekoztato'
    u1 = 'https://www.jegy.hu/articles/655/adatkezelesi-tajekoztato/1'
    lista = [u0, u1]
    lista, hibalista = lablec_cs.tobboldallinkes(driver=chrome, varbongeszo='chrome', varido=0,
                                                 varurl=kornyezet,
                                                 varteszteset_neve=teszt1,
                                                 varteszteset_leiras=teszt2, varkeres='Adatkezelési tájékoztató',
                                                 varteszteset_kepek='adatkezelesi', varslaido=30, varurllista=lista)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Gyakori kérdések
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Gyakori kérdések'
    teszt2 = 'Teszt során azt nézzük, hogy a Gyakori kérdések link jól működik-e'
    u = 'https://www.jegy.hu/articles/349/gyakori-kerdesek'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='gyakorikerdesek', varslaido=20,
                                  vartipus=2,
                                  varhely='Gyakori kérdések', varszoveg='Gyakori kérdések', varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Vásárlási tájékoztató
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Vásárlási tájékoztató'
    teszt2 = 'Teszt során azt nézzük, hogy a Vásárlási tájékoztató link jól működik-e'
    u = 'https://www.jegy.hu/articles/19/vasarlasi-tajekoztato'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='vasarlasitajekoztato', varslaido=20,
                                  vartipus=2,
                                  varhely='Vásárlási tájékoztató', varszoveg='Vásárlási tájékoztató', varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Hirdetési lehetőség
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Hirdetési lehetőség'
    teszt2 = 'Teszt során azt nézzük, hogy a Hirdetési lehetőség link jól működik-e'
    u = 'http://www.ojt.hu/marketing#mediaajanlat'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='hirdetes', varslaido=20, vartipus=2,
                                  varhely='Hirdetési lehetőség', varszoveg='Hirdetési lehetőség', varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Kapcsolat
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Kapcsolat'
    teszt2 = 'Teszt során azt nézzük, hogy a Kapcsolat link jól működik-e'
    u = 'https://www.jegy.hu/articles/557/kapcsolat'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='kapcsolat', varslaido=20, vartipus=2,
                                  varhely='Kapcsolat', varszoveg='Kapcsolat', varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Jegypontok
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Jegypontok'
    teszt2 = 'Teszt során azt nézzük, hogy a Jegypontok link jól működik-e'
    u = 'https://www.jegy.hu/jegyirodak'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='jegypontok', varslaido=20, vartipus=2,
                                  varhely='Jegypontok', varszoveg='Jegypontok', varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Elmaradt előadások
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Elmaradt előadások'
    teszt2 = 'Teszt során azt nézzük, hogy az Elmaradt előadások link jól működik-e'
    u = kornyezet + 'cancelled'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='elmaradt', varslaido=20, vartipus=2,
                                  varhely='Elmaradt előadások', varszoveg='Elmaradt előadások', varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Széchenyi Terv
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Széchenyi Terv'
    teszt2 = 'Teszt során azt nézzük, hogy a Széchenyi Terv link jól működik-e'
    u = kornyezet + 'articles/435/uj-szechenyi-terv'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='szechenyiterv', varslaido=20,
                                  vartipus=2,
                                  varhely='Széchenyi Terv', varszoveg='Széchenyi Terv', varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    CIB fizetés - Gyakori kérdések
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'CIB fizetés - Gyakori kérdések'
    teszt2 = 'Teszt során azt nézzük, hogy a CIB fizetés - Gyakori kérdések link jól működik-e'
    u = kornyezet + 'articles/499/'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='cibfifzetes', varslaido=20,
                                  vartipus=2, varhely='CIB fizetés GYFK', varszoveg='CIB fizetés GYFK', varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
   *****************************************************************************************
   CIB - Fizetési tájékoztató
   *****************************************************************************************    
   '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'CIB - Fizetési tájékoztató'
    teszt2 = 'Teszt során azt nézzük, hogy a CIB - Fizetési tájékoztató link jól működik-e'
    u = kornyezet + 'articles/513/'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='cibfiztaj', varslaido=20,
                                  vartipus=2, varhely='CIB - Fizetési tájékoztató',
                                  varszoveg='CIB - Fizetési tájékoztató',
                                  varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Társadalmi felelősségvállalás
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Társadalmi felelősségvállalás'
    teszt2 = 'Teszt során azt nézzük, hogy a Társadalmi felelősségvállalás link jól működik-e'
    u = kornyezet + 'articles/517/trsadalmi-felelssgvllals'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='tarsadalmifel', varslaido=20,
                                  vartipus=2, varhely='Társadalmi felelősségvállalás',
                                  varszoveg='Társadalmi felelősségvállalás',
                                  varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    SuperShop programismertető
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'SuperShop programismertető'
    teszt2 = 'Teszt során azt nézzük, hogy a SuperShop programismertető link jól működik-e'
    u = kornyezet + 'articles/654/supershop-programismerteto'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='supershop', varslaido=20,
                                  vartipus=2, varhely='SuperShop programismertető',
                                  varszoveg='SuperShop programismertető',
                                  varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Oldaltérkép
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Oldaltérkép'
    teszt2 = 'Teszt során azt nézzük, hogy az Oldaltérkép link jól működik-e'
    u = kornyezet + 'sitemap'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='oldalterkep', varslaido=20,
                                  vartipus=2, varhely='Oldaltérkép', varszoveg='Oldaltérkép', varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Rólunk
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Rólunk'
    teszt2 = 'Teszt során azt nézzük, hogy a Rólunk link jól működik-e'
    u = 'http://www.interticket.com/?lang=hu'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='rólunk', varslaido=20,
                                  vartipus=2, varhely='Rólunk', varszoveg='Rólunk', varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Események Lengyelországban
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Események Lengyelországban'
    teszt2 = 'Teszt során azt nézzük, hogy az Események Lengyelországban link jól működik-e'
    u = 'https://www.interticket.pl/'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='lengyel', varslaido=20,
                                  vartipus=2, varhely='Események Lengyelországban',
                                  varszoveg='Események Lengyelországban', varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Események Szlovákiában
    *****************************************************************************************    
    '''
    # import lablec_cs
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Események Szlovákiában'
    teszt2 = 'Teszt során azt nézzük, hogy az Események Szlovákiában link jól működik-e'
    u = 'https://www.interticket.sk/'
    lista, hibalista = \
        lablec_cs.oldallinkmegnez(driver=chrome, varbongeszo='chrome', varido=0, varurl=kornyezet,
                                  varteszteset_neve=teszt1,
                                  varteszteset_leiras=teszt2, varteszteset_kepek='esemenyszlovak', varslaido=20,
                                  vartipus=2, varhely='Események Szlovákiában', varszoveg='Események Szlovákiában',
                                  varerurl=u)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Fő kiemelt megnézése
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Fő kiemelt'
    teszt2 = 'Teszt során azt nézzük, hogy a főkiemelt megfelelően működik-e.'
    lista, hibalista = \
        kiemelt_ajanlat_cs.fokiemelt(chrome, 'Chrome', 0, kornyezet, teszt1, teszt2, 'fokiemelt', 15)

    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Nyelvválasztó angol
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó angol'
    teszt2 = 'Teszt során azt nézzük, hogy az angol nyelvválasztó jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                         varteszteset_neve=teszt1,
                                         varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                         varnyelv=1, varszoveg='FEATURED EVENTS',
                                         varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Nyelvválasztó Dán
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó Dán'
    teszt2 = 'Teszt során azt nézzük, hogy a Dán nyelvválasztó jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                         varteszteset_neve=teszt1,
                                         varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                         varnyelv=2, varszoveg='UDVALGTE ARRANGEMENTER',
                                         varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Nyelvválasztó Magyar
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó Magyar'
    teszt2 = 'Teszt során azt nézzük, hogy a Magyar nyelvválasztó jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                         varteszteset_neve=teszt1,
                                         varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                         varnyelv=3, varszoveg='KIEMELT AJÁNLATAINK',
                                         varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Nyelvválasztó Szlovén
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó Szlovén'
    teszt2 = 'Teszt során azt nézzük, hogy a Szlovén nyelvválasztó jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                         varteszteset_neve=teszt1,
                                         varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                         varnyelv=4, varszoveg='ODPORÚČANÉ PODUJATIA',
                                         varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Nyelvválasztó Lengyel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó Lengyel'
    teszt2 = 'Teszt során azt nézzük, hogy a Lengyel nyelvválasztó jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                         varteszteset_neve=teszt1,
                                         varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                         varnyelv=5, varszoveg='POLECAMY',
                                         varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Nyelvválasztó Német
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó Német'
    teszt2 = 'Teszt során azt nézzük, hogy a Német nyelvválasztó jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                         varteszteset_neve=teszt1,
                                         varteszteset_leiras=teszt2, varteszteset_kepek='nyelvnemet', varslaido=20,
                                         varnyelv=6,
                                         varszoveg='HERVORGEHOBENE ANGEBOTE',
                                         varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Nyelvválasztó alul Angol
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó alul Angol'
    teszt2 = 'Teszt során azt nézzük, hogy az Angol nyelvválasztó alul jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto_alul(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                              varteszteset_neve=teszt1,
                                              varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                              varnyelv=1, varszoveg='FEATURED EVENTS',
                                              varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Nyelvválasztó alul Dán
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó alul Dán'
    teszt2 = 'Teszt során azt nézzük, hogy a dán nyelvválasztó alul jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto_alul(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                              varteszteset_neve=teszt1,
                                              varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                              varnyelv=2, varszoveg='UDVALGTE ARRANGEMENTER',
                                              varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Nyelvválasztó alul Magyar
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó alul Magyar'
    teszt2 = 'Teszt során azt nézzük, hogy a Magyar nyelvválasztó alul jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto_alul(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                              varteszteset_neve=teszt1,
                                              varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                              varnyelv=3, varszoveg='KIEMELT AJÁNLATAINK',
                                              varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Nyelvválasztó alul Szlovén
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó alul Szlovén'
    teszt2 = 'Teszt során azt nézzük, hogy a Szlovén nyelvválasztó alul jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto_alul(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                              varteszteset_neve=teszt1,
                                              varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                              varnyelv=4, varszoveg='ODPORÚČANÉ PODUJATIA',
                                              varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Nyelvválasztó alul Lengyel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó alul Lengyel'
    teszt2 = 'Teszt során azt nézzük, hogy a Lengyel nyelvválasztó alul jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto_alul(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                              varteszteset_neve=teszt1,
                                              varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                              varnyelv=5, varszoveg='POLECAMY',
                                              varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Nyelvválasztó alul Német
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Nyelvválasztó alul Német'
    teszt2 = 'Teszt során azt nézzük, hogy a Német nyelvválasztó alul jól működik-e.'
    elem = '/html/body/div[1]/div[5]/div[1]/div/div/h4'
    lista, hibalista = \
        kiemelt_ajanlat_cs.nyelvvalaszto_alul(driver=chrome, varbongeszo='Chrome', varido=0, varurl=kornyezet,
                                              varteszteset_neve=teszt1,
                                              varteszteset_leiras=teszt2, varteszteset_kepek='nyelvangol', varslaido=20,
                                              varnyelv=6, varszoveg='HERVORGEHOBENE ANGEBOTE',
                                              varelem=elem)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Regisztráió rövid jelszóval Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Regisztráció rövid jelszó'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztrációs során rövid jelszót adunk meg.'
    szoveg1 = 'Kérjük írjon legalább 8 karaktert!'
    lista, hibalista = \
        regisztracio_cs.regisztracio_rovid_jelszo2(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'regrovidjelszo', 20,
                                                   'valami@telenor.hu', '123456', szoveg1)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Regisztráió jelszó hossza 8 csak szám jelszóval Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Regisztráció jelszó hossza 8 csak szám'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztrációs során rövid jelszót adunk meg.'
    szoveg1 = 'Sikertelen regisztráció'
    szoveg2 = '''A jelszó formátuma(jelszó erőssége) nem megfelelő! A Jelszónak legalább nyolc karakter hosszúságúnak kell lenni és kis-, nagybetűket, valamint számjegyet kell tartalmazni. Kérjük, adjon meg új, megfelelő jelszót! Köszönjük!'''
    lista, hibalista = \
        regisztracio_cs.regisztracio_rosszjelszo2(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'regjohoszszam', 20,
                                                  'valami@telenor.hu', '12345678', szoveg1, szoveg2)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Regisztráió jelszó hossza 8 csak kisbetű jelszóval Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Regisztráció jelszó hossza 8 csak kisbetű'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztrációs során rövid jelszót adunk meg.'
    szoveg1 = 'Sikertelen regisztráció'
    szoveg2 = '''A jelszó formátuma(jelszó erőssége) nem megfelelő! A Jelszónak legalább nyolc karakter hosszúságúnak kell lenni és kis-, nagybetűket, valamint számjegyet kell tartalmazni. Kérjük, adjon meg új, megfelelő jelszót! Köszönjük!'''
    lista, hibalista = \
        regisztracio_cs.regisztracio_rosszjelszo2(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'csakbetu', 20,
                                                  'valami@telenor.hu', 'asdfghjk', szoveg1, szoveg2)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Regisztráió jelszó hossza 8 csak NAGYBETŰ jelszóval Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Regisztráció jelszó hossza 8 csak nagybetű'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztrációs során rövid jelszót adunk meg.'
    szoveg1 = 'Sikertelen regisztráció'
    szoveg2 = '''A jelszó formátuma(jelszó erőssége) nem megfelelő! A Jelszónak legalább nyolc karakter hosszúságúnak kell lenni és kis-, nagybetűket, valamint számjegyet kell tartalmazni. Kérjük, adjon meg új, megfelelő jelszót! Köszönjük!'''
    lista, hibalista = \
        regisztracio_cs.regisztracio_rosszjelszo2(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'csaknagybetu', 20,
                                                  'valami@telenor.hu', 'ASDFGHJK', szoveg1, szoveg2)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Regisztráió jelszó hossza 8 csak kis-, és NAGYBETŰ jelszóval Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Regisztráció jelszó hossza 8 csak kis- nagybetű'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztrációs során rövid jelszót adunk meg.'
    szoveg1 = 'Sikertelen regisztráció'
    szoveg2 = '''A jelszó formátuma(jelszó erőssége) nem megfelelő! A Jelszónak legalább nyolc karakter hosszúságúnak kell lenni és kis-, nagybetűket, valamint számjegyet kell tartalmazni. Kérjük, adjon meg új, megfelelő jelszót! Köszönjük!'''
    lista, hibalista = \
        regisztracio_cs.regisztracio_rosszjelszo2(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'kisnagybetu', 20,
                                                  'valami@telenor.hu', 'asdfghjK', szoveg1, szoveg2)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Regisztráió jelszó hossza 8 csak kisbetű és szám jelszóval Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    teszt1 = 'Regisztráció jelszó hossza 8 kisbetű, szám'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztrációs során rövid jelszót adunk meg.'
    szoveg1 = 'Sikertelen regisztráció'
    szoveg2 = '''A jelszó formátuma(jelszó erőssége) nem megfelelő! A Jelszónak legalább nyolc karakter hosszúságúnak kell lenni és kis-, nagybetűket, valamint számjegyet kell tartalmazni. Kérjük, adjon meg új, megfelelő jelszót! Köszönjük!'''
    lista, hibalista = \
        regisztracio_cs.regisztracio_rosszjelszo2(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'kisbetuszam', 20,
                                                  'valami@telenor.hu', 'asdfghj1', szoveg1, szoveg2)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Regisztráió jelszó hossza 8 csak NAGYBETŰ és szám jelszóval Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Regisztráció jelszó hossza 8 csak nagybetű és szám'
    teszt2 = 'Teszt során azt nézzük, hogy a regisztrációs során rövid jelszót adunk meg.'
    szoveg1 = 'Sikertelen regisztráció'
    szoveg2 = '''A jelszó formátuma(jelszó erőssége) nem megfelelő! A Jelszónak legalább nyolc karakter hosszúságúnak kell lenni és kis-, nagybetűket, valamint számjegyet kell tartalmazni. Kérjük, adjon meg új, megfelelő jelszót! Köszönjük!'''
    lista, hibalista = \
        regisztracio_cs.regisztracio_rosszjelszo2(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'nagybetuszam', 20,
                                                  'valami@telenor.hu', 'ASDFGHJ1', szoveg1, szoveg2)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Bejelentkezés tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Bejelentkezés'
    teszt2 = 'Teszt során azt nézzük, hogy be tudunk-e jelentkezni.'
    file = open(filelokhelye+'bejelentkezesjegyhusikeres.txt')
    emailcim = file.readline()
    jelszo = file.readline()
    file.close()
    lista, hibalista = \
        bejelent_cs.bejelent_v2(chrome, 'Chrome', 0, kornyezet, teszt1, teszt2, 'bejelentkezes', 20,
                                emailcim,
                                jelszo, 'Vincze Tamás')
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Bejelentkezés rossz jelszóval az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Bejelentkezés rossz jelszó'
    teszt2 = 'Teszt során azt nézzük, hogyha rossz jelszót adunk meg és minden jól működik'
    file = open(filelokhelye+'bejelentkezesjegyhusikertelen.txt')
    emailcim = file.readline()
    jelszo = file.readline()
    nev = file.readline()
    file.close()
    lista, hibalista = \
        bejelent_cs.bejelentrosszjelszo(chrome, 'Chrome', 0, 'https://www.jegy.hu/', teszt1, teszt2, 'bejelentkezes',
                                        20,
                                        emailcim, jelszo, nev)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Bejelentkezés nem létező loginnal az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Bejelentkezés nem létező login'
    teszt2 = 'Teszt során azt nézzük, hogyha nem létező loginnal próbálunk meg belépni.'
    file = open(filelokhelye+'bejelentkezesjegyhunemletezo.txt')
    emailcim = file.readline()
    jelszo = file.readline()
    nev = file.readline()
    file.close()
    lista, hibalista = \
        bejelent_cs.bejelentnemletezologin(chrome, 'Chrome', 0, kornyezet, teszt1, teszt2, 'bejelentkezes',
                                           20, emailcim, jelszo, nev)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    App link tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'App'
    teszt2 = 'Teszt során azt nézzük, hogy az app link működik-e.'
    lista, hibalista = \
        kiemelt_ajanlat_cs.app(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'app', 13)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Bérletek link tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Bérletek'
    teszt2 = 'Teszt során azt nézzük, hogy a Bérletek link megjelenik-e.'
    lista, hibalista = \
        kiemelt_ajanlat_cs.berletek(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'berletek', 13)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Facebook tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'facebook'
    teszt2 = 'Teszt során azt nézzük, hogy a facebbok ikon megjelenik-e felül.'

    lista, hibalista = \
        kiemelt_ajanlat_cs.facebook(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'facebook', 10)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Instagram tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Instagram'
    teszt2 = 'Teszt során azt nézzük, hogy az Instagram rendben megjelenik-e az oldalon.'
    lista, hibalista = \
        kiemelt_ajanlat_cs.instagram(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'instagram', 15)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Felső kereső tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Felső kereső'
    teszt2 = 'Teszt során azt nézzük, hogy a felső kereső működik-e az oldalon.'
    lista, hibalista = \
        kiemelt_ajanlat_cs.felsokereso(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'felso_kereso', 15, 'müpa')
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Kiemelt ajánló 1 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Kiemelt ajánlat 1'
    teszt2 = 'Teszt során azt nézzük, hogy a kiemelt ajánló 1 megjelenik-e az oldalon.'
    lista, hibalista = kiemelt_ajanlat_cs.kiemelt_ajanlat_megnezese(chrome, 'chrome', 0, kornyezet, teszt1, teszt2,
                                                                    'kiemelt1', 20, 1)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Kiemelt ajánló 2 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Kiemelt ajánlat 2'
    teszt2 = 'Teszt során azt nézzük, hogy a kiemelt ajánló 2 megjelenik-e az oldalon.'
    lista, hibalista = \
        kiemelt_ajanlat_cs.kiemelt_ajanlat_megnezese(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'kiemelt2', 20, 2)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Kiemelt ajánló 3 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Kiemelt ajánlat 3'
    teszt2 = 'Teszt során azt nézzük, hogy a kiemelt ajánló 3 megjelenik-e az oldalon.'
    lista, hibalista = kiemelt_ajanlat_cs.kiemelt_ajanlat_megnezese(chrome, 'chrome', 0, kornyezet, teszt1,
                                                                    teszt2, 'kiemelt2', 20, 3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Ajánló 1 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajánló 1'
    teszt2 = 'Teszt során azt nézzük, hogy az ajánló 1 megjelenik-e az oldalon.'
    lista, hibalista = kiemelt_ajanlat_cs.ajanlo_megnezese(chrome, 'chrome', 0, kornyezet, teszt1,
                                                           teszt2, 'ajanlo1', 20, 1)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Ajánló 2 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajánló 2'
    teszt2 = 'Teszt során azt nézzük, hogy az ajánló 2 megjelenik-e az oldalon.'
    lista, hibalista = kiemelt_ajanlat_cs.ajanlo_megnezese(chrome, 'chrome', 0, kornyezet, teszt1,
                                                           teszt2, 'ajanlo3', 20, 2)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Ajánló 3 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajánló 3'
    teszt2 = 'Teszt során azt nézzük, hogy az ajánló 3 megjelenik-e az oldalon.'
    lista, hibalista = kiemelt_ajanlat_cs.ajanlo_megnezese(chrome, 'chrome', 0, kornyezet, teszt1,
                                                           teszt2, 'ajanlo3', 20, 3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Ajánló 4 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajánló 4'
    teszt2 = 'Teszt során azt nézzük, hogy az ajánló 4 megjelenik-e az oldalon.'
    lista, hibalista = kiemelt_ajanlat_cs.ajanlo_megnezese(chrome, 'chrome', 0, kornyezet, teszt1,
                                                           teszt2, 'ajanlo4', 20, 4)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Ajánló 5 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''

    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajánló 5'
    teszt2 = 'Teszt során azt nézzük, hogy az ajánló 5 megjelenik-e az oldalon'
    chrome2 = bongeszo.chrome_inditasa()
    lista, hibalista = kiemelt_ajanlat_cs.ajanlo_megnezese(chrome2, 'chrome', 0, kornyezet, teszt1, teszt2, 'ajanlo5',
                                                           20, 5)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Ajánló 6 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajánló 6'
    teszt2 = 'Teszt során azt nézzük, hogy az ajánló 6 megjelenik-e az oldalon.'
    lista, hibalista = kiemelt_ajanlat_cs.ajanlo_megnezese(chrome, 'chrome', 0, kornyezet, teszt1,
                                                           teszt2, 'ajanlo6', 20, 6)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Ajánló 7 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajánló 7'
    teszt2 = 'Teszt során azt nézzük, hogy az ajánló 7 megjelenik-e az oldalon.'
    lista, hibalista = kiemelt_ajanlat_cs.ajanlo_megnezese(chrome, 'chrome', 0, kornyezet, teszt1,
                                                           teszt2, 'ajanlo7', 20, 7)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Ajánló 8 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajánló 8'
    teszt2 = 'Teszt során azt nézzük, hogy az ajánló 8 megjelenik-e az oldalon.'
    lista, hibalista = kiemelt_ajanlat_cs.ajanlo_megnezese(chrome, 'chrome', 0, kornyezet, teszt1,
                                                           teszt2, 'ajanlo8', 20, 8)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Ajánló 9 tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Ajánló 9'
    teszt2 = 'Teszt során azt nézzük, hogy az ajánló 9 megjelenik-e az oldalon.'
    lista, hibalista = kiemelt_ajanlat_cs.ajanlo_megnezese(chrome, 'chrome', 0, kornyezet, teszt1,
                                                           teszt2, 'ajanlo9', 20, 9)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Kereső összes tesztelése az oldalon Chrome böngészővel
    *****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Kereső összes választó'
    teszt2 = 'Teszt során azt nézzük, hogy az összes kereső működik-e'
    # lista, hibalista = kereso_cs.kereso_osszes(chrome,'chrome',0,kornyezet,teszt1,teszt2,'kereso_osszes', 14, True)
    lista, hibalista = kereso_cs.ujosszes(chrome, 'chrome', 0, kornyezet, teszt1, teszt2, 'kereso_osszes', 14, True)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Kereső első az oldalon
    ****************************************************************************************
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Kereső első választó'
    teszt2 = 'Teszt során azt nézzük, hogy az első kereső működik-e'
    lista, hibalista = \
        kereso_cs.kereso_elso(chrome, 'Chrome', 0, kornyezet, teszt1, teszt2, 'kereso_elso', 12, 1, True)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))
    '''
    *****************************************************************************************
    Kereső masodik az oldalon
    ****************************************************************************************
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Kereső masodik választó'
    teszt2 = 'Teszt során azt nézzük, hogy a masodik kereső működik-e'
    lista, hibalista = \
        kereso_cs.kereso_masodik(chrome, 'Chrome', 0, kornyezet, teszt1, teszt2, 'kereso_masodik', 12, 1,
                                 True)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    *****************************************************************************************
    Kereső harmadik az oldalon
    ****************************************************************************************
    '''
    chrome = bongeszo.chrome_inditasa()
    # firefox = bongeszo.firefox_inditasa()
    teszt1 = 'Kereső harmadik választó'
    teszt2 = 'Teszt során azt nézzük, hogy a harmadik kereső működik-e'
    lista, hibalista = \
        kereso_cs.kereso_harmadik(chrome, 'Chrome', 0, kornyezet, teszt1, teszt2, 'kereso_harmadik', 12, 1,
                                  True)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file.writelines(csv_keszito(teljes_lista))

    '''
    ****************************************************************************************
    Hírlevél feliratkozás megnézése felül, hogy egy még nem feliratkozott email címet adunk meg.
    ****************************************************************************************    
    '''
    chrome = bongeszo.chrome_inditasa()
    url = 'https://www.jegy.hu'
    teszteset_nev = 'Hírlevél feliratkozas felül'
    teszteset_leiras = 'A teszt során azt nézzük meg, hogy a felül a hírlevél feliratkozás működik-e.'
    teszteset_nevkepek = 'hirlevel_felul_jo'
    email = 'scvinyo9@gmail.com'
    irszam = '1144'
    vnev = 'Vincze'
    knev = 'Tamás'
    lista, hibalista = \
        hirlevel_cs.hirlevel_feliratkozas_felulv2(chrome, 'chrome', 0, kornyezet, teszteset_nev, teszteset_leiras,
                                                  teszteset_nevkepek, 12,
                                                  email, irszam, vnev, knev, 'valami', 'valami2', 'valami3')
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    file.writelines(csv_keszito(teljes_lista))
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2

    '''
    ***********************************************************************************
    Hírlevél feliratkozás megnézése, hogy foglalt emailt adunk meg FELÜL
    ***********************************************************************************
    '''
    chrome = bongeszo.chrome_inditasa()
    teszteset_nev = 'Hírlevél feliratkozás foglalt felul'
    teszteset_leiras = 'Teszt során azt nézzük, hogy a hírlevél feliratkozás oldalon, foglalt emailt címet adunk meg.'
    tesztesetnevk = 'hirlevel_foglalt'
    email = 'scvinyo@gmail.com'
    irszam = '1144'
    vnev = 'Vincze'
    knev = 'Tamás'
    lista, hibalista =\
        hirlevel_cs.hirlevel_feliratkozas_foglalt_felulv2(chrome, 'chrome', 0, kornyezet, teszteset_nev,
                                                          teszteset_leiras, tesztesetnevk, 15, email, irszam, vnev, knev,
         'tool1', 'tool2', 'tool3')
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    file.writelines(csv_keszito(teljes_lista))
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    '''
    ***********************************************************************************
    Hírlevél feliratkozás alul, hogy helyes email címet adunk meg
    ***********************************************************************************
    '''
    chrome = bongeszo.chrome_inditasa()
    teszteset_nev = 'Hírlevél feliratkozás alul'
    teszteset_leiras = 'Teszt során azt nézzük, hogy a hírlevél feliratkozás során, a jegy.hu-n, alul helyesn email címet adunk meg.'
    tesztesetnevk = 'hirlevel_alul'
    email = 'scvinyo10@gmail.com'
    irszam = '1144'
    vnev = 'Vincze'
    knev = 'Tamás'
    lista, hibalista = \
        hirlevel_cs.hirlevel_feliratkozas_alul(chrome, 'chrome', 0, kornyezet, teszteset_nev, teszteset_leiras,
                                               tesztesetnevk, 15, email, irszam, vnev, knev,
         'tool1', 'tool2', 'tool3')
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    file.writelines(csv_keszito(teljes_lista))
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2

    '''
    ************************************************************************************
    Hírlevél feliratkozás megnézése alul, hogy foglalt email címet adunk meg.
    ************************************************************************************
    '''
    chrome = bongeszo.chrome_inditasa()
    email = 'scvinyo@gmail.com'
    teszteset_nev = 'Hirlevel_foglalt_alul'
    teszteset_leiras = 'Teszt során azt nézzük, hogy foglalt email címmel próbálunk alul feliratkozni.'

    lista, hibalista = \
        hirlevel_cs.hirlevel_foglalt_alulv2(chrome, 'chrome', 0, kornyezet, teszteset_nev, teszteset_leiras,
                                            'hirlevel_foglalt_alul', 16, email)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    file.writelines(csv_keszito(teljes_lista))
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    '''
    ******************************************************************************
    TOP10-es megnézése
    ******************************************************************************
    '''
    chrome = bongeszo.chrome_inditasa()
    teszteset_nev = 'TOP10 megnézése'
    teszteset_leiras = 'Teszt során azt nézzük, hogy a TOP10-es lista megjeleneik-e'
    lista, hibalista = \
        top10_select.top10v2(chrome, 'chrome', 0, kornyezet, teszteset_nev, teszteset_leiras, 'top10', 6)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    file.writelines(csv_keszito(teljes_lista))
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    '''
    ******************************************************************************
    TOP10-es select 1-es tesztet futtatjuk.
    ******************************************************************************
    '''
    chrome = bongeszo.chrome_inditasa()
    teszteset_nev = 'TOP10 színház'
    teszteset_leiras = 'A TOP10-es listában azt nézzük meg, hogy a színház lista működik-e.'
    lista, hibalista = \
        top10_select.top10selectv2(chrome, 'chrome', 0, kornyezet, teszteset_nev, teszteset_leiras, 'top10select1', 15,
                                   1)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    file.writelines(csv_keszito(teljes_lista))
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2

    '''
    ******************************************************************************
    TOP10-es select 2-es tesztet futtatjuk.
    ******************************************************************************
    '''
    chrome = bongeszo.chrome_inditasa()
    teszteset_nev = 'TOP10 koncert, zene'
    teszteset_leiras = 'A TOP10-es listában azt nézzük meg, hogy a koncert, zene lista működik-e.'
    lista, hibalista = \
        top10_select.top10selectv2(chrome, 'chrome', 0, kornyezet, teszteset_nev, teszteset_leiras,
                                   'top10select2', 15, 2)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    file.writelines(csv_keszito(teljes_lista))
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2

    '''
    ******************************************************************************
    TOP10-es select 3-es tesztet futtatjuk.
    ******************************************************************************
    '''
    chrome = bongeszo.chrome_inditasa()
    teszteset_nev = 'TOP10 fesztival zene'
    teszteset_leiras = 'A TOP10-es listában azt nézzük meg, hogy a fesztival zene lista működik-e.'
    lista, hibalista = \
        top10_select.top10selectv2(chrome, 'chrome', 0, kornyezet, teszteset_nev, teszteset_leiras,
                                   'top10select3', 15, 3)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    file.writelines(csv_keszito(teljes_lista))
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)

    emailszoveg = emailszoveg + szoveg2

    '''
    ******************************************************************************
    TOP10-es select 4-es tesztet futtatjuk.
    ******************************************************************************
    '''
    chrome = bongeszo.chrome_inditasa()
    teszteset_nev = 'TOP10 múzeum kiállítás'
    teszteset_leiras = 'A TOP10-es listában azt nézzük meg, hogy a múzeum, kiállítás lista működik-e.'
    lista, hibalista = \
        top10_select.top10selectv2(chrome, 'chrome', 0, kornyezet, teszteset_nev, teszteset_leiras,
                                   'top10select4', 15, 4)
    tesztesetek = seged_cs.lista_mod(tesztesetek, lista[3])
    teljes_lista = lista + hibalista
    file.writelines(csv_keszito(teljes_lista))
    szoveg2 = gyakorlat.tabalazat_sora(teljes_lista)
    emailszoveg = emailszoveg + szoveg2
    file = open(filelokhelye+'emailkuldes_login.txt')
    emailcim = file.readline()
    jelszo = file.readline()
    file.close()
    gyakorlat.send_email2(emailcim, jelszo,
                          emaillista, str(tesztesetek[0]) + '/' + str(tesztesetek[1]) + '/' + str(tesztesetek[2]),
                          seged_cs.emailosszerak(tesztesetek, emailszoveg))
    file.close()
    # import requests
    post_fields = {'address': 'scvinyo9%40gmail.com'}
    r = requests.post('https://www.jegy.hu/admin/newsletter/unsubscribe', data=post_fields)
    print(r.status_code, r.reason)
    print(r.text)
    post_fields = {'address': 'scvinyo10%40gmail.com'}
    r = requests.post('https://www.jegy.hu/admin/newsletter/unsubscribe', data=post_fields)
    print(r.status_code, r.reason)
    print(r.text)
