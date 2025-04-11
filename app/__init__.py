from flask import Flask, render_template, request, jsonify
import openai
import os

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/rules")
    def rules():
        return render_template("rules.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/chat", methods=["GET", "POST"])
    def chat():
        if request.method == "POST":
            user_input = request.json.get("message")
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for the housing community Glansbaggen G:A in Norrköping. Only answer questions about the samfällighet, its rules, and applicable legal conditions."},
                    {"role": "user", "content": user_input},
                ]
            )
            reply = response.choices[0].message.content
            return jsonify({"reply": reply})
        return render_template("chat.html")

    return app
