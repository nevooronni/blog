from app import create_app,db
from flask_script import Manager,Server
from app.models import BlogPost
from flask_migrate import Migrate,MigrateCommand

app = create_app('development')

manager = Manager(app)#inititalize extension
migrate = Migrate(app,db)#initialize extension
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

@manager.command
def test():
	"""Run the unit tests."""
	import unittest
	tests = unittest.TestLoader().discover('tests')#loads the tests
	unittest.TextTestRunner(verbosity=2).run(tests)#runs the tests

@manager.shell
def make_shell_context():
	return dict(app = app,db = db,BlogPost = BlogPost)

if __name__ == '__main__':
	manager.run()
