import streamlit as st
from streamlit_option_menu import option_menu

# st.title("Hello World")
# st.header("📝This is a header📝")
# st.subheader("This is a subheader")
# st.write("✔️  This is a text")
# st.text("This is a text")
# st.code("""

# #include <stdio.h>

# int main() {
#   printf("Hello World!");
#   return 0;
# }

# """,language="c")

# st.latex(r"E=mc^2")
# st.metric(label="Temperature",value="70°F",delta="-1.2°F")
# st.progress(0.5)
# st.progress(0.5,text="50%")

# st.progress(0.5,text="50%")

# st.text_input("Enter your name")
# st.number_input("Enter your age")
# st.date_input("Enter your date of birth")
# st.checkbox("I agree")
# st.radio("Select your gender",["Male","Female","Other"])
# st.multiselect("Select your country",["United States","Canada","United Kingdom","Australia"])
# st.slider(label="Select your age",min_value=0,max_value=100,value=25)

with st.sidebar:
    
    select = option_menu(
        menu_title="Vinsup",
        options=['Home','About','Service'],
        icons=['house','file-person','gear']
                
    )
    
if select == "Home":
    st.title("Welcome to Home")
    st.divider()
    col1,col2 = st.columns(2)
    with col1:
        a = st.text_input("Name")
        if st.button("Click"):
         st.write(a)
         st.balloons()
    with col2:
        st.text_input("Email")
        st.image('https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png')

elif select == "About":
    st.title("Welcome to About")

elif select == "Service":
    st.title("Welcome to Service")