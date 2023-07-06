from flask import Flask
from time import sleep, time
from psutil import boot_time, disk_usage, net_io_counters
from subprocess import check_output
from os import path as ospath
app = Flask(__name__)
botStartTime = time()
if ospath.exists('.git'):
    commit_date = check_output(["git log -1 --date=format:'%y/%m/%d %H:%M' --pretty=format:'%cd'"], shell=True).decode()
else:
    commit_date = 'No UPSTREAM_REPO'

@app.route('/status', methods=['GET'])
def status():
    bot_uptime = time() - botStartTime
    uptime = time() - boot_time()
    sent = net_io_counters().bytes_sent
    recv = net_io_counters().bytes_recv
    return {
        'commit_date': commit_date,
        'uptime': uptime,
        'on_time': bot_uptime,
        'free_disk': disk_usage('.').free,
        'total_disk': disk_usage('.').total,
        'network': {
            'sent': sent,
            'recv': recv,
        },
    }
@app.route('/')
def hello_world():
    return 'TGNVS'


if __name__ == "__main__":
    app.run()
