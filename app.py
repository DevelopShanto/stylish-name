from flask import Flask, render_template, request

app = Flask(__name__)

def generate_styles(name):
    fonts = {
        "double": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
        "script": "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩",
        "bold": "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏ＱＲＳＴＵＶＷＸＹＺ",
        "mono": "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂Ｔ𝚄ＶＷ𝚇Ｙ𝚉"
    }
    ascii_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    for key in fonts:
        new_name = ""
        for char in name:
            if char in ascii_chars:
                index = ascii_chars.index(char)
                new_name += fonts[key][index]
            else:
                new_name += char
        res.append(new_name)
    
    res.append(f"『{name}』")
    res.append(f"亗 {name} 亗")
    for i in range(1, 95):
        res.append(f"{name} Style {i}")
    return res

@app.route("/", methods=["GET", "POST"])
def index():
    combined_styles = []
    tiktok_id = "@DevelopShanto"
    if request.method == "POST":
        name = request.form.get("name")
        eng_list = generate_styles(name)
        for s in eng_list:
            combined_styles.append({"eng": s, "arb": f"{name} ☪️"})
    return render_template("index.html", styles=combined_styles, tiktok=tiktok_id)
