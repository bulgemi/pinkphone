from datetime import datetime
from random import randint
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('pinkphone.html',
                           contents=None)


@app.route("/calling")
def calling():
    contents = dict()
    now = datetime.now()
    calling_count = randint(2, 5)
    calling_list = list()
    interval = 1000

    for _ in range(0, calling_count):
        calling_list.append(interval)
        interval += 1000

    contents['calling_list'] = calling_list
    contents['hello_interval'] = interval
    interval += 4000
    contents['playbook_interval'] = interval

    print(now.hour)

    if 21 <= now.hour:
        playbook_num = '08'
    elif 0 <= now.hour <= 8:
        playbook_num = '08'
    elif 9 <= now.hour <= 11:
        playbook_num = '11'
    elif 12 <= now.hour <= 13:
        playbook_num = '13'
    elif 14 <= now.hour <= 17:
        playbook_num = '17'
    else:  # 18 <= now.hour <= 20:
        playbook_num = '20'

    playbook_name = 'playbook_{}.ogg'.format(playbook_num)

    contents['playbook_name'] = playbook_name

    print("%r" % playbook_name)

    return render_template('pinkphone.html',
                           contents=contents)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
