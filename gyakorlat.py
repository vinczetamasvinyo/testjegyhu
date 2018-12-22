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
    alkonyvtar = teszteset_neve+'_'+ido
    os.makedirs(alkonyvtar)
    os.chdir(alkonyvtar)
    return path+'/'+alkonyvtar

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
        server.sendmail(FROM, TO, TEXT)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")

def send_email2(user, pwd, recipient, subject, body):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    TO = recipient if type(recipient) is list else [recipient]
    COMMASPACE = ', '
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = COMMASPACE.join(recipient)
    #msg['To'] = recipient

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
      <head></head>
      <body>
        <table border 1px solid black;>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td> 
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td> 
    <td>94</td>
  </tr>
</table>
        
      </body>
    </html>
    """
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(body, 'html')

    msg.attach(part1)
    msg.attach(part2)

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
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")


def send_email3(user, pwd, recipient, subject, body):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    TO = recipient if type(recipient) is list else [recipient]
    COMMASPACE = ', '
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = COMMASPACE.join(recipient)
    # msg['To'] = recipient

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
      <head></head>
      <body>
        <table border 1px solid black;>
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td> 
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td> 
    <td>94</td>
  </tr>
</table>

      </body>
    </html>
    """
    # Record the MIME types of both parts - text/plain and text/html.
    # part1 = MIMEText(text, 'plain')
    part1 = MIMEText(body, 'plain')
    # part2 = MIMEText(body, 'html')

    msg.attach(part1)
    # msg.attach(part2)

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
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")


szoveg = """\
    <html>
      <head></head>
      <body>
        <table border 1px solid black;>
  <tr><th>Firstname</th><th>Lastname</th><th>Age</th></tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td> 
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td> 
    <td>94</td>
  </tr>
</table>
        
      </body>
    </html>
    """
szoveg1 = """\
    <html>
      <head></head>
      <body>
        <table border 1px solid black;>
        <tr>
            <th>Teszteset neve</th>
            <th width="300">Teszteset leírása</th> 
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
        </tr>
        """
szoveg3 = """</table>        
      </body>
    </html>
    """

def tabalazat_sora(varlista):
    if varlista[3] == "Sikertelen":
        sor = "<tr bgcolor=\"#FF0000\">"
    else:
        sor = "<tr>"
    for i in varlista:
        sor = sor + "<td>" + i + "</td>"
    sor = sor + "</tr>"
    return sor