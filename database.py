from flask import json
from sqlalchemy import create_engine,text

user_name = 'root'
host = '127.0.0.1'
password = 'vignesh2001'
db_name = 'projects'


engine = create_engine(f'mysql+pymysql://{user_name}:{password}@{host}/{db_name}')


with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM projectlist'))

result_dicts = []
for row in result.mappings():
    project = dict(row)
    project['lang_used'] = json.loads(project['lang_used'])
    result_dicts.append(project)

print(result_dicts)