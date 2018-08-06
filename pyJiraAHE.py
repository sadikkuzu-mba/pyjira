## https://www.linkedin.com/in/sadikkuzu/
#
# https://pypi.python.org/pypi/jira/
# http://jira.readthedocs.io/en/master/examples.html
# w/ https://www.youtube.com/watch?v=xnKhsTXoKCI
# http://stackoverflow.com/questions/30168387/python-jira-return-the-content-of-a-filter
#

import JiraAHE
from getpass import getpass
from unicodedata import normalize

linkJ = "https://aheinsis.atlassian.net/browse/"

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


jahe = JiraAHE.getJiraAHEobj()
if jahe is None:
    exit()

TESTflag = False
TESTset = set([])
TESTissues = jahe.search_issues("filter=14408 ORDER BY updated DESC")
if len(TESTissues)>0:
    TEST = TESTissues[0]
    TESTtime = TEST.fields.updated
    TESTset.add(IssText(TEST))
    TESTflag = True

BAflag = False
BAset = set([])
BAissues = jahe.search_issues("filter=14409 ORDER BY updated DESC")
if len(BAissues)>0:
    BA = BAissues[0]
    BAtime = BA.fields.updated
    BAset.add(IssText(BA))
    BAflag = True

if __name__ == "__main__":
    print "Test:",
    print TESTset
    print "BA:",
    print BAset
    if TESTflag and IssText(TEST) not in TESTset:
        print "Test: ",
        print IwL(TEST)
        TESTset.add(str(TEST))
    if BAflag and IssText(BA) not in BAset:
        print "BA: ",
        print IwL(BA)
        BAset.add(str(BA))
