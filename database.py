import sqlalchemy
from sqlalchemy import create_engine,text
db_connect_string="mysql+pymysql://1z15knwoi70vh1gx8bbq:pscale_pw_7kwjTMeGJvMTHLA0NoEe1KJuApIf1CM5B2y46mGsw88@aws.connect.psdb.cloud/joviancarrers?charset=utf8mb4"
engine = create_engine(db_connect_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
            
        }
    }
)
with engine.connect() as conn:
  result=conn.execute(text("select * from jobs"))


jobs=[]
for row in result.all():
  jobs.append(dict(row._mapping))
print(jobs)
