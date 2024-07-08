from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_value = request.form['input_field']
    # Process the input value with your Python code
    output_value = your_python_function(input_value)
    print(input_value)
    return render_template('index.html', output_value=output_value)

def your_python_function(input_value):
    # Your Python code goes here
    return f"Processed value: {input_value}"

if __name__ == '__main__':
    app.run(debug=True)
