from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

df = pd.read_pickle('result.pkl')
df = pd.DataFrame(df)

#Home Page
@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('test.html')

#Result Page
@app.route('/result', methods=['POST', 'GET'])
def result():
    #if request.method == 'POST':
    #return df.to_html(header="true", table_id="table")
    return render_template('test2.html',  tables=[df.to_html(classes='data', header="true")])


if __name__ == '__main__':
    app.run(port=5000, debug=True)