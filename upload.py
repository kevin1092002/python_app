from flask import Blueprint,render_template,request,redirect,flash,current_app,url_for
from werkzeug.utils import secure_filename
import os
uploads = Blueprint('uploads', __name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg']) #allowed extension from the task description
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@uploads.route('/upload_page')
def upload():
    # Handle logo upload and image processing
    # config_width =current_app.config['MAX_LOGO_WIDTH']
    # print (current_app.config['MAX_LOGO_WIDTH'])
    # config_height= current_app.config['MAX_LOGO_HEIGTH']
    return render_template('upload.html',max_widths=current_app.config['MAX_LOGO_WIDTH'], max_height=current_app.config['MAX_LOGO_HEIGTH'])
    # return send_file('path_to_final_image')@views.route('/upload')

@uploads.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        print(file.filename)
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        config_width =current_app.config['MAX_LOGO_WIDTH']
        config_height= current_app.config['MAX_LOGO_HEIGTH']
        #print('upload_image filename: ' + filename) 
        flash('Image successfully uploaded and displayed below')
        return render_template('upload.html', filename=filename, max_widths = config_width, max_heights =config_height )
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
    
@uploads.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@uploads.route('/resize')
def resize():
    #print('display_image filename: ' + filename)
    config = []
    config.append()
    config.append()

    return config