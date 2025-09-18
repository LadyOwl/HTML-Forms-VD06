from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    if request.method == 'POST':

        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')

        user_data = {
            'name': name,
            'age': age,
            'city': city,
            'hobby': hobby
        }

    return render_template('index.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)