from flask import Flask , render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hard to guess String'
bootstrap = Bootstrap(app)

class NameForm(Form):
    name = TextField('Aap ka naam kya hai?',validators=[Required()])

@app.route('/',methods=['GET','POST'])
@app.route('/index',method=['GET','POST'])
def index():
                     name = None
                     form = NameForm()
                     if form.validate_on_submit():
                         name = form.name.data
                         form.name.data=""
                     return render_template('index.html', form=form, name=name)
if __name__=='__main__':
    app.run(debug=True)

