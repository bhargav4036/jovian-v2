from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Data engineer',
  'location': 'delhi',
  'salary': 'rs.150000'
}, {
  'id': 2,
  'title': 'Data analyst',
  'location': 'india',
  'salary': 'rs.15000'
}, {
  'id': 3,
  'title': 'Data manager',
  'location': 'delhiii',
  'salary': 'rs.15000'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS, company='jovian')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


app.run(host='0.0.0.0', debug=True)
