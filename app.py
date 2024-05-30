from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form_handler():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        mobile = request.form.get('mobile')

        # Here you can process the received data, e.g., save it to a database.

        return 'Form submitted successfully!'
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)