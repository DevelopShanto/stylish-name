from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_styles(name):
    # ১০০+ স্টাইলের লজিক (সংক্ষেপে দেওয়া হলো)
    styles = [
        f"꧁{name}꧂", f"★{name}★", f"『{name}』", f"⚡{name}⚡", 
        f"🔥{name}🔥", f"❤️{name}❤️", f"👑{name}👑", f"✨{name}✨"
    ]
    # এখানে লুপ চালিয়ে আরও ডিজাইন বাড়ানো যায়
    return styles

@app.route("/", methods=["GET", "POST"])
def index():
    eng_styles = []
    arb_styles = []
    plain_arb = ""
    if request.method == "POST":
        name = request.form.get("name")
        eng_styles = generate_styles(name)
        # আরবির জন্য সাধারণ উদাহরণ
        plain_arb = name 
        arb_styles = [f" {name} ", f" ☪️ {name} ☪️ "]
    
    # render_template ব্যবহার করছি যেন templates/index.html ফাইলটা কাজ করে
    return render_template("index.html", eng=eng_styles, arb=arb_styles, plain_arb=plain_arb)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
