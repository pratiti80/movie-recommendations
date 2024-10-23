from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'c2aedca4f9a18e61a95892ff8a18f401'
BASE_URL = 'https://api.themoviedb.org/3'


@app.route('/')
def index():
  return render_template('index_html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('movie_query')
        search_url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={query}"
        response = requests.get(search_url)
        data = response.json()
        return render_template('search_results.html', movies=data['results'], query=query)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
  




