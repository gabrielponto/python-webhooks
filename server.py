#-*- coding: utf-8 -*-
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
		path = os.path.join(os.path.realpath(__file__).replace('server.py', ''), 'scripts', path[0], '{}.sh'.format(path[1]))
		try:
			call(path)
		except OSError:
			raise OSError(u'{}: {}'.format('File not found: ', path))

if __name__ == '__main__':
    app.run()