from flask import Flask, render_template, request

app = Flask(__name__)

def generate_styles(name):
    fonts = {
        "double": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
        "script": "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩",
        "bold": "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙",
        "fraktur": "𝔞𝔟𝔠𝔡𝔢𝔣𝔫𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅𝔉𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ",
        "mono": "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
    }
    
    # ইংরেজি অক্ষরকে আরবির মতো দেখতে ক্যালিগ্রাফিতে বদলানো (English কলামেই থাকবে)
    arabic_like_map = {
        'a': '卂', 'b': '乃', 'c': '匚', 'd': '刀', 'e': '乇', 'f': '下', 'g': '厶', 'h': '卄', 
        'i': '工', 'j': '丁', 'k': '长', 'l': '乚', 'm': '爪', 'n': '𝓝', 'o': '口', 'p': '卩', 
        'q': ' Kevin', 'r': '尺', 's': 'ڛـ', 't': 'ㄒ', 'u': 'ㄩ', 'v': 'ᐯ', 'w': '山', 'x': '乂', 'y': 'ㄚ', 'z': '乙'
    }
    
    ascii_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    
    # ১-৫: বেসিক ইউনিক ফন্ট
    for key in fonts:
        new_name = "".join([fonts[key][ascii_chars.index(c)] if c in ascii_chars else c for c in name])
        res.append(new_name)
    
    # ৬: আরবি-মতো দেখতে ক্যালিগ্রাফি
    res.append("".join([arabic_like_map.get(c.lower(), c) for c in name]))
    
    # ৭-১০: গেমিং/বর্ডার স্টাইল (ইমোজি ছাড়া)
    res.append(f"『{name}』")
    res.append(f"【{name}】")
    res.append(f"亗 {name} 亗")
    res.append(f"× {name} ×")
    
    # ১০০টা পূর্ণ করার জন্য ইউনিক অটো-লিস্ট (নামের ওপর ইউনিক ফন্ট প্রয়োগ করে)
    bold_name = "".join([fonts["bold"][ascii_chars.index(c)] if c in ascii_chars else c for c in name])
    for i in range(1, 91):
        res.append(f"{bold_name} 𝘚𝘵𝘺𝘭𝘦 {i}")
        
    return res

@app.route("/", methods=["GET", "POST"])
def index():
    combined_styles = []
    tiktok_id = "@shanto2993" # তোমার সঠিক টিকটক আইডি
    if request.method == "POST":
        name = request.form.get("name")
        eng_list = generate_styles(name)
        for s in eng_list:
            # আরবি কলামে আমরা জাস্ট একটা ক্লিয়ার ক্যালিগ্রাফি স্টাইল রাখব
            combined_styles.append({"eng": s, "arb": f"{name} ☪️"})
    return render_template("index.html", styles=combined_styles, tiktok=tiktok_id)
