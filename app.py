from flask import Flask, render_template, request

app = Flask(__name__)
app.run(host='127.0.0.1', port=8080, debug=True)

@app.route("/", methods=["GET", "POST"])
def index():
    complement = None
    reverse = None

    if request.method == "POST":
        seq = request.form.get("sequence")
        action = request.form.get("action")

        if action == "Complement":
            complement = ""
            for i in seq:
                if i.upper() == 'A':
                    complement += 'T'
                elif i.upper() == 'T':
                    complement += 'A'
                elif i.upper() == 'G':
                    complement += 'C'
                elif i.upper() == 'C':
                    complement += 'G'
                else:
                    return "Invalid input: Please provide a valid DNA sequence."

        elif action == "Reverse Sequence":
            reverse = seq[::-1]

    return render_template("index.html", complement=complement, reverse=reverse)
