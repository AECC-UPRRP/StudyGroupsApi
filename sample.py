from app import db, StudyGroup

group = StudyGroup("Los chamas", "9/may/2015", "9/may/2015", "Frente a CCOM", "API", "Julio", "7871234567", "julio@example.com", "Esto esta bueno")

db.session.add(group)
db.session.commit()