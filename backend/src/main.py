from flask import Flask, render_template
from api import api_bp
from flask_cors import CORS

app = Flask(__name__, static_folder='../../frontend/dist/static', template_folder='../../frontend')
app.register_blueprint(api_bp)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
