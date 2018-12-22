def cookiemegnyom(driver, megnyom=True):
    if megnyom:
        try:
            cookie = driver.find_element_by_css_selector('a.button.accept_cookie')
            cookie.click()
        except:
            print('nincs cooki')

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

def lista_osszerak(varteszteset_neve, varteszteset_leiras, varurl, vareredmeny, varbongeszo,
                   varkezdet, varvege, vartime, varkepekhelye):
    try:
        varvisszaad = []
        varvisszaad.append(varteszteset_neve)
        varvisszaad.append(varteszteset_leiras)
        varvisszaad.append(varurl)
        varvisszaad.append(vareredmeny)
        varvisszaad.append(varbongeszo)
        varvisszaad.append(varkezdet.strftime("%Y.%m.%d %H:%M:%S.%f"))
        varvisszaad.append(varvege.strftime("%Y.%m.%d %H:%M:%S.%f"))
        varvisszaad.append(str(varvege-varkezdet))
        varvisszaad.append(str(vartime))
        if len(varkepekhelye) > 0:
            varvisszaad.append(varkepekhelye)
    except:
        pass
    finally:
        return varvisszaad
def lista_osszerakv2(varteszteset_neve, varteszteset_leiras, varurl, vareredmeny, varbongeszo,
                   varkezdet, varvege, vartime, vartisztafutasiido, varslaido, varkepekhelye):
    try:
        varvisszaad = []
        varvisszaad.append(varteszteset_neve)
        varvisszaad.append(varteszteset_leiras)
        varvisszaad.append(varurl)
        varvisszaad.append(vareredmeny)
        varvisszaad.append(varbongeszo)
        varvisszaad.append(varkezdet.strftime("%Y.%m.%d %H:%M:%S.%f"))
        varvisszaad.append(varvege.strftime("%Y.%m.%d %H:%M:%S.%f"))
        varvisszaad.append(str(varvege-varkezdet))
        varvisszaad.append(str(vartime))
        varvisszaad.append(str(vartisztafutasiido))
        varvisszaad.append(str(varslaido))
        if len(varkepekhelye) > 0:
            varvisszaad.append(varkepekhelye)
    except:
        pass
    finally:
        return varvisszaad


def kepet_keszit(driver, varkepnev, varkepsorszama, vartimestamp=True):
    """
    :rtype: object
    :param driver: 
    :param varkepnev: String. A képek nevét tartalmazza. 
    :param varkepsorszama: Szám. A képek sorszám indexét tartalmazza.
    :param vartimestamp: Boolen. Kell-e a képekhez a timestamp.
    :return: 
    """
    import datetime    
    try:
        if vartimestamp:
            ido = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            kep = varkepnev+str(varkepsorszama)+ '_' + ido + '.png'
        else:
            kep = varkepnev+str(varkepsorszama) + '.png'
        driver.get_screenshot_as_file(kep)
    except:
        pass


def lista_mod(lista,szoveg):
    lista[0]= lista[0]+1
    if szoveg == 'Sikeres':
        lista[1]=lista[1]+1
    else:
        lista[2]=lista[2]+1
    return lista

def emailosszerak(lista, tablazat):
    szoveg1 = """\
            <html>
              <head></head>
              <body>"""
    szoveg2 = "Összes teszteset száma: " + str(lista[0]) + "<br>"
    szoveg3 = "Sikeres tesztek száma: " + str(lista[1]) + "<br>"
    szoveg4 = "Sikertelen tesztek száma: " + str(lista[2]) + "<br><br>"
    szoveg5 = """
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
    szoveg6 ="""</table>        
          </body>
        </html>
        """
    return szoveg1+szoveg2+szoveg3+szoveg4+szoveg5+tablazat+szoveg6


