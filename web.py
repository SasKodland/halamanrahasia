from flask import Flask 
import random 

app = Flask(__name__)

fakta = ['8 dari 10 siswa kecanduan gadget',
         'Elon Musk bilang sosmed disetting untuk candu',
         'Elon Musk mengajurkan regulasi candu']

koin = ['Koin mu menampilkan Angka !',
        'Koin mu menampilkan Gambar !',
        'Whoops Koin mu hilang !']

@app.route('/')
def home():
    return "<h1>WEBSITE BELAJAR</h1><a href='random_fact'>Klik untuk melihat fakta random!</a><h1></h1><a href='lempar_koin'>Klik untuk melempar koin!</a>"



@app.route("/random_fact")
def hello_world():
    return f"<h1>Fakta Kecanduan Teknologi</h1><p>{random.choice(fakta)}</p>"

@app.route("/lempar_koin")
def Koinners():
    return f"<h1>Lempar Koin</h1><p>{random.choice(koin)}</p>"


app.run(debug=True)

