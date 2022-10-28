# Import needed functionality
from flask import render_template, Flask, request, redirect
import markdown
from os.path import exists

# Create flask object inherited from Flask
app = Flask(__name__, 
        static_url_path='/static/', static_folder='static')

# Load plugins
import plugins.date as plugin_date

# Get page content and return ready template
def display_page(page):
    if exists('content/'+page+'.md'):
        return render_template('page.html', content=get_content(page))
    else:
        return "File not found <div class='date'>" + plugin_date.css + plugin_date.action() + '</date>'


# Get markdown file and return html
def get_content(page):
    return markdown.markdown(open('content/'+page+'.md', 'r').read())

# Bind / request to function index
@app.route('/')
def index():
    # Return simple string variable
    return display_page('index')

@app.route('/<page>')
def content_page(page):
    return display_page(page)

# If ran from command line start development server on
# port 5000
if __name__ == "__main__":
    # <1024 require admin access
    app.run(port=5000, debug=True)