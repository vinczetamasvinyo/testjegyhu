def edge_inditasa(varutvonal='C:\python\selenium\webdriver\edge\MicrosoftWebDriver2.exe'):
    """
    Inicializálja az EDGE böngészőt, így ezt később lehet használni a műveletek során.
    :param varutvonal: A MicrosoftWebDriver.exe elérési útvonala. Ez szükséges, hogy el tudjuk indítani az EDGE-t.
    :return: Visszaadja az EDGE inicializált driverét.
    """
    from selenium import webdriver
    var_driver = webdriver.Edge(varutvonal)
    return var_driver


def chrome_inditasa(varutvonal='C:\python\selenium\webdriver\chrome7\chromedriver.exe', varfelbontas = False):
    """
    Inicializálja a Chrome böngészőt, így ezt később lehet használni a műveletek során.
    :param varutvonal: A Chrome driver elérési útvonala. Ez szükséges, hogy el tudjuk indítani a chrome böngészőt.
    :return: Visszaadja a Chrome inicializált driverét.
    """
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    options = Options()
    if varfelbontas:
        options.add_argument("window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")
        # options.add_argument("--start-fullscreen")
    # options.add_argument("ignore-certificate-errors")
    # utoljára tesztem bele 2018.07.24
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('disable-infobars')
    # options.add_argument("--verbose",""--log-path=D:\\qc1.log")
    var_driver = webdriver.Chrome(varutvonal, chrome_options=options)
    # var_driver = webdriver.Chrome(varutvonal,service_args=["--verbose", "--log-path=D:\\qc1.log"])
    # var_driver = webdriver.Chrome(varutvonal)
    return var_driver


def firefox_inditasa():
    """
    Inicializálja a Firefox böngészőt, így ezt később lehet használni a műveletek során.

    :return: Visszaadja a Chrome inicializált driverét.
    """
    from selenium import webdriver
    # var_driver = webdriver.Firefox(executable_path="C:\python\selenium\geckodriver2\geckodriver.exe")
    var_driver = webdriver.Firefox()
    # var_driver.get('https://www.jegy.hu')
    return var_driver