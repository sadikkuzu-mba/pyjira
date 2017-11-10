## https://www.linkedin.com/in/sadikkuzu/
#
# https://pypi.python.org/pypi/jira/
# http://jira.readthedocs.io/en/master/examples.html
# w/ https://www.youtube.com/watch?v=xnKhsTXoKCI
# http://stackoverflow.com/questions/30168387/python-jira-return-the-content-of-a-filter
#

import jira
# import postaci

username = "skuzu@anadoluhayat.com.tr"
password = "SadikKUZU#1" # Number1 as usual;)
urlJ = "https://aheinsis.atlassian.net/"
linkJ = "https://aheinsis.atlassian.net/browse/"

def cls(nL=50): # number of lines
    print "\n"*int(nL)

def getText(txt):
    try:
        ret = input(txt + " >> ")
    except:
        ret = None
    return ret

def IwL(id): # IssueWithLink
    id = str(id)
    link = "<a href='"+linkJ+id+"' target=_blank>"+id+"</a>"
    return link


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

TESTset.add(str(TEST))
BAset.add(str(BA))

if __name__ == "__main__":
    print "Test:",
    print TESTset
    print "BA:",
    print BAset
    if str(TEST) not in TESTset:
        print "Test: ",
        print IwL(TEST)
        TESTset.add(str(TEST))
        # postaci.postala(str(TEST), IwL(TEST))
    if str(BA) not in BAset:
        print "BA: ",
        print IwL(BA)
        BAset.add(str(BA))
        # postaci.postala(str(BA), IwL(BA))
