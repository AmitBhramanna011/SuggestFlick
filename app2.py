from flask import Flask, render_template, request
import requests

from p import process

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def process_input():
    user_input = request.form['movie']
    result = process(user_input)
    if not result:
        # Handle the case where no recommendations are found
        return render_template('no_recommendations.html')
    poster_url=[]
    for i in range(len(result)):
        response=requests.get('https://www.omdbapi.com/?s='+result[i][1]+'&y='+result[i][0]+'&apikey=855c3c5f')
        if response.status_code == 200:
            movie_json = response.json()

            # Check if the 'Search' key is present in the JSON response
            if 'Search' in movie_json:
                # Check if there is at least one result in the 'Search' list
                if len(movie_json['Search']) > 0:
                    poster_url.append(movie_json['Search'][0]['Poster'])
                else:
                    poster_url.append("No poster available")
            else:
                poster_url.append("No 'Search' key in API response")
        else:
            poster_url.append(f"Error: {response.status_code}")
        
    print(poster_url)
    print(movie_json)
    # print(len(poster_url))
    return render_template('result.html', data=result,poster_url=poster_url)

if __name__ == '__main__':
    app.run(debug=True)
