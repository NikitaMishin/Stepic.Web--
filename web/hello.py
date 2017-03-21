

def wsgi_app(environ,start_response):
    status = "200 OK"
    headers = ["Content-Type", "text/plain"]
    body = [environ["QueryString"].replace("&","\r\n"),encoding = "utf-8"]
	start_response(status,headers)
	return [body]
    
