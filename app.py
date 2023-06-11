from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import create_engine,text

app = Flask(__name__)

def load_jobs_from_db():
  with engine.connect() as conn:
    result=conn.execute(text("select * from jobs"))
    jobs=[]
    for row in result.all():
      jobs.append(dict(row._mapping))
      print(jobs)
      return jobs

@app.route('/')
def hello_world():
  jobs=load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company='jovian')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs)


app.run(host='0.0.0.0', debug=True)
