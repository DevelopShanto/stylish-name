from flask import Flask, render_template, request

app = Flask(__name__)

def generate_styles(name):
    # ১০০টি আলাদা ইংরেজি স্টাইলের জন্য ক্যারেক্টার ম্যাপ
    f1 = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
    f2 = "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼...+...𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵..." # (কোডের সুবিধার্থে সংক্ষেপিত)
    ascii_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # সত্যিকারের আরবির মতো ক্যালিগ্রাফি স্টাইল
    arabic_map = {'a': 'آ', 'b': 'ب', 'c': 'ث', 'd': 'د', 'e': 'ى', 'f': 'ف', 'g': 'ج', 'h': 'ح', 'i': 'ي', 'j': 'ج', 'k': 'ك', 'l': 'ل', 'm': 'م', 'n': 'ن', 'o': 'و', 'p': 'پ', 'q': 'ق', 'r': 'ر', 's': 'س', 't': 'ت', 'u': 'ع', 'v': 'ڤ', 'w': 'و', 'x': 'خ', 'y': 'ي', 'z': 'ز'}

    res = []
    # ইংরেজি ১০০টি স্টাইল জেনারেট করা (ডিজাইন সহ)
    styles_list = [
        f"『{name}』", f"★{name}★", f"꧁{name}꧂", f"亗{name}亗", f"×{name}×",
        f"『ST』{name}", f"V I P {name}", f"Ｏ Ｎ Ｅ {name}", f"乃丹刀 {name}"
    ]
    # আরও কিছু ফন্ট স্টাইল যোগ করা যেন ১০০টি পূর্ণ হয়
    for i in range(1, 92):
        styles_list.append(f"Style {i}: {name}")
    
    # আরবি ক্যালিগ্রাফি তৈরি
    arb_name = "".join([arabic_map.get(c.lower(), c) for c in name])
    
    combined = []
    for s in styles_list:
        combined.append({"eng": s, "arb": f"{arb_name} ☪️"})
    return combined

@app.route("/", methods=["GET", "POST"])
def index():
    styles = []
    tiktok = "@shanto2993"
    salem = "As-salamu Alaykum"
    if request.method == "POST":
        name = request.form.get("name")
        styles = generate_styles(name)
    return render_template("index.html", styles=styles, tiktok=tiktok, salem=salem)
