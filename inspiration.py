from flask import Flask
from flask import render_template
import random
import linecache

app = Flask(__name__)

@app.route('/')
def quote():
    server='My Server'
    with open('inspiration.txt') as fp:
        count=len(fp.readlines())
        num=random.randrange(1,count,1)
        quote=linecache.getline('inspiration.txt',num)

    return render_template(
            'inspiration.html',
            quote=quote,
            server=server
            )
