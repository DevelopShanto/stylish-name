from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_styles(name):
    # ইংরেজি বিভিন্ন ফন্টের ম্যাপ
    fonts = [
        "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫", "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",
        "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳", "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧"
    ]
    ascii_chars = "abcdefghijklmnopqrstuvwxyz"
    
    # আরবির জন্য ক্যালিগ্রাফি ম্যাপ
    arb_map = {'a':'آ','b':'ب','c':'ث','d':'د','e':'ى','f':'ف','g':'ج','h':'ح','i':'ي','k':'ك','l':'ل','m':'م','n':'ن','o':'و','r':'ر','s':'س','t':'ت','u':'ع','w':'و','y':'ي'}

    # ডেকোরেশন লিস্ট
    decor = ["꧁{}꧂", "亗{}亗", "『{}』", "★{}★", "×{}×", "【{}】", "『ST』{}", "V I P {}", "Ｏ Ｎ Ｅ {}", "乃丹刀 {}"]
    
    styles = []
    # ১০০+ ইংরেজি স্টাইল জেনারেট করা
    for i in range(1, 111):
        base_name = name
        # ১০টির পর বাকিগুলোর জন্য মিক্সড স্টাইল তৈরি করা
        if i > 10:
            d = random.choice(decor)
            base_name = d.format(name)
        else:
            base_name = decor[i-1].format(name)
        
        # আরবি ভার্সন তৈরি (প্রথম ২০টির জন্য)
        arb_name = "".join([arb_map.get(c.lower(), c) for c in name]) if i <= 20 else ""
        
        styles.append({"eng": base_name, "arb": arb_name})
    
    return styles

@app.route("/", methods=["GET", "POST"])
def index():
    res = []
    if request.method == "POST":
        name = request.form.get("name")
        res = generate_styles(name)
    return render_template("index.html", styles=res, tiktok="@shanto2993", salem="As-salamu Alaykum")
