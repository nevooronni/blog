from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
	'''
	form for post our blog post
	'''
	name = StringField("Blog Name",validators = [required])
	content = TextAreaField('Content')
	submit = SubmitField('Submit')

	