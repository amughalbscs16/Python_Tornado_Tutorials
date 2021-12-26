# Python Tornado Tutorials(Self Made)
Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.

Start from lecture 1, i.e. a basic one file application, and keep on moving and observing the updates in the consequent lectures.
#Hello, world
Here is a simple “Hello, world” example web app for Tornado:
<code>
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):<br/>
    def get(self):<br/>
        self.write("Hello, world")<br/>

def make_app():<br/>
    return tornado.web.Application([<br/>
        (r"/", MainHandler),<br/>
    ])<br/>

if __name__ == "__main__":<br/>
    app = make_app()<br/>
    app.listen(8888)<br/>
    tornado.ioloop.IOLoop.current().start()<br/>
  
</code>
This example does not use any of Tornado’s asynchronous features; for that see this simple chat room.
