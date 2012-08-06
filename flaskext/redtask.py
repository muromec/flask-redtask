import json
from functools import wraps

import memcache
from flask import Blueprint, request

app = Blueprint('task', __name__)

WHITE = ['127.0.0.1']

@app.route('/_ah/task', methods=['POST'])
def task_run():
    if request.remote_addr not in WHITE:
        return 'no'

    data = json.loads(request.form['_'])
    callname = data.get('call')
    a, kw = data['args'], data['kwargs']

    modname, symname = callname.rsplit('.', 1)
    mod = __import__(modname, fromlist=[symname])
    call = getattr(mod, symname)

    call.direct(*a, **kw)
    return 'ok'

def get_mc():
    mc = memcache.Client(['127.0.0.1:11211'])
    return mc

mc = get_mc()

def _defer(f, *a, **kw):
    env = [
    ]
    task = {
        "url": request.url_root+'_ah/task',
            "method": "POST",
            "body": { "_": json.dumps({
                "args": a,
                "kwargs": kw,
                "env": env,
                "call": "%s.%s" % (f.__module__,f.__name__),
            }),},
    }
    mc.set('task:url', json.dumps(task))

def defer(f):
    @wraps(f)
    def defered(*a, **kw):
        return _defer(f, *a, **kw)

    defered.direct = f
    defered.defer = defered

    return defered
