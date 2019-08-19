from flask import Flask, render_template
import markovify

with open("cleanedtexto.txt") as f:
    	text = f.read()

app = Flask(__name__)


@app.route('/')
def title():
	
	text_model = markovify.NewlineText(text)
	# titles = (text_model.make_sentence(max_overlap_total=100, tries=1000))
	title = text_model.make_short_sentence(60).rstrip('.')
	return render_template(
		'test.html', **locals())

if __name__ == '__main__':
	app.run()
		# host='0.0.0.0', port=80)