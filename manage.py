from app import create_app,db
from flask_script import Manager,Server
from app.models import BlogPost

app = create_app('development')

@manager.shell
def make_shell_context():
	return dict(app = app,db = db,BlogPost = BlogPost)

if __name__ == '__main__':
	manager.run()
