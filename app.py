from flask import Flask, render_template, request, session, redirect, url_for
from chatbot import Chatbot

app = Flask(__name__)
app.secret_key = "simple-secret-key"

bot = Chatbot()

@app.route("/", methods=["GET", "POST"])
def index():
    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        user_message = request.form.get("message", "").strip()

        if user_message:
            bot_reply = bot.get_response(user_message)

            messages = session["messages"]
            messages.append({"role": "user", "text": user_message})
            messages.append({"role": "bot", "text": bot_reply})
            session["messages"] = messages

        return redirect(url_for("index"))

    return render_template("index.html", messages=session["messages"])


@app.route("/clear", methods=["POST"])
def clear():
    session["messages"] = []
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)