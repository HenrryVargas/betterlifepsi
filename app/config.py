import os

BABEL_DEFAULT_LOCALE = 'zh_CN'
BABEL_DEFAULT_TIMEZONE = 'CST'
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://flask:flask@localhost:5432/flask'
SECRET_KEY = '123QWEasDzXcqazw'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = '123QWEasDzXcqazw'
SECURITY_REGISTERABLE = False
SECURITY_CONFIRMABLE = False
SECURITY_RECOVERABLE = False
SECURITY_CHANGEABLE = False
DEBUG = (os.environ.get('DEBUG') == "True")
TESTING = (os.environ.get('TESTING') == "True")
DEBUG_TB_INTERCEPT_REDIRECTS = False
SENTRY_DSN = os.environ.get('SENTRY_DSN')
# TODO: Move those business related settings to a table and make it changeable via UI.
DEFAULT_DELIVER_DAY = 5
DEFAULT_LEAD_DAY = 3
DEFAULT_CATEGORY_ID = 1
