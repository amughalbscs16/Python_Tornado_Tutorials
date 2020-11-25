import tornado.ioloop
import tornado.web
from app.server.app_server import ChiMainServer


if __name__ == "__main__":
    port = 8001
    app = ChiMainServer()
    app.listen(port)
    print("Port: {}".format(port))
    tornado.ioloop.IOLoop.current().start()

