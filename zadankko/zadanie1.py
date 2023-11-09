# importowanie modułów i klas
from flask import Flask, render_template, request
from flask_bs4 import Bootstrap
import math

#konfiguracja aplikacji
app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = "POaduinbuiqFDAADF%$W$#WQHnnaSUODbFASDue"

#głównia część aplikacji
@app.route('/')
def index():
    return render_template('template.html',
                           title="home",)

@app.route('/wynik', methods=['POST'])
def liczenieDelty():
    a = float(request.form["a"])
    b = float(request.form["b"])
    c = float(request.form["c"])
    Delta = float((b**2)-4*a*c)

    if a == 0:
        return("a nie może być 0")

    elif Delta > 0:
        x1 = round(((-b + math.sqrt(Delta)) /2*a), 2)
        x2 = round(((-b - math.sqrt(Delta)) /2*a), 2)
        return(round(((-b - math.sqrt(Delta)) /2*a), 2))
    elif Delta == 0:
        x0 = -b/2*a
        return ("miejsce zerowe to: ", round(x0,2))
    elif (Delta < 0):
        return("Delta jest mniejsza od zera")
    return render_template('wynik.html',
                           title="home",
                           )


#uruchamianie informacji
if __name__ == '__main__':
        app.run(debug=True)
