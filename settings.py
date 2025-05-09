pip install dj-database-url
mport dj-database-url
import os
DATABASES = {
 "default": dj_database_url.parse(os.environ.get("postgresql://test_db_0c7m_user:6ETFQYGC7vT6PBTggqsJG4BxuzjqHwqd@dpg-d0epges9c44c738a9bq0-a.oregon-postgres.render.com/test_db_0c7m"))
