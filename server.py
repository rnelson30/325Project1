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
    with open("logFile.txt", "w+") as logger:
        logger.write(request.headers["user-agent"] + "\n")
    return render_template("root.html")

if __name__ == "__main__":
    app.run(debug=True)
