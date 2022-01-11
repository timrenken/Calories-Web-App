from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()

        return render_template('calories_form_page.html',
                               calories_form=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        temperature = Temperature(country=calories_form.country.data,
                                  city=calories_form.city.data).get()

        calorie = Calorie(weight=float(calories_form.weight.data),
                          height=float(calories_form.height.data),
                          age=float(calories_form.age.data),
                          sex=calories_form.sex.data,
                          temperature=temperature)

        calories = round(calorie.calculate(), 0)

        return render_template('calories_form_page.html',
                               result=True,
                               calories_form=calories_form,
                               calories=calories)


class CaloriesForm(Form):
    weight = StringField(label="Enter weight in pounds: ", default="160")
    height = StringField(label="Enter height in inches: ", default="68")
    age = StringField(label="Enter your current age: ", default="35")
    sex = StringField(label="Enter your sex: (male / female) ", default="male")
    city = StringField(label="Enter your City: ")
    country = StringField(label="Enter your Country: ", default="USA")

    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form',
                 view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)
