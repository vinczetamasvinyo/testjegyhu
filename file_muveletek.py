def kepekhez_konyvtarat(teszteset_neve, kepek_path='c:/kepek/kepek/'):
    """
    Létrehozza és beállítja a könyvtárstruktúrát ahova a teszteset során a képeket készít a teszteset.
    :param teszteset_neve: Teszteset neve amihez a képeket készíti majd a program. Ez a név belekerül a könyvtárnévbe.
    :param kepek_path: Képek készítésének a foldere. Ha nem adjuk meg, akkor az alapérték c:/kepek/kepek
    :return: A függvény visszaadja a létrehozott könyvtár elérési útját.
    """
    import time
    import os
    import datetime
    path = kepek_path + datetime.date.today().strftime("%Y_%m_%d")
    ido = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
    if os.path.exists(path) != True:
        os.makedirs(path)
    os.chdir(path)
    alkonyvtar = teszteset_neve + '_' + ido
    os.makedirs(alkonyvtar)
    os.chdir(alkonyvtar)
    return path + '/' + alkonyvtar