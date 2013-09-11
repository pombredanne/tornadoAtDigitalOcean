import tornado.wsgi
import os
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
	techs = ['BAE', 'Python', 'Tornado', 'AngularJS']
        self.render('index.html', techs=techs)
 
settings = {"template_path": os.path.join(os.path.dirname(__file__), 
				   	   "templates")}
apphandlers = tornado.wsgi.WSGIApplication([
    (r"/", MainHandler),
], **settings)
from bae.core.wsgi import WSGIApplication

application = WSGIApplication(apphandlers)
