from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

poll_data = {
    'question': 'Qual a sua Linguagem Preferida?',
    'options': [
        {'id': 1, 'text': 'Java', 'votes': 0},
        {'id': 2, 'text': 'Javascript', 'votes': 0},
        {'id': 3, 'text': 'Python', 'votes': 0},
    ]
}

@app.get("/")
def show_poll():
    return render_template("poll.html", poll_data=poll_data)

@app.post("/")
def poll():
    choice = request.form.get("language")
    id_found = False

    for item in poll_data['options']:
        if item['id'] == int(choice):
            id_found = True
            item['votes'] += 1
            break

    if id_found:
        return redirect(url_for("show_poll"))
    else:
        return "Erro: ID não Encontrado!", 404

if (__name__) == "__main__":
    app.run(debug=True)