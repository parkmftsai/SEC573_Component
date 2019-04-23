import sqlite3
db = sqlite3.connect("./History")
for eachrow in db.execute("SELECT urls.id, urls.url,urls.title,urls.visit_count,urls.typed_count,urls.last_visit_time,urls.hidden FROM urls,visits WHERE urls.id=visits.url;"):
   print(eachrow)

