from flask import Flask, render_template, request
import process
import test_function
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        info = request.form['good_keyword']
        bad_info = request.form['bad_keyword']
        length = request.form['length']
        try:
            length = int(length)
        except ValueError:
            return render_template('index.html')
        result = []

        l, vector, base = process.get_corpus(good_keywords = info, bad_keywords = bad_info)
        if l == None and vector == None and base == None:
            print('<p>bad keywords</p>')
            return render_template('index.html')
        query = request.form['text'].split()
        test_function.my_print(query)
        res = process.analysis_data(l, vector, base, query, int(length))
        for i in res:
            result.append(l[i])
        if result == None or len(result) == 0:
            for i in range(int(length)):
                result.append(None)
        return render_template("result.html",result = result)



if __name__ == '__main__':
    app.run(debug = True)