
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, static_file

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root = '/home/maxiimou/prod/pythonanywhere/static')

@route('/mad-dam')
@view('mad-dam')
def maddam_input():
    return

@post('/mad-dam')
def maddam_submit():
    return True

application = default_app()

