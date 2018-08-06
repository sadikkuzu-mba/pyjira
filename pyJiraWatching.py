import JiraAHE

jahe = JiraAHE.getJiraAHEobj()
if jahe is None:
    exit()

# UnWatched and wanted to be Watched issues
UWlist = jahe.search_issues("filter=14415")  # filter = 14407 AND watcher != currentUser() ORDER BY updated DESC
print len(UWlist)
for uw in UWlist:
    print str(uw)
    jahe.add_watcher(uw, jahe.current_user())