from main import app
import pyvibe as pv

# rotas
@app.route('/')
def index():
    page = pv.Page('Home')
    page.add_header('Hello World')
    return page.to_html()

@app.route('/page2')
def page2():
    page = pv.Page('Home2')
    page.add_header('Hello World')
    return page.to_html()