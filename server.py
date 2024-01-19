from flask_app import app
from flask_app.controllers import users, stats, opponents

if __name__ == "__main__":
    app.run(debug=True)
