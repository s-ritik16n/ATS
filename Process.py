import os,sys, shelve
import requests, json

class Process(object):
    """ Process,
    create daemon process, and kill parent"""
    def __init__(self):
        super(Process, self).__init__()
        pass

    def fork_new_process(self):
        try:
            pid = os.fork()
            if pid>0:
                sys.exit(0)
        except OSError, e:
            sys.stderr.write("fork failed %d %s"%(e.errno,e.strerror))
            sys.exit(1)
        self.daemonize()

    def daemonize(self):
        os.setsid()
        os.umask(0)
        self.daemon_job()

    def daemon_job(self):
        payload = {"type":"note","title":"testing","body":"anything"}

	r = requests.post("https://api.pushbullet.com/v2/pushes",headers = {"Access-Token":"","Content-Type":"application/json"},data = json.dumps(payload))


p = Process()
p.fork_new_process()
