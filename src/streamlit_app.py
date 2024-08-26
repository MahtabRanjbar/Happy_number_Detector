import streamlit as st
import plotly.express as px

def is_happy(n: int) -> (bool, list):
    """Determine if a number is a happy number and return the process."""
    seen = set()
    process = []  # To store the process for visualization
    while n != 1 and n not in seen:
        seen.add(n)
        process.append(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    process.append(n)
    return n == 1, process

def batch_check(numbers):
    """Batch check happy numbers from a list of integers."""
    return {number: is_happy(number)[0] for number in numbers}

def visualize_happy_process(process):
    """Create an interactive plot showing the process of getting to a happy number."""
    df = {"Step": list(range(1, len(process) + 1)), "Number": process}
    fig = px.line(df, x="Step", y="Number", markers=True, title="Happy Number Process",
                  labels={"Step": "Step Number", "Number": "Intermediate Values"})
    fig.update_traces(marker=dict(size=10, symbol="circle"), line=dict(color="green", width=3))
    st.plotly_chart(fig)


def main():
    st.title("Happy Number Checker 😃")
    st.write("""
    This app helps you check if a number is a happy number or not. 
    You can test a single number or upload a file to check multiple numbers. Let's see some happy numbers! 🎉
    """)

    # Single Number Check
    st.header("🔢 Check a Single Number")
    number = st.number_input("Enter a number:", min_value=1, step=1)
    if st.button("Check if Happy"):
        is_happy_number, process = is_happy(number)
        if is_happy_number:
            st.success(f"🎉 {number} is a happy number! 😊")
            st.write("Here’s how it works:")
            st.write(" ➡️ ".join(str(num) for num in process))
            visualize_happy_process(process)
        else:
            st.error(f"😔 {number} is not a happy number.")
            st.write("Here’s the process it followed:")
            st.write(" ➡️ ".join(str(num) for num in process))
            visualize_happy_process(process)

    # Batch Check from File
    st.header("📂 Batch Check from File")
    uploaded_file = st.file_uploader("Upload a file with numbers (one number per line):", type=["txt"])

    if uploaded_file is not None:
        try:
            # Read and process the file
            numbers = [int(line.strip()) for line in uploaded_file]
            results = batch_check(numbers)
            st.write("Results:")
            for number, happy in results.items():
                st.write(f"✅ {number} is {'a happy' if happy else 'not a happy'} number.")
        except ValueError:
            st.error("🚫 The file contains invalid data. Please make sure it only contains integers.")

if __name__ == "__main__":
    main()
