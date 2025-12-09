from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return "Page d'accueil"

@app.route('/newuser/', methods=['GET', 'POST'])
def newuser():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username', '')

        # Critères
        criteres = [
            (r'.{6,}', "Au moins 6 caractères"),
            (r'.*[0-9].*', "Au moins 1 chiffre"),
            (r'.*[A-Z].*', "Au moins 1 majuscule"),
            (r'.*[a-z].*', "Au moins 1 minuscule"),
            (r'.*[#%{}@].*', "Au moins 1 caractère spécial parmi #%{}@")
        ]

        # Vérification
        erreurs = []
        for patt, msg in criteres:
            if re.fullmatch(patt, username) is None and not re.search(patt, username):
                erreurs.append(msg)

        if not erreurs:
            message = "Identifiant valide ✅"
        else:
            message = "Échec sur : " + ", ".join(erreurs)

    return render_template('newuser.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

