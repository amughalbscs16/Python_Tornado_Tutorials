
import time
import os
import tornado.web
from handlers.home_handler import HomeHandler
from handlers.main_api_handler import MainAPIHandler

STATIC_PATH = os.path.join(os.path.dirname(__file__), '../../assets')


class ChiMainServer(tornado.web.Application):
    def __init__(self):

        settings = {
            'debug': True,
            'serve_traceback': False,
            'compress_response': True,
            'template_path': 'templates/',
            'static_url_prefix': '/assets/',
            'static_path': STATIC_PATH,
            'autoreload': False,
            'xsrf_cookies': False,
        }

        handlers = self.GetHandlers()

        tornado.web.Application.__init__(self, handlers, **settings)

        return

    def GetHandlers(self):
        # /api/slug/Method
        handlers = []
        handlers.append((r"/", HomeHandler))
        handlers.append((r"/api/(.*)/(.*)", MainAPIHandler))
        return handlers
