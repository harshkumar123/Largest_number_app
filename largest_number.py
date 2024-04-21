import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

def main():
    st.title("Find the Largest Among Three Numbers")
    
    st.write("Enter three numbers below:")
    
    x = st.number_input("Enter first number", value=0)
    y = st.number_input("Enter second number", value=0)
    z = st.number_input("Enter third number", value=0)
    
    if st.button("Get Largest"):
        largest = find_largest(x, y, z)
        st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
