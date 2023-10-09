from flask import Flask, render_template, request, jsonify
from typing import List

app = Flask(__name__)

class Choice:
    def __init__(self, id:int, name: str):
        self.id = id
        self.name = name

class App:
    def __init__(self):
        self.selected = None
        self.choices: List[Choice] = [Choice(1, "Apache Hadoop"),
                                      Choice(2, "Apache Spark"),
                                      Choice(3, "Apache Jupyter Notebook"),
                                      Choice(4, "SonarQube and SonarScanner")]

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
    app.run()
