from flask import Flask, render_template, request

app = Flask(__name__)

# Глобальный список для хранения всех пользователей (временно, для демо)
users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')
        hobby = request.form.get('hobby')

        # Добавляем нового пользователя в список
        users.append({
            'name': name,
            'age': age,
            'city': city,
            'hobby': hobby
        })
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)