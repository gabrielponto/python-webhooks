import web

urls = ('/.*', 'hooks')

app = web.application(urls, globals())

class hooks:
    def POST(self):
        data = web.data()
        print 'DATA RECEIVED:'
        print >> 'test.txt', data
        print
        return 'OK'

if __name__ == '__main__':
    app.run()