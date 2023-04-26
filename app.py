from ast import If
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# load the model from disk
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    # try:
        recieved = [int(x) for x in request.form.values()]
        k = np.array(recieved)  #final_features

        codn = bool
        
        if( (k[0]>=16) and (k[0]<=90))  :     
                codn = True                         #age
        else:     
                codn = False
                
        # for i in range(1,16):
        #     if((k[i]==0) or (k[i]==1)):     
        #             codn = codn and True   
        #     else:     
        #             codn = codn and False

        if(codn):
            model = pickle.load(open('model.pkl', 'rb'))
            transform_data_of_array = pickle.load(open('transform_data_of_array.pkl', 'rb'))
            int_features = transform_data_of_array.transform([k])
            prediction = model.predict( int_features)
            # output = round(prediction[0], 2)
            if(int(prediction)==1):
                return render_template('index.html', prediction_text='You have sugar')
            else:
                return render_template('index.html', prediction_text="You don't have sugar")
        else:
            return render_template('index.html', prediction_text='Please give correct input, all either 0 or 1 (except age b/w 16:90) {} '.format(k))
        
    # except:
        # return render_template('index.html', prediction_text='Please give correct input, all either 0 or 1 (except age b/w 5:100) $ {} '.format(codn))


if __name__ == "__main__":
   app.run(debug=True)

# app.run(host='localhost',port=80)
