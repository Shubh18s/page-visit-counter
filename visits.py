from flask import Flask
from redis import Redis
app = Flask(__name__)
r = Redis(host='redis-server', port=6379)
r.set('visits', 0)

@app.route('/')
def index():
    try:
        count = int(r.get('visits'))
        r.set('visits', count+1)
        return '<h1>Number of visits is %s</h1>' % count
    except:
        return '<h1>Oops, visits undefined!</h1>' 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)