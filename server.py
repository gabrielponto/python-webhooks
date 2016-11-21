#-*- coding: utf-8 -*-
import web
import json
import os
urls = ('/.*', 'hooks')
app = web.application(urls, globals())

class hooks:
	def POST(self):
		data = json.loads(web.data())
		path = data['repository']['full_name'].split('/')
		#full_name is like gabrieloliveiranet/topweb-web
		current_path = os.path.realpath(__file__)
		parts = current_path.split(os.sep)
		del parts[-1] #delete the file name of current
		current_path = os.sep.join(parts)
		path = os.sep.join([current_path, 'scripts', path[0], '{}.sh'.format(path[1])])
		try:
			os.system(path)
		except OSError:
			raise OSError(u'{}: {}'.format('File not found: ', path))

if __name__ == '__main__':
    app.run()