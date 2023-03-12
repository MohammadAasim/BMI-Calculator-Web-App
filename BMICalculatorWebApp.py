import streamlit as st

#title of calculator
st.title('Welcome to BMI Calculator')

#take weight in kgs 
weight = st.number_input("Enter your weight (in Kgs)")

#take height by radio button
status = st.radio("Select your height format : ",('cm','meters','feet'))

#initialize bmi to None
bmi = None

if(status=='cm'):
    height = st.number_input('Centimeters')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter Some value of height")

elif(status=='meters'):
    height = st.number_input('Meters')
    try:
        bmi = weight / (height**2)
    except:
        st.text("Enter Some value of height")

else:
    height = st.number_input('Feet')
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter Some value of height")

if(st.button('calculate BMI')):
    if bmi is not None:
        st.text('Your BMI Index is {}'.format(bmi))
    else:
        st.text('Enter valid height and weight')

#check if bmi is defined before using it in if statements
if bmi is not None:
    if(bmi < 16):
        st.error('You are Extremely Underweight')
    elif(bmi >= 16 and bmi < 18.5):
        st.warning('You are Underweight')
    elif(bmi >= 18.5 and bmi < 25):
        st.success('Healthy')
    elif(bmi >= 25 and bmi < 30):
        st.warning('Overweight')
    elif(bmi >= 30):
        st.error('Extremely Overweight')
