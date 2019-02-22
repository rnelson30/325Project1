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
	logger.write(request.remote_addr + "~")
        if "Forwarded" in request.headers:
            logger.write(request.headers["Forwarded"] + "~")
        else:
            logger.write("NaN~")
        logger.write('%s~' % datetime.datetime.now())
        if "user-agent" in request.headers:
            logger.write(request.headers["user-agent"] + "~")
        else:
            logger.write("NaN~")
        if "connection" in request.headers:
            logger.write(request.headers["connection"] + "~")
        else:
            logger.write("NaN~")
        if "dnt" in request.headers:
            logger.write(request.headers["dnt"] + "~")
        else:
            logger.write("NaN~")
        if "host" in request.headers:
            logger.write(request.headers["host"] + "~")
        else:
            logger.write("NaN~")
        if "upgrade-insecure-requests" in request.headers:    
            logger.write(request.headers["upgrade-insecure-requests"] + "~")
        else:
            logger.write("NaN~")
        if "accept" in request.headers:
            logger.write(request.headers["accept"] + "~")
        else:
            logger.write("NaN~")
        if "accept-language" in request.headers:
            logger.write(request.headers["accept-language"] + "~")
        else:
            logger.write("NaN~")
        if "accept-encoding" in request.headers:    
            logger.write(request.headers["accept-encoding"] + "\n")
        else:
            logger.write("NaN~")
    return render_template("root.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int("80"))
