import os
from werkzeug.wrappers import Request, Response
from dotenv import load_dotenv

load_dotenv()
user = os.getenv("USER_MIDDLEWARE")
password = os.getenv("PASS_MIDDLEWARE")


class middleware():
    """
    WSGI middleware
    """
    def __init__(self, app):
        self.app = app
        self.userName = user
        self.password = password

    def __call__(self, environ, start_response):
        request = Request(environ)
        userName = request.authorization['username']
        password = request.authorization['password']

        # verify the username and password from env config variable
        if userName == self.userName and password == self.password:
            environ['user'] = {'name': self.userName}
            return self.app(environ, start_response)
        res = Response(u'Authorization failed: {},{}'.format(self.userName, self.password), mimetype='text/plain', status=401)
        return res(environ, start_response)