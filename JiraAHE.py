from jira import JIRA
from getpass import getpass

username = "skuzu@anadoluhayat.com.tr"
password = "SadikKUZU#1"  # Number1 as usual;)
urlJ = "https://aheinsis.atlassian.net/"

def getText(txt):
    try:
        ret = getpass(txt + " >> ")
    except:
        ret = None
    return ret

def cls(nL=50): # number of lines
    print "\n"*int(nL)

def getJiraAHEobj():
    try:
        global username
        global password
        username = getText("username")
        password = getText("password")
        cls()
        jahe = JIRA(urlJ, basic_auth=(username, password))
        return jahe
    except:
        return None
