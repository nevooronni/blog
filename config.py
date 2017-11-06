import os

class Congig:
	'''
	parent configuration class
	'''
	SECRET_KEY=os.environ.get('SECRET_KEY')

class ProdConfig(Config):
	'''
	child production config class
	'''
	pass

class DevConfig(Config):
	'''
	child development config class
	'''
	DEBUG=True

config_options={
	'development':DevConfig,
	'production':ProdConfig,
}