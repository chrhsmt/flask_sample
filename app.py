from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route('/', methods=["GET", "POST", "PUT"])
def index():
  if request.method == "GET":
    app.logger.debug("start --debug")
    app.logger.info("info")
    app.logger.warning("warn")
    app.logger.error("error")
    return render_template("index.html", method=request.method, title="Hello fuckin' world.")
  elif request.method == "PUT":
    return render_template("index.html")
  else:
    return "Hello, World POST"

@app.route('/user/<name>')
def user(name):
  return render_template("user.html", name=name, title="User is")

@app.route('/post/<int:post_id>')
def post_id(post_id):
  return "Hello, post%s" % post_id

# with app.test_request_context():
#   print url_for('index')
#   print url_for('user', name="yes i do")
#   print url_for('post_id', post_id= 22)

if __name__ == '__main__':
  app.run(debug = True)