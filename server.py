import web
import json
import os
from subprocess import call
urls = ('/.*', 'hooks')
app = web.application(urls, globals())

class hooks:
	def POST(self):
		data = json.loads(web.data())
		path = data['repository']['full_name'].split('/')
		#full_name is like gabrieloliveiranet/topweb-web
		print os.path.join('.', 'scripts', path[0], '{}.sh'.format(path[1]))
		call(os.path.join('.', 'scripts', path[0], '{}.sh'.format(path[1])))

if __name__ == '__main__':
    app.run()