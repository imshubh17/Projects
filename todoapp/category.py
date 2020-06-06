from app import db, TodoList
catName = 'Default'
cat1 = TodoList(catName)          
#cat1.name = "Default"
db.session.add(cat1)
db.session.commit()