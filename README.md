# Python Tornado Tutorials(Self Made)
Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.

Start from lecture 1, i.e. a basic one file application, and keep on moving and observing the updates in the consequent lectures.
#Hello, world
Here is a simple “Hello, world” example web app for Tornado:
<code>
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
  
</code>
This example does not use any of Tornado’s asynchronous features; for that see this simple chat room.
