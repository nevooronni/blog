import os

class Config:
	'''
	parent configuration class
	'''
	SECRET_KEY=os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nevo:speeds01@localhost/iblogger'

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