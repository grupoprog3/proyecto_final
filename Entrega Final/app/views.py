from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'apodo': 'AzaelI'}
	return render_template('index.html', titulo='Inicio', user=user)
