from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import inspect

#from models import Entry


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///miCrud.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    description = db.Column(db.String(120), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)

    def __repr__(self):
#        return f"Entry('{self.title}'"
        return self.title


#SQLAlchemy.create.all()
with app.app_context():
    db.create_all()


'''


#from .models.entry import Entry
#from .models.user import User
#from forms.contact import ContactForm

'''

@app.route('/')
@app.route('/index')
def index():

    entries = Entries.query.all()
    return render_template('index.html', entries=entries)
#    return render_template('index.html')


@app.route('/entries')
def entries():

    entries = Entries.query.all()
    return render_template('entries.html', entries=entries)
#    return render_template('entries.html')




@app.route("/entriesNew")
def entriesNew():

#    table = inspect(model)
    table = inspect(Entries)
    tablec = table.c
    for column in table.c:
        print (column.name)

    for colName in tablec:
        print (colName)
#<!--
#          <input type='submit' value=' delete' />
#
#
#</form>
##


#        </td></tr>
#-->
#       {% endfor %}

    #print (table)

    #students = Students.query.all()
    #db.session.delete(deletetodo)
    #db.session.commit()
#    return render_template("studentsNew1.html")
    return render_template("entriesNew1.html", tablec=tablec)






@app.route("/entriesInsert", methods=['GET','POST'])
def entriesInsert():
    print ('begin entriesInsert')
    #exit()
    if request.method=='POST':
        print ('post')

        print (request.form)
#        fields = request.form['name']
        fields = request.form
        cDesc = request.form['entries.description']
        print (cDesc)
        entriesTitle = fields['entries.title']
        print (entriesTitle)

        entries = Entries(title=entriesTitle, description=cDesc)

        print(entries)

        db.session.add(entries)
        db.session.commit()

    entries1 = Entries.query.all()
    print (entries1)
    for entry in entries1:
       print (entry)

    #exit()
#db.session.delete(deletetodo)
    #db.session.commit()
    #return render_template("courses.html", courses1=courses1)
    return redirect("/entries")




if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=5000)

