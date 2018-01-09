## https://www.linkedin.com/in/sadikkuzu/
#
# https://pypi.python.org/pypi/jira/
# http://jira.readthedocs.io/en/master/examples.html
# w/ https://www.youtube.com/watch?v=xnKhsTXoKCI
# http://stackoverflow.com/questions/30168387/python-jira-return-the-content-of-a-filter
#

import jira
from getpass import getpass
from unicodedata import normalize

username = "skuzu@anadoluhayat.com.tr"
password = "SadikKUZU#1" # Number1 as usual;)
urlJ = "https://aheinsis.atlassian.net/"
linkJ = "https://aheinsis.atlassian.net/browse/"

def cls(nL=50): # number of lines
    print "\n"*int(nL)

def getText(txt):
    try:
        ret = getpass(txt + " >> ")
    except:
        ret = None
    return ret

def IwL(id): # IssueWithLink
    id = str(id)
    link = "<a href='"+linkJ+id+"' target=_blank>"+id+"</a>"
    return link

def IssText(Iss): # issue id and summary
    return str(Iss)+" - "+str(Iss.fields.updated)+" - "+normalize('NFKD', Iss.fields.summary).encode('ascii','ignore')
    #return str(Iss)+" - "+str(Iss.fields.summary)

def IssDetails(Iss): # issue details
    print str(Iss)
    print Iss.fields.summary
    print "assignee:",
    print Iss.fields.assignee.displayName
    print "creator:",
    print Iss.fields.creator.displayName
    print "created: "+str(Iss.fields.created)
    print "updated: "+str(Iss.fields.updated)

try:
    username = getText("username")
    password = getText("password")
    cls()

    jahe = jira.JIRA(urlJ,basic_auth=(username,password))
except:
    exit()

TEST = jahe.search_issues("filter=11803 ORDER BY updated DESC")[0]
TESTtime = TEST.fields.updated

BA = jahe.search_issues("filter=12100 ORDER BY updated DESC")[0]
BAtime = BA.fields.updated

TESTset = set([])
BAset = set([])

TESTset.add(IssText(TEST))
BAset.add(IssText(BA))

if __name__ == "__main__":
    print "Test:",
    print TESTset
    print "BA:",
    print BAset
    if IssText(TEST) not in TESTset:
        print "Test: ",
        print IwL(TEST)
        TESTset.add(str(TEST))
    if IssText(BA) not in BAset:
        print "BA: ",
        print IwL(BA)
        BAset.add(str(BA))
