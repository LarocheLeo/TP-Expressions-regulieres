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

        if re.fullmatch(r'.{6,}', username) is None : 
            message = "Echec : au moins 6 caractères requis"

        else: 
            if re.fullmatch(r'.*[0-9].*', username) is None : 
                message = "Echec : au moins 1 nombre requis"

            else: 
                if re.fullmatch(r'.*[A-Z].*', username) is None : 
                    message = "Echec : au moins 1 majuscule requis"

                else:
                    if re.fullmatch(r'.*[a-z].*', username) is None : 
                        message = "Echec : au moins 1 minuscule requis"

                    else:
                        if re.fullmatch(r'.*[#%{}@].*', username) is None : 
                            message = "Echec : au moins avoir l'un des caractères suivant: #%{}@"    
                        else: 
                            message = "Identifiant valide"
                            
    return render_template('newuser.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

