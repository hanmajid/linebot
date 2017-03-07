from flask import Flask, url_for
app = Flask(__name__)
counter = 0

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

@app.route('/send', methods=['GET','POST'])
def api_receive():
	global counter
	counter += 1
	return 'Added to list, counter : ' + str(counter)

if __name__ == '__main__':
	# counter = 0
	print "counter : " + str(counter)
	app.run()