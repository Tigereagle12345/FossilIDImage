from flask import Flask, redirect, url_for, render_template, request, flash
from werkzeug.utils import secure_filename
import os
from PIL import Image
from pathlib import Path
import uuid
import guess

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['UPLOAD_FOLDER'] = "D:/Eamon/Documents/GitHub/FossilIDImage/Website/uploads"


@app.route('/')
def main():
	return redirect(url_for('home'))

@app.route('/mail')
def mail():
	return redirect("mailto:fossilai937@gmail.com")

@app.route('/home')
def home():
	return render_template("home.html", page="Home")

@app.route('/use')
def use():
	return render_template("use.html", page="Use The AI")

@app.route('/guess', methods = ['GET', 'POST'])
def make_guess():
	if request.method == 'POST':
		f = request.files['file']
		if 'file' in request.files:
			if f.filename == "":
				flash("You need to select a file!")
			else:
				if check_extension(f.filename):
					hash_value = uuid.uuid4().hex
					image_path = os.path.join("D:/Eamon/Documents/GitHub/FossilIDImage/Website/tmp", hash_value + secure_filename(f.filename))
					f.save(image_path)
					im = Image.open(image_path)
					im = im.convert("RGB")
					im_name = Path(str(image_path)).stem
					im_name = str(im_name) + ".jpg"
					im_path = os.path.join(secure_filename(im_name))
					im.save(im_path)
					pred_class = guess.predict(image_path)
					os.remove(image_path)
					os.remove(im_path)
					return render_template("guess.html", page="Upload Complete", pred_class=pred_class)
				else:
					flash("Your files are not in a valid format! Please convert them to .jpg, .jpeg or .png files.")
		else:
			flash("You need to select a file!")
	return redirect(url_for("use"))

@app.route('/upload')
def upload():
	classes = ["-Select Class-", "Ammonite", "Trilobite"]
	return render_template("upload.html", page="Upload Images", classes=classes)

@app.route('/error/<num>')
def error(num):
	message = """
Errors:

400 - Bad Request. The server cannot or will not process the request due to an apparent client error (e.g., malformed request syntax, size too large, invalid request message framing, or deceptive request routing).
404 - Not Found. The requested resource could not be found.
	"""
	return render_template("error.html", page=f"Error: {num}", message=message)

@app.route('/upload_complete', methods = ['GET', 'POST'])
def upload_complete():
	if request.method == 'POST':	
		f = request.files['file']
		im_type = request.form['im_type']
		if 'file' in request.files:
			if f.filename == "":
				flash("You need to select a file!")

			else:
				if im_type == "-Select Class-":
					flash("You need to select a class!")
				else:
					if check_extension(f.filename):
						hash_value = uuid.uuid4().hex
						image_path = os.path.join(app.config['UPLOAD_FOLDER'], hash_value + secure_filename(f.filename))
						f.save(image_path)
						im_path = preprocess(image_path, im_type)
						file_list = open("images.txt", "a")
						file_list.write(str(im_path) + "\n")
						file_list.close()
						return render_template("upload_complete.html", page="Upload Complete")
					else:
						flash("Your files are not in a valid format! Please convert them to .jpg, .jpeg or .png files.")
		else:
			flash("You need to select a file!")
	return redirect(url_for("upload"))
	#return im_type + " " + str(f)

def check_extension(filename):
	allowed_ext = {"png", "jpg", "gif", "heic", "jpeg", "raw"}
	ext = filename[filename.rindex(".")+1:]
	if ext in allowed_ext:
		return True
	else:
		return False

def preprocess(image_path, im_type):
	# Opens a image in RGB mode
	im = Image.open(image_path)
	im = im.convert("RGB")
	im = im.resize((180, 180))
	im_name = Path(str(image_path)).stem
	im_name = str(im_name) + ".jpg"
	im_path = os.path.join(app.config['UPLOAD_FOLDER'] + "/" + im_type + "/" + secure_filename(im_name))
	im.save(im_path)
	if not image_path[image_path.rindex(".")+1:] in ["jpg", "jpeg"]:
		os.remove(image_path)
	return im_path


if __name__ == '__main__':
	app.debug = True
	app.run()
	app.run(debug = True)
