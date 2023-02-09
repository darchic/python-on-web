from flask import Flask, render_template, request

def search4Letters(phrase: str, letters: str='aeiou') -> set:
    return set(letters).intersection(set(phrase))

app = Flask(__name__)
@app.route('/')
def hello()->str:
    return 'Hello from Flask'
@app.route('/search4', methods=['POST'])
def do_search()-> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str (search4Letters(phrase, letters))
    return render_template('result.html',
                   the_phrase=phrase,
                   the_letters=letters,
                   the_title=title,
                   the_results=results)
@app.route('/entry')
def entry_page()->'html':
    return render_template('entry.html',
                           the_title="Welcome")
app.run()





