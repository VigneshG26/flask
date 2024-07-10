from flask import Flask, abort, render_template

from database import result_dicts

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Full Stack Developer',
        'location': 'Chennai',
        'salary': '12LPA'
    },
    {
        'id': 2,
        'title': 'Front End Developer',
        'location': 'Bangalore',
        'salary': '5LPA'
    },
    {
        'id': 3,
        'title': 'Back End Developer',
        'location': 'Bangalore',
        'salary': '7LPA'
    }
]

Projects = result_dicts

# Projects = [
#     {
#         'id': 1,
#         'img_src':'../static/images/KrishFashionn.jpg',
#         'alt': 'krish',
#         'lang_used': ['HTML','CSS','JS'],
#         'proj_desc1': 'krish Fashion, your premier shopping haven is here.',
#         'proj_desc2': 'Shop Now!',
#         'code_link': 'https://github.com/VigneshG26/KrishFashion',
#         'live_link': 'https://vigneshg26.github.io/KrishFashion/'
#     },
#     {
#         'id': 2,
#         'img_src':'../static/images/Glow Organic.jpg',
#         'alt': 'Glow Organic',
#         'lang_used': ['HTML','CSS','JS'],
#         'proj_desc1': 'Enhance your health! Purchase our organic products.',
#         'proj_desc2': 'Shop Now!',
#         'code_link': 'https://github.com/VigneshG26/Glow-Organic',
#         'live_link': 'https://vigneshg26.github.io/Glow-Organic/'
#     },
#     {
#         'id': 3,
#         'img_src':'../static/images/fetch-products.jpg',
#         'alt': 'Fetch Products',
#         'lang_used': ['HTML','CSS','JS','API'],
#         'proj_desc1': 'Fetched products data from external source using ',
#         'proj_desc2': 'Fetch API.',
#         'code_link': 'https://github.com/VigneshG26/Fetching-Data-from-External-Server',
#         'live_link': 'https://vigneshg26.github.io/Fetching-Data-from-External-Server/'
#     },
#     {
#         'id': 4,
#         'img_src':'../static/images/blackpink.jpg',
#         'alt': 'Blackpink',
#         'lang_used': ['HTML','CSS','JS'],
#         'proj_desc1': 'Blackpink\'s world, Welcome to a fan\'s paradise. ',
#         'proj_desc2': 'Explore Now!.',
#         'code_link': 'https://github.com/VigneshG26/Blackpink-Webpage',
#         'live_link': 'https://vigneshg26.github.io/Blackpink-Webpage/'
#     },
#     {
#         'id': 5,
#         'img_src':'../static/images/Jazzle.jpg',
#         'alt': 'Jazzle',
#         'lang_used': ['HTML','CSS','JS'],
#         'proj_desc1': 'Jazzle your one stop shopping is here.',
#         'proj_desc2': 'Shop Now!.',
#         'code_link': 'https://github.com/VigneshG26/E-Commerce-Website',
#         'live_link': 'https://vigneshg26.github.io/E-Commerce-Website/'
#     }
# ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Careers')
def careers():
    return render_template('careers.html', jobs = JOBS)

@app.route('/Projects')
def projects():
    return render_template('projects.html', projects = Projects)

@app.route('/Details/<int:id>')
def details(id):  
    try:
        data = Projects[id - 1]
        return render_template('details.html', data = data)
    except Exception as e:
        return "Page Not Found 404"


if __name__ == '__main__':
    app.run(debug=True)