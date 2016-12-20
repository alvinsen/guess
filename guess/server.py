# -*- coding: utf-8 -*-
#
# This piece of code is written by
#    Jianing Yang <jianingy.yang@gmail.com>
# with love and passion!
#
#        H A P P Y    H A C K I N G !
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |
#    [________]_|__|________)<     |YANG|
#     oo    oo  'oo OOOO-| oo\\_   ~o~~o~
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#                             20 Dec, 2016
#
from flask import Flask, request, render_template
from random import randint
from uuid import uuid4

answers = dict()
app = Flask(__name__)


@app.route("/")
def index():
    uuid = request.args.get('uuid', str(uuid4()))
    answers[uuid] = randint(1, 10)
    return render_template("guess.html", uuid=uuid)


@app.route("/guess")
def guess():
    uuid = request.args.get('uuid', str(uuid4()))
    num = int(request.args.get('num'))
    answer = answers[uuid]
    if num > answer:
        hint = "try something smaller"
        win = False
    elif num < answer:
        hint = "try something bigger"
        win = False
    else:
        hint = "bingo! it's %d" % answer
        win = True
    return render_template("guess.html", hint=hint, win=win, uuid=uuid)


def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
