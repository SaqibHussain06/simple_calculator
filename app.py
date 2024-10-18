import streamlit as st

def main():
    st.title("Simple Calculator")

    # Input fields for the numbers
    num1 = st.number_input("Enter the first number", value=0.0, step=1.0)
    num2 = st.number_input("Enter the second number", value=0.0, step=1.0)

    # Dropdown for selecting the operation
    operation = st.selectbox("Select operation", ("Addition", "Subtraction", "Multiplication", "Division"))

    # Perform the calculation
    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                st.error("Cannot divide by zero!")
                return
            result = num1 / num2

        # Display the result
        st.success(f"The result of {operation.lower()} is: {result}")

if __name__ == "__main__":
    main()
