from flask import Flask
from math import factorial

app = Flask(__name__)

@app.route('/factorial/<number>')
def get_factorial(number):
    number = int(number)
    try:
        result = factorial(number)
    except Exception as error:
        return f"{number} is an illegal value: {error}"
    return f"la respuesta es {int(result)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)