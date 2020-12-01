import tornado.web
import json
from controllers import registry


class MainAPIHandler(tornado.web.RequestHandler):

    """

    slug: the controller slug
    method: the controller method

    """

    def prepare(self):
        pass

    async def post(self, slug, method):
        print(self.request.path)
        data = json.loads(self.request.body)
        # If correct controller
        controller = None
        if slug in registry:
            controller = registry[slug]
        ctrl_obj = controller(data)
        json_data = json.dumps({})
        # If function in controller
        if method in ctrl_obj.methods:
            ctrl_method = getattr(ctrl_obj, method)
            # call the function with data
            self.json_data = ctrl_method()

        # returning the data
        self.write(self.json_data)





