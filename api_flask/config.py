import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
elk_url = "http://bch-elk-01.cci-entel.cl:9200/_search?"
headers = {"content-type": "application/json"}
# SQLALCHEMY_ECHO = False
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/database_name"