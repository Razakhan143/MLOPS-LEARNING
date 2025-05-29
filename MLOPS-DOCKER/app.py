from flask import Flask, render_template_string, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session management

# Sample fun facts to display
fun_facts = [
    "Did you know? Honey never spoils!",
    "Octopuses have three hearts!",
    "Bananas are berries, but strawberries aren't!",
    "A group of flamingos is called a 'flamboyance'.",
    "The Eiffel Tower can be 15 cm taller during hot days."
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        if username:
            session['username'] = username
            return redirect(url_for('greet'))
        else:
            error = "Please enter a valid name."
            return render_template_string(TEMPLATE_INDEX, error=error)
    return render_template_string(TEMPLATE_INDEX)

@app.route('/greet')
def greet():
    username = session.get('username')
    if not username:
        return redirect(url_for('index'))
    fact = random.choice(fun_facts)
    return render_template_string(TEMPLATE_GREET, username=username, fact=fact)

@app.route('/reset')
def reset():
    session.pop('username', None)
    return redirect(url_for('index'))

# Templates (inline for simplicity)
TEMPLATE_INDEX = '''
<!DOCTYPE html>
<html>
<head>
    <title>Docker Flask App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <h2>Welcome to the Docker Flask Demo!</h2>
        <form method="POST" class="mt-3">
            <div class="mb-3">
                <label for="username" class="form-label">Enter your name:</label>
                <input type="text" class="form-control" id="username" name="username" required>
            </div>
            {% if error %}
            <div class="alert alert-danger">{{ error }}</div>
            {% endif %}
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
</body>
</html>
'''

TEMPLATE_GREET = '''
<!DOCTYPE html>
<html>
<head>
    <title>Greeting</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-success text-white">
    <div class="container mt-5">
        <h1>Hello, {{ username }}! 🎉</h1>
        <p>Welcome to this Flask app for Docker demonstration. 🚀</p>
        <p><em>{{ fact }}</em></p>
        <a href="{{ url_for('reset') }}" class="btn btn-light mt-3">Enter a New Name</a>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
