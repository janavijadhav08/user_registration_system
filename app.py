import streamlit as st
import psycopg2


# -------------------------------
# PostgreSQL Connection
# -------------------------------
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="python_demo",
        user="postgres",
        password="root",
        port=5432
    )


# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Registration Form",
    page_icon="📝",
    layout="centered"
)


# -------------------------------
# UI
# -------------------------------
st.title("📝 User Registration Form")
st.write("Enter your details below to register.")


with st.form("registration_form"):

    full_name = st.text_input("Full Name")

    email = st.text_input("Email Address")

    phone = st.text_input("Phone Number")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        step=1
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    submitted = st.form_submit_button("Register")


# -------------------------------
# Store Data
# -------------------------------
if submitted:

    if full_name == "" or email == "":
        st.error("Please enter your name and email.")

    else:

        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                INSERT INTO registrations
                (full_name, email, phone, age, gender)
                VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                full_name,
                email,
                phone,
                age,
                gender
            )

            cursor.execute(query, values)
            conn.commit()

            cursor.close()
            conn.close()

            st.success("Registration successful! 🎉")

        except Exception as e:
            st.error(f"Database error: {e}")