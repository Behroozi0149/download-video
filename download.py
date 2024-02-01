import webbrowser
url =input("enter your url:")
url=url[:12]+"ss"+url[12:]
webbrowser.open(url)