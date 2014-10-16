from .settings import *

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}
