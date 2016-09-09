from app import app
from flask.templating import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'raidyue'}
    return '''
        <html>
            <head>
                <title>Home Page</title>
            </head>
            <body>
                <h1>Hello, %s</h1>
            </body>
        </html>
    ''' % user['nickname']
