import streamlit as st
from formulae import Quadratic,loadlottie,timedtext
from datetime import date
from streamlit_lottie import st_lottie
import time
import matplotlib.pyplot as plt
import numpy as np



st.set_page_config(page_title="Quadratics X",page_icon="Ashupagecon.jpg")
st.logo("Ashulogo.jpg",icon_image="Ashulogo.jpg",size="large")
password = "27022011ASHU-xyproject-17.519268,78.3901018,int-i5,30.08.2025,vs,27022011"

if "login" not in st.session_state:
    st.session_state.login = False


if "show_lottie" not in st.session_state:
    st.session_state.show_lottie = True

if "lottie_done" not in st.session_state:
    st.session_state.lottie_done = False    


if "page" not in st.session_state:
    st.session_state.page = "numpad"

if "code" not in st.session_state:
    st.session_state.code = False

if "pas" not in st.session_state:
    st.session_state.pas = ""

if "name" not in st.session_state:
    st.session_state.name = ""

if "dob" not in st.session_state:
    st.session_state.dob = ""

if "email" not in st.session_state:
    st.session_state.email = ""

def lottieweb():
    
    lottie = loadlottie("https://lottie.host/bf8b2dbc-69ca-4ac4-a4b3-c85eb074d413/ihocoQv9YR.json")
    
    if lottie:
            st_lottie(lottie,height=500,width=500,reverse=True,quality="high")
    else:
            st.error("error")
    time.sleep(4.45)  
    st.session_state.lottie_done = True
    st.session_state.show_lottie = False
    st.rerun()
   
details = {} 
def sublogin():
 
    with st.form("details"):
        details["s"] = st.text_input("Name")
        details["d"] = st.date_input("date of birth",min_value=date(1800,1,1),max_value=date.today())
        details["f"] = st.text_input("email")
        sub = st.form_submit_button("submit")
        
        if sub:
            if not all(details.values()):
                st.warning("Please fill every details")
                
                
            
            elif all(details.values()):    
                st.balloons()
                st.snow()
                st.success("success")
                st.session_state.login = True
                st.rerun()
def login():
    if st.session_state.show_lottie and not st.session_state.lottie_done:
        lottieweb()
    else: 
        sublogin()


def sub1homepage(text):
    
    x1,x2,x3,x4,c,b,a = Quadratic(text)
    col1,col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.balloons()
            st.subheader(f"*X* = {x1}")
            st.subheader(f"*X* = {x2}")
            st.subheader(f"*X* = {x3}")
            st.subheader(f"*X* = {x4}")
    with col2:

        x = np.linspace(-10, 10, 500)
        y = a*x**2 + b*x + c

        fig, ax = plt.subplots()
        ax.plot(x, y, label=f"y = {a}x² + {b}x + {c}")
        ax.axhline(0)
        ax.axvline(0)
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)
    st.divider()

    if st.button("Return"):
        st.session_state.page = "numpad"
        st.rerun()
           

def subhomepage():
    if "num" not in st.session_state:
        st.session_state.num = ""

    st.markdown("### Quadratic Builder")


    text = st.text_input("Input", st.session_state.num, disabled=True)

    def press(key):
        st.session_state.num += str(key)

    def clear():
        st.session_state.num = ""
    
    def backspace():
        st.session_state.num = st.session_state.num[:-1]

    buttons = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [".", "0", "⌫"],
        ["x","x²","+","-"],
        ["Enter"]
    ]

    for row in buttons:
        
        cols = st.columns(len(row))
        
        for i, key in enumerate(row):
            if key == "C":
                cols[i].button("Clear", on_click=clear, use_container_width=True)
            
            elif key == "⌫":
                cols[i].button("⌫", on_click=backspace, use_container_width=True)
            
            elif key == "Enter":
                if cols[i].button("enter", use_container_width=True):
                    if st.session_state.num.strip() != "":
                        st.session_state.page = "result"
                        st.rerun()
                
            else:
                cols[i].button(key, on_click=press, args=(key,), use_container_width=True)
    
    st.markdown("""
                <style>
                button {
                    height: 70px !important;
                    font-size: 24px !important;
                    border-radius: 12px !important;
                }
                div.stButton > button {
                    transition: 0.2s ease-in-out;
                }
                div.stButton > button:hover {
                    transform: scale(1.05);
                }
                </style>
                """, unsafe_allow_html=True)

    
def homepage():

        
        if st.session_state.page == "numpad":
            subhomepage()

        elif st.session_state.page == "result":
            sub1homepage(st.session_state.num)   

    

def graphs():


    st.title("📊 Interactive Quadratic Graph")

    a = st.slider("a (coefficient of X^2)", -1000.0, 1000.0, 1.0)
    b = st.slider("b (coefficent of x)", -1000.0, 1000.0, 1.0)
    c = st.slider("c (constant)", -1000.0, 1000.0, 1.0)

    x = np.linspace(-10, 10, 500)
    y = a*x**2 + b*x + c

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"y = {a}x² + {b}x + {c}")
    ax.axhline(0)
    ax.axvline(0)
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
def secret():
    st.write_stream(timedtext('''Hi if you come here might be a freiend of **Ashu** or an hacker once again welcome to the 
                    website'''))
    st.write_stream(timedtext('''This section I about the main core,brain of the website If you came upto here because of grace 
                    of **Ashu**, If you are a hacker I think you are not a pro hacker because this website dosen't Value and If you want to comment Mail:- **ashutoshreddy.g@hotmail.com**'''))
    st.code('''
import streamlit as st
from formulae import Quadratic,loadlottie,timedtext
from datetime import date
from streamlit_lottie import st_lottie
import time
import matplotlib.pyplot as plt
import numpy as np
import json


st.set_page_config(page_title="Quadratics X",page_icon="Ashupagecon.jpg")
st.logo("Ashulogo.jpg",icon_image="Ashulogo.jpg",size="large")
password = "27022011ASHU-xyproject-17.519268,78.3901018,int-i5,30.08.2025,vs,27022011"

if "login" not in st.session_state:
    st.session_state.login = False


if "show_lottie" not in st.session_state:
    st.session_state.show_lottie = True

if "lottie_done" not in st.session_state:
    st.session_state.lottie_done = False    


if "page" not in st.session_state:
    st.session_state.page = "numpad"

if "code" not in st.session_state:
    st.session_state.code = False

if "pas" not in st.session_state:
    st.session_state.pas = ""

if "name" not in st.session_state:
    st.session_state.name = ""

if "dob" not in st.session_state:
    st.session_state.dob = ""

if "email" not in st.session_state:
    st.session_state.email = ""

def lottieweb():
    
    lottie = loadlottie("https://lottie.host/bf8b2dbc-69ca-4ac4-a4b3-c85eb074d413/ihocoQv9YR.json")
    
    if lottie:
            st_lottie(lottie,height=500,width=500,reverse=True,quality="high")
    else:
            st.error("error")
    time.sleep(4.45)  
    st.session_state.lottie_done = True
    st.session_state.show_lottie = False
    st.rerun()
   
details = [st.session_state.name,st.session_state.dob,st.session_state.email]   
def sublogin():
 
    with st.form("details"):
        st.session_state.name = st.text_input("Name")
        st.session_state.dob = st.date_input("date of birth",min_value=date(1800,1,1),max_value=date.today())
        st.session_state.email = st.text_input("email")
        sub = st.form_submit_button("submit")
        print(details)
        if sub:
            if not all(details):
                st.warning("Please fill every details")
                
                
            
            elif all(details.values()):    
                st.balloons()
                st.snow()
                st.success("success")
                st.session_state.login = True
                st.rerun()
def login():
    if st.session_state.show_lottie and not st.session_state.lottie_done:
        lottieweb()
    else: 
        sublogin()
detail={
    "Name": [st.session_state.name],
    "Date of birth": [st.session_state.dob],
    "email": [st.session_state.email]
}
with open("datainfo.json","w") as f:
    json.dump(detail,f)   


def sub1homepage(text):
    
    x1,x2,x3,x4,c,b,a = Quadratic(text)
    col1,col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.balloons()
            st.subheader(f"*X* = {x1}")
            st.subheader(f"*X* = {x2}")
            st.subheader(f"*X* = {x3}")
            st.subheader(f"*X* = {x4}")
    with col2:

        x = np.linspace(-10, 10, 500)
        y = a*x**2 + b*x + c

        fig, ax = plt.subplots()
        ax.plot(x, y, label=f"y = {a}x² + {b}x + {c}")
        ax.axhline(0)
        ax.axvline(0)
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)
    st.divider()

    if st.button("Return"):
        st.session_state.page = "numpad"
        st.rerun()
           

def subhomepage():
    if "num" not in st.session_state:
        st.session_state.num = ""

    st.markdown("### Quadratic Builder")


    text = st.text_input("Input", st.session_state.num, disabled=True)

    def press(key):
        st.session_state.num += str(key)

    def clear():
        st.session_state.num = ""
    
    def backspace():
        st.session_state.num = st.session_state.num[:-1]

    buttons = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [".", "0", "⌫"],
        ["x","x²","+","-"],
        ["Enter"]
    ]

    for row in buttons:
        
        cols = st.columns(len(row))
        
        for i, key in enumerate(row):
            if key == "C":
                cols[i].button("Clear", on_click=clear, use_container_width=True)
            
            elif key == "⌫":
                cols[i].button("⌫", on_click=backspace, use_container_width=True)
            
            elif key == "Enter":
                if cols[i].button("enter", use_container_width=True):
                    if st.session_state.num.strip() != "":
                        st.session_state.page = "result"
                        st.rerun()
                
            else:
                cols[i].button(key, on_click=press, args=(key,), use_container_width=True)
    
    st.markdown("""
                <style>
                button {
                    height: 70px !important;
                    font-size: 24px !important;
                    border-radius: 12px !important;
                }
                div.stButton > button {
                    transition: 0.2s ease-in-out;
                }
                div.stButton > button:hover {
                    transform: scale(1.05);
                }
                </style>
                """, unsafe_allow_html=True)

    
def homepage():

        
        if st.session_state.page == "numpad":
            subhomepage()

        elif st.session_state.page == "result":
            sub1homepage(st.session_state.num)   

    

def graphs():


    st.title("📊 Interactive Quadratic Graph")

    a = st.slider("a (controls opening)", -5.0, 5.0, 1.0)
    b = st.slider("b (controls tilt)", -10.0, 10.0, 0.0)
    c = st.slider("c (vertical shift)", -10.0, 10.0, 0.0)

    x = np.linspace(-10, 10, 500)
    y = a*x**2 + b*x + c

    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"y = {a}x² + {b}x + {c}")
    ax.axhline(0)
    ax.axvline(0)
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
def secret():
    st.write_stream(timedtext("Hi if you come here might be a freiend of **Ashu** or an hacker once again welcome to the 
                    website"))
    st.write_stream(timedtext("This section I about the main core,brain of the website If you came upto here because of grace 
                    of **Ashu**, If you are a hacker I think you are not a pro hacker because this website dosen't Value and If you want to comment Mail:- **ashutoshreddy.g@hotmail.com**"))
    st.code("",language="python")
def code1(pas):
    if pas == password:
        secret()
    else:
        st.write("For password Mail: **ashutoshreddy.g@hotmail.com**")

def code2():
    col1,col2 = st.columns(2)
    with col1:    
        pas = st.text_input("Enter the codepass",type="password") 
        sv = st.button("submit")
        if sv:
            st.session_state.pas = pas
            st.session_state.code = True
    with col2:
        st.image("quadratic.jpg")
    
def code():    
    if st.session_state.code == False:
        code2()
    else:
        code1(pas=st.session_state.pas)

if st.session_state.login == False:
    login()
else:    
    pages = st.navigation([st.Page(homepage,title="Solver",icon=":material/home:"),   
            st.Page(graphs,title="📊Graphs"),
            st.Page(code,title="Code"),
            
    ],position="top")
    
    pages.run()
            

    
            ''',language="python")
def code1(pas):
    if pas == password:
        secret()
    else:
        st.write("For password Mail: **ashutoshreddy.g@hotmail.com**")

def code2():
    col1,col2 = st.columns(2)
    with col1:    
        pas = st.text_input("Enter the codepass",type="password") 
        sv = st.button("submit")
        if sv:
            st.session_state.pas = pas
            st.session_state.code = True
    with col2:
        st.image("quadratic.png")
    
def code():    
    if st.session_state.code == False:
        code2()
    else:
        code1(pas=st.session_state.pas)

if st.session_state.login == False:
    login()
else:    
    pages = st.navigation([st.Page(homepage,title="Solver",icon=":material/home:"),   
            st.Page(graphs,title="📊Graphs"),
            st.Page(code,title="Code"),
            
    ],position="top")
    
    pages.run()
            

