from flask import Flask,render_template,request,escape,session
from cheker import check_logged_in

def log_request(req:'flask_request',res:str)->None:
    with open('vsearch.log','a') as log:
        print(req,res,file=log)

def search4letters(pharse:str,letters:str='aeiou')->set:
    return set(letters).intersection(set(pharse))

app=Flask(__name__)
app.secret_key='YouWillNeverGuess'
@app.route('/search4',methods=['POST'])
def do_search() -> 'html':
    pharse=request.form['pharse']
    letters=request.form['letters']
    title='Here are your results:'
    results=str(search4letters(pharse,letters))
    log_request(request,results)
    return render_template('result.html',
                            the_title=title,
                            the_pharse=pharse,
                            the_letters=letters,
                            the_results=results)
@app.route('/')
@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html',the_title='Welcome to search4letters on the web!')
@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='Viev Log', the_row_titles=titles,the_data=contents,)

@app.route('/login')
def do_loggin()->str:
    session['logged_in']=True
    return 'You are logged in'

@app.route('/logout')
def do_logout()->str:
    session.pop('logged_in')
    return 'You are logged out'
if __name__ == '__main__':
    app.run(debug=True)