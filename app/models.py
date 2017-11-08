from . import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


class BlogPost(db.Model):
	'''
	class that creates object for a blog post
	'''
	__tablename__ = 'posts'

	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String)
	post = db.Column(db.String)
	date_posted = db.Column(db.DateTime,default=datetime.utcnow)

	def save_BlogPost(self):
		'''
		function that saves the blog post to the db
		'''
		db.session.add(self)
		db.session.commit()

	@classmethod
	def get_BlogPost(cls):
		'''
		function that gets a list of all the blog posts on the db
		'''
		list_of_blogs = BlogPost.query.all()
		return list_of_blogs		

	@classmethod
	def delete_BlogPost(cls,BlogPost_id):
		'''
		function that deletes  a blog post from the db
		'''
		delete_blog = BlogPost.query.filter_by(id=BlogPost_id).delete()
		db.session.commit()


