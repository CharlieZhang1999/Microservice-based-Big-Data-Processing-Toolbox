from flask import Flask, render_template, request, jsonify, redirect
from typing import List

app = Flask(__name__)

class Choice:
    def __init__(self, id:int, name: str, ip: str, port: int):
        self.id = id
        self.name = name
        self.ip = ip
        self.port = port

class App:
    def __init__(self):
        self.selected = None
        self.choices: List[Choice] = [Choice(1, "Apache Hadoop", "34.67.231.30", 9870),
                                      Choice(2, "Apache Spark", "34.67.109.128", 8080),
                                      Choice(3, "Jupyter Notebook", "34.136.154.200", 8888),
                                      Choice(4, "Jenkins", "35.184.215.158", 8080),
                                      Choice(5, "SonarQube", "34.134.30.188", 9000)]

    def select(self, choice: Choice):
        self.selected = choice
    
    def get_choice_by_id(self, id) -> Choice:
        for choice in self.choices:
            if choice.id == id:
                return choice
        return None

my_app = App()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', choices=my_app.choices)

@app.route('/', methods=['POST'])
def select():
    choice_id = int(request.form.get('choice_id'))
    selected = my_app.get_choice_by_id(choice_id)
    my_app.select(selected)
    return render_template('index.html', choices=my_app.choices, selected=selected)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
