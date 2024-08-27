from flask import Flask, render_template, session, redirect, url_for, make_response, request

app = Flask(__name__)

app.secret_key = 'ma_clef_a_moi_et_a_personne_dautre'

ma_liste = ['patate', 'poireaux', 'choux', 'carottes', 'oignons']

@app.route("/index.html", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pseudo = request.form.get('pseudo')
        passion = request.form.get('passion')
        #On stock les données dans la session active
        session['pseudo'] = pseudo
        session['passion'] = passion
        return redirect(url_for('home'))
    return render_template("index.html")

@app.route("/set_cookie")
def set_cookie():
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('pseudo', session.get('pseudo', 'invité'))  
    return resp

@app.route("/ma_page.html")
def ma_page():
    variable = "Ceci est affiché avec une variable"
    pseudo = request.cookies.get('pseudo', session.get('pseudo', 'invité')) 
    return render_template("ma_page.html", variable=variable, pseudo=pseudo)

@app.route("/clear_cookies")
def clear_cookies():
    resp = make_response(redirect(url_for('home')))
    resp.delete_cookie('pseudo')
    return resp

@app.route("/liste.html")
def liste():
    return render_template("liste.html", liste=ma_liste)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4200)