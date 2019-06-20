from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import main
    app.register_blueprint(main)

    return app

html = """
<!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Page Title</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel="icon" href="data:;base64,iVBORw0KGgo=">
        <!--<link rel='stylesheet' type='text/css' media='screen' href='main.css'>
        <script src='main.js'></script>-->
    </head>
    <body>
        <h1>Hola mundo</h1>
    </body>
    </html>
"""