from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from Log_Writer.logger import App_Logger
from Base64.Decoder import decodeImage
from Preprocess.preprocessor import process
from Model_Loader.load_model import load
import torch


app = Flask(__name__)
CORS(app)

logger = App_Logger()


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def homePage():
    try:
        logger.log("Rendered Home Page Successfully")
        return render_template('index.html')
    except Exception as e:
        return print(e)


@app.route('/prediction', methods=['POST'])
@cross_origin()
def index():
    try:
        if request.method == 'POST':

            # Collect BAse64 string
            base64 = request.form['image']
            logger.log("Collected Base64 string")

            # Decode base64 string & get PIL image
            image = decodeImage(base64)

            # Convert to Image array & then to tensor & preprocess
            image=process(image)

            # Load Model
            # model=load(PATH='model_weights/best_wts_76.263%06-01-2022__09_27.pth')
            model = load(PATH='model_weights/best_model_76.263%06-01-2022__09_27.pth')

            # Prediction
            with torch.no_grad():
                outputs = model(image)
                _, pred = torch.max(outputs, 1)

            # {'glioma_tumor': 0, 'meningioma_tumor': 1, 'no_tumor': 2, 'pituitary_tumor': 3}
            prediction = "shows no indication of Tumor"
            if pred == 0:
                prediction = "shows indication of Glioma Tumor"
            if pred == 1:
                prediction = "shows indication of Meningioma Tumor"
            if pred == 2:
                prediction = "shows no indication of Tumor"
            if pred == 3:
                prediction = "shows indication of Pituitary Tumor"

            logger.log("Prediction Successful")
            return render_template("results.html", prediction=prediction, base64=base64)
        else:
            logger.log("Did not get POST request\n")
            return render_template("index.html")
    except Exception as e:
        logger.log("ERROR : Some Error Occurred\n")
        return print(f"Error : {e}")


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=8001)
