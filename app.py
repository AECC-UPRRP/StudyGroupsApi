from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)


class StudyGroup(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	starting_date = db.Column(db.String(20))
	end_date = db.Column(db.String(20))
	place = db.Column(db.String(80))
	course_description  = db.Column(db.String(140))
	cordinator_name = db.Column(db.String(40))
	cordinator_phone = db.Column(db.String(10))
	cordinator_email = db.Column(db.String(80))
	comments = db.Column(db.String(140)) 

	def __init__(self, title, starting_date, end_date, place, course_description, cordinator_name, cordinator_phone, cordinator_email, comments):
		self.title = title
		self.starting_date = starting_date 
		self.end_date = end_date
		self.place = place
		self.course_description  = course_description
		self.cordinator_name = cordinator_name
		self.cordinator_phone = cordinator_phone
		self.cordinator_email = cordinator_email
		self.comments = comments
  
  	def __repr__(self):
  		return '<StudyGroup> %s' % self.title

  	def asdict(self):
  		return self.__dict__


@app.route('/')
def hello():
	return "The API is at <a href='/groups'>/groups</a>"

@app.route('/groups', methods=['GET', 'POST'])
def groups():
	if request.method == 'POST':
	    groupJson = request.get_json(force=True)
	    newGroup = StudyGroup(groupJson['title'], groupJson['starting_date'], groupJson['end_date'], groupJson['place'], groupJson['course_description'], groupJson['cordinator_name'], groupJson['cordinator_phone'], groupJson['cordinator_email'], groupJson['comments'])
	    db.session.add(newGroup)
	    db.session.commit()
	groups = StudyGroup.query.all()
	realGroups = []
  	for group in groups:
  		group = group.asdict()
  		group.pop('_sa_instance_state', None)
  		realGroups.append(group)
  	return jsonify({"groups": realGroups})


if __name__ == '__main__':
	app.run(debug=True)