from flask import Flask, render_template_string, request

app = Flask(__name__)

def generate_styles(name):
    # Fancy Font Mapping (প্রিমিয়াম ফন্ট)
    fonts = {
        "bold": "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏Ｑ𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳",
        "italic": "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻",
        "script": "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃",
        "double": "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫",
        "mono": "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"
    }
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    def transform(text, mapping):
        table = str.maketrans(normal, mapping)
        return text.translate(table)

    results = []
    # ফেন্সি ফন্ট
    results.append(transform(name, fonts["bold"]))
    results.append(transform(name, fonts["script"]))
    results.append(transform(name, fonts["double"]))
    
    # প্রিমিয়াম সিম্বলিক ডিজাইন
    symbols = [
        "꧁༺ {} ༻꧂", "⚔️ {} ⚔️", "『 {} 』", "☠️ {} ☠️", "✨ {} ✨",
        "☬ {} ☬", "♛ {} ♛", "亗 {} 亗", "✿ {} ✿", "❤️ {} ❤️",
        "⫷ {} ⫸", "〆{}〆", "卍 {} 卍", "◥ {} ◤", "๏ {} ๏",
        "【{}】", "☄️ {} ☄️", "⚡ {} ⚡", "❄️ {} ❄️",
        "╰‿╯ {} ╰‿╯", "×͜× {}", "☯️ {} ☯️", "⚓ {} ⚓", "⛓️ {} ⛓️"
    ]
    
    # ফন্ট এবং সিম্বল মিক্স করে ১০০+ স্টাইল
    for s in symbols:
        results.append(s.format(name))
        results.append(s.format(transform(name, fonts["bold"])))
        results.append(s.format(transform(name, fonts["script"])))
        results.append(s.format(transform(name, fonts["double"])))

    return results

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Saif's Premium Styles</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: sans-serif; text-align: center; background: #0f0c29; color: white; padding: 20px; }
        .container { max-width: 500px; margin: auto; }
        input { padding: 15px; width: 80%; border-radius: 25px; border: none; margin-bottom: 15px; font-size: 16px; }
        button { padding: 12px 25px; background: #ff4757; color: white; border: none; border-radius: 25px; font-weight: bold; cursor: pointer; }
        .result-box { background: rgba(255, 255, 255, 0.1); padding: 15px; margin: 10px 0; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; border-left: 5px solid #ff4757; }
        .copy-btn { background: #2ed573; padding: 5px 12px; font-size: 12px; border-radius: 15px; border: none; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <h1>💎 Premium Styles 💎</h1>
        <form method="POST">
            <input type="text" name="name" placeholder="আপনার নাম লিখুন..." required>
            <br>
            <button type="submit">ম্যাজিক দেখুন</button>
        </form>
        <div style="margin-top: 20px;">
        {% if res %}
            {% for s in res %}
                <div class="result-box">
                    <span>{{ s }}</span>
                    <button class="copy-btn" onclick="copy('{{ s }}')">Copy</button>
                </div>
            {% endfor %}
        {% endif %}
        </div>
    </div>
    <script>
        function copy(text) {
            navigator.clipboard.writeText(text);
            alert("কপি হয়েছে: " + text);
        }
    </script>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    res = None
    if request.method == "POST":
        name = request.form.get("name")
        res = generate_styles(name)
    return render_template_string(HTML, res=res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

