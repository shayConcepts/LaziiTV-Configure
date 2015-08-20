# -----------------------------------
#     cyclone.py
#     Author: Andrew Shay
#     Created: June 10 2012
#     Description: The Tornado server that runs Flask
# -----------------------------------


from tornado.wsgi import WSGIContainer
from tornado.ioloop import IOLoop
from tornado.web import FallbackHandler, RequestHandler, Application
from app import app


class MainHandler(RequestHandler):
    def get(self):
        self.write("This message comes from Tornado ^_^")

tr = WSGIContainer(app)

application = Application([
                          (r"/tornado", MainHandler),
                          (r".*", FallbackHandler, dict(fallback=tr)),
                          ])


def start_cyclone(app_port):
    """
    Starts tornado to run Flask

    Keyword Arguments:
    app_port -- Int. The port to use for Tornado
    """

    # Attempt to find open port
    try:
        application.listen(app_port)
        print("Cyclone Started:" + str(app_port))
        IOLoop.instance().start()
    except:
        print("Failed to start Tornado")
        pass


if __name__ == "__main__":
    start_cyclone(5000)
