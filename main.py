#-*- coding: utf-8 -*-
#filename: main.py
import sys
import web
sys.path.append(r'./cgi/')# filename: handle.py
sys.path.append(r'./cgi/SE/')# filename: handle.py
sys.path.append(r'./DB/')# filename: handle.py
sys.path.append(r'./handle/')
from handle import Handle

urls = (
    '/wx', 'Handle',
)
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
