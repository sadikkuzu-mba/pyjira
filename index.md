---
layout: default
---

* * * 

[JQLs for AFP](https://github.com/sadikkuzu-mba/pyJiraAHE/blob/master/JQLs_for_AFP.md#jqls-for-afp)

**Open issues (AFP) - Test**
```
project = AHEFENPROD AND status = "To Do" AND filter = 14413 ORDER BY duedate ASC
```

**FilterHelper14413**
```
assignee in (..test users one by one..)
```

* * * 

 [pyJiraAHE.py](https://github.com/sadikkuzu-mba/pyJiraAHE/blob/master/pyJiraAHE.py) 
```python
import jira

# ...

jahe = jira.JIRA(urlJ,basic_auth=(username,password))

TEST = jahe.search_issues("filter=11803 ORDER BY updated DESC")[0]

# ...
```

* * * 
