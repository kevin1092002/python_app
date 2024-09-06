from flask import Flask, request, render_template, send_file
import os
from datetime import datetime
from dotenv import load_dotenv, dotenv_values
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = "Application_Key" #encrypt key for session data
    USER_UPLOAD_FOLDER = 'website/static/uploads/' #The task ask to upload an application folder
 

    app.config['UPLOAD_FOLDER'] = USER_UPLOAD_FOLDER
    app.config['MAX_LOGO_WIDTH'] = 250  #Recommend logo size  
    app.config['MAX_LOGO_HEIGTH'] = 150 #Recommend logo size  
    from .view import views
    from .upload import uploads

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(uploads, url_prefix="/")

    return app
    

 





