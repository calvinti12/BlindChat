import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Database setup
SQLALCHEMY_DATABASE_URI = postgres://sicesapiuadffa:e85752c6f072f1261e99c63ac31637b84c41fe62d9fcd3385227faa36f826248@ec2-54-221-196-253.compute-1.amazonaws.com:5432/d12ef7nd0hamvv
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Facebook
ACCESS_TOKEN = 'YOUR_FACEBOOK_APP_ACCESS_TOKEN'
VERIFY_TOKEN = 'FACEBOOK_APP_VERIFY_TOKEN'

# App
APP_URL = "https://lovemeto.herokuapp.com/"

# For analytics purposes
CHATMETRICS_TOKEN = 'CHATMETRICS_TOKEN'

# For debugging
PAGE_ID = 'FACEBOOK_PAGE_PSID'
ADMIN_ID = "ADMIN_PSID"

