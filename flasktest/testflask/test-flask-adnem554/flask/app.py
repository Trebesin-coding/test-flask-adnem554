# Z následujících si vyber kód a sestav funkční flask aplikaci (není třeba použít vše, vyber si pouze ty části kódu, které potřebuješ)
# Kód je funkční, pouze místo dotazníků je potřeba doplnit podle potřeby
from flask import Flask, render_template, request, redirect, url_for
import json
app = Flask(__name__)
json_file = "recenze.json"




@app.route("/")
def vítej():

    return render_template("vitej.html")


@app.route("/form")
def form():
    login = request.args.get("login")
    recenze = request.args.get("recenze")
    print(login,recenze)
    if login and recenze:
        return redirect(url_for("form",jinja_login=login,jinja_recenze=recenze))
    if recenze == "nic":
        print ("uživatel byl příliš líný na napsání recenze")
    with open("recenze.json","w", encoding="utf-8")as f:
        json.dump(recenze,f,ensure_ascii=False,indent=2)

    return render_template("form.html",jinja_name=login,jinja_recenze=recenze)

# app = Flask(__name__)

# @app.route("???")
# request.args.get("???")
# request.form.get("???")
# print("???")
# cursor.execute("???")
# if request.method == "POST"
# render_template("???", ???, ???)


if __name__ == "__main__":
     app.run(debug=True)
   #  zapina main funkci a končí, plus sama od sebe zapina debug
