import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("root.html")


@app.route('/img/<img_name>')
def show_post(img_name):
    # show the post with the given id, the id is an integer
    # return 'Img %s' % img_name
    print(request.headers)
    with open("logFile.txt", "a") as logger:
        logger.write(img_name + "~")
        logger.write('%s~' % datetime.datetime.now())
        logger.write(request.headers["user-agent"] + "~")
        logger.write(request.headers["connection"] + "~")
        logger.write(request.headers["dnt"] + "~")
        logger.write(request.headers["host"] + "~")
        logger.write(request.headers["upgrade-insecure-requests"] + "~")
        logger.write(request.headers["accept"] + "~")
        logger.write(request.headers["accept-language"] + "~")
        logger.write(request.headers["accept-encoding"] + "\n")
    return render_template("root.html")


if __name__ == "__main__":
    app.run(debug=True)
