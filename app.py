
import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('model.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not heart disease'
    else:
        return 'The person is heart disease'

    
def main():
    
    
    # giving a title
    st.title('heart disease Prediction Web App')
    
    
    # getting the input data from the user
    
    
    age = st.text_input('age')
    sex = st.text_input('sex')
    trestbps = st.text_input('trestbps')
    chol = st.text_input('chol')
    fbs = st.text_input('fbs')
    restecg = st.text_input('restecg')
    thalach = st.text_input('thalach')
    exang = st.text_input('exang')
    oldpeak = st.text_input('oldpeak')
    ca = st.text_input('ca')
    cp_0 = st.text_input('cp_0')
    cp_1 = st.text_input('cp_1')
    cp_2 = st.text_input('cp_2')
    cp_3 = st.text_input('cp_3')
    thal_0 = st.text_input('thal')
    thal_1 = st.text_input('thal_1')
    thal_2 = st.text_input('thal_2')
    thal_3 = st.text_input('thal_3')
    slope_0 = st.text_input('slope_0')
    slope_1 = st.text_input('slope_1')
    slope_2 = st.text_input('slope_2')
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('heart disease Test Result'):
        diagnosis = diabetes_prediction([age,sex,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,ca,cp_0,cp_1,cp_2,cp_3,thal_0,thal_1,thal_2,thal_3,slope_0,slope_1,slope_2
])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
