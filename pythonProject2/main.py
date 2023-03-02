from flask import Flask, render_template, request, escape

def search4letters(phrase: str, letters: str='aeiou') -> set:
    return set(letters).intersection(set(phrase))

app = Flask(__name__)
@app.route('/')
def hello()->str:
    return 'Hello from Flask'

@app.route('/viewlog')
def view_the_log()-> 'html':
    contents=[]
    with open('log.txt') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                 contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Result')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)

@app.route('/cheese')
def cheese()->'html':
    return render_template('cheese.html',
                           the_title="Текст отправки")

@app.route('/cheese_results', methods=['POST'])
def cheesePost()->'html':
    your_pet=request.form['your_pet']
    return render_template('cheese-result.html',
                           your_pet=your_pet)

@app.route('/test')
def test()->'html':
    return render_template('test.html',
                           the_title="Текст отправки")

@app.route('/test_results', methods=['POST'])
def testPost()->'html':
    your_name=request.form['your_name']
    return render_template('test-result.html',
                           your_name=your_name)

def log_request(req:'flask_request', res:str)->None:
    with open('log.txt', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent,res,file=log,sep='|')

@app.route('/search4', methods=['POST'])
def do_search()->'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    result = str(search4letters(phrase, letters))
    log_request(request, result)
    return render_template('result.html',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_title=title,
                            the_result=result,)
@app.route('/entry')
def entry_page()->'html':
    return render_template('entry.html', the_title="Welcome")
app.run()