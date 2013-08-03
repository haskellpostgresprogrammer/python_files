import umarutils as u
import imaplib

def login():
    IMAP_SERVER='imap.gmail.com'
    IMAP_PORT=993
    m = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    m.login(u.getpass[0], u.getpass[1])
    return m

def logout(m):
    m.logout()

def send(m,data):
    m.send(data)
    return m
