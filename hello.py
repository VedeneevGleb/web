def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)
    qs = environ['QUERY_STRING'].split('&')
    qss = [item+'\n' for item in qs]
    return qss