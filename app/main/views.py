from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from .. import db
from .froms import BlogForm,commentForm
from . import main
from ..models import User,BlogPost
import markdown2

@main.route('/')
def index():
	'''
	route that displays the blogpost
	'''
	blog_posts = BlogPost.get_BlogPost()
	title = 'iBlogger'
	return render_template('index.html',title = title,blog_posts = blog_posts)
