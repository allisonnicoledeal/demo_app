from flask import Flask, render_template, redirect, g, url_for, request

import model

app = Flask(__name__)


@app.route("/")
def index():
    model.connect()
    users = model.get_users()
    return render_template("index.html", users=users)
    
@app.route("/user_profile")
def show_user():
    model.connect()
    user_id = request.args.get("id")
    user = model.get_user_by_id(user_id)
    # user_profile = model.user_name.get_posts()

    return render_template("user_profile.html", user= user)
                                                # name=user.name,
                                                # email=user.email)
                                                


if __name__ == "__main__":
    app.run(debug=True)
