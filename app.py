import streamlit as st
import numpy as np
import joblib

# Load your trained SVM model (make sure to specify the correct path to your model file)
model = joblib.load('svm_model.pkl')

# Function to predict student status
def predict_student_status(inputs):
    # Convert inputs to a NumPy array and reshape to match the model's expected input
    input_array = np.array(inputs).reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_array)

    return prediction[0]

# Streamlit app layout
st.title('Student Status Prediction App')

# Input fields
marital_status = st.selectbox("Marital Status", [1, 2, 3, 4, 5, 6])
application_mode = st.selectbox("Application Mode", [1, 2, 5, 7, 10, 15, 16, 17, 18, 26, 27, 39, 42, 43, 44, 51, 53, 57])
application_order = st.number_input("Application Order", min_value=0, max_value=9)
course = st.selectbox("Course", [33, 171, 8014, 9003, 9070, 9085, 9119, 9130, 9147, 9238, 9254, 9500, 9556, 9670, 9773, 9853, 9991])
daytime_evening_attendance = st.selectbox("Daytime/Evening Attendance", [1, 0])
previous_qualification = st.selectbox("Previous Qualification", [1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 15, 19, 38, 39, 40, 42, 43])
previous_qualification_grade = st.number_input("Previous Qualification Grade", min_value=0, max_value=200)
nationality = st.selectbox("Nationality", [1, 2, 6, 11, 13, 14, 17, 21, 22, 24, 25, 26, 32, 41, 62, 100, 101, 103, 105, 108, 109])
mothers_qualification = st.selectbox("Mother's Qualification", [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 18, 19, 22, 26, 27, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44])
fathers_qualification = st.selectbox("Father's Qualification", [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 18, 19, 20, 22, 25, 26, 27, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44])
mothers_occupation = st.selectbox("Mother's Occupation", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 122, 123, 125, 131, 132, 134, 141, 143, 144, 151, 152, 153, 171, 173, 175, 191, 192, 193, 194])
fathers_occupation = st.selectbox("Father's Occupation", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 90, 99, 101, 102, 103, 112, 114, 121, 122, 123, 124, 131, 132, 135, 141, 143, 144, 151, 152, 153, 154, 161, 163, 171, 172, 174, 175, 181, 182, 183, 192, 193, 194, 195])
admission_grade = st.number_input("Admission Grade", min_value=0, max_value=200)
displaced = st.selectbox("Displaced", [1, 0])
educational_special_needs = st.selectbox("Educational Special Needs", [1, 0])
debtor = st.selectbox("Debtor", [1, 0])
tuition_fees_up_to_date = st.selectbox("Tuition Fees Up To Date", [1, 0])
gender = st.selectbox("Gender", [1, 0])
scholarship_holder = st.selectbox("Scholarship Holder", [1, 0])
age_at_enrollment = st.number_input("Age at Enrollment", min_value=0)
international = st.selectbox("International", [1, 0])
curricular_units_1st_sem_credited = st.number_input("Curricular Units 1st Sem Credited", min_value=0)
curricular_units_1st_sem_enrolled = st.number_input("Curricular Units 1st Sem Enrolled", min_value=0)
curricular_units_1st_sem_evaluations = st.number_input("Curricular Units 1st Sem Evaluations", min_value=0)
curricular_units_1st_sem_approved = st.number_input("Curricular Units 1st Sem Approved", min_value=0)
curricular_units_1st_sem_grade = st.number_input("Curricular Units 1st Sem Grade", min_value=0)
curricular_units_1st_sem_without_evaluations = st.number_input("Curricular Units 1st Sem Without Evaluations", min_value=0)
curricular_units_2nd_sem_credited = st.number_input("Curricular Units 2nd Sem Credited", min_value=0)
curricular_units_2nd_sem_enrolled = st.number_input("Curricular Units 2nd Sem Enrolled", min_value=0)
curricular_units_2nd_sem_evaluations = st.number_input("Curricular Units 2nd Sem Evaluations", min_value=0)
curricular_units_2nd_sem_approved = st.number_input("Curricular Units 2nd Sem Approved", min_value=0)
curricular_units_2nd_sem_grade = st.number_input("Curricular Units 2nd Sem Grade", min_value=0)
curricular_units_2nd_sem_without_evaluations = st.number_input("Curricular Units 2nd Sem Without Evaluations", min_value=0)
unemployment_rate = st.number_input("Unemployment Rate", min_value=0.0, format="%.2f")
inflation_rate = st.number_input("Inflation Rate", min_value=0.0, format="%.2f")
gdp = st.number_input("GDP", min_value=0.0, format="%.2f")

# Button to predict
if st.button('Predict'):
    inputs = [
        marital_status,
        application_mode,
        application_order,
        course,
        daytime_evening_attendance,
        previous_qualification,
        previous_qualification_grade,
        nationality,
        mothers_qualification,
        fathers_qualification,
        mothers_occupation,
        fathers_occupation,
        admission_grade,
        displaced,
        educational_special_needs,
        debtor,
        tuition_fees_up_to_date,
        gender,
        scholarship_holder,
        age_at_enrollment,
        international,
        curricular_units_1st_sem_credited,
        curricular_units_1st_sem_enrolled,
        curricular_units_1st_sem_evaluations,
        curricular_units_1st_sem_approved,
        curricular_units_1st_sem_grade,
        curricular_units_1st_sem_without_evaluations,
        curricular_units_2nd_sem_credited,
        curricular_units_2nd_sem_enrolled,
        curricular_units_2nd_sem_evaluations,
        curricular_units_2nd_sem_approved,
        curricular_units_2nd_sem_grade,
        curricular_units_2nd_sem_without_evaluations,
        unemployment_rate,
        inflation_rate,
        gdp
    ]

    prediction = predict_student_status(inputs)
    st.success(f'The predicted status is: **{prediction}**')
