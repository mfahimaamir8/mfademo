import gspread
import streamlit as st  
import pandas as pd
import time 
from google.oauth2.service_account import Credentials
from google.oauth2 import service_account
#from oauth2client.service_account import ServiceAccountCredential
import streamlit.components.v1 as components
from pivottablejs import pivot_ui
from mitosheet.streamlit.v1 import spreadsheet
from pygwalker.api.streamlit import StreamlitRenderer
from st_aggrid import AgGrid
import streamlit as st
import numpy as np
import pandas as pd
from hashlib import md5
import streamlit as st







st.set_page_config(
    page_title="Streamlit Layouts Tutorial",
    page_icon=":art:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""<style> section[data-testid="stSidebar"][aria-expanded="true"]{display: none;}</style> """, unsafe_allow_html=True)


st.title("Muhammad Fahim Aamir -03336774947")
st.header("Demo App for data visualization and graphical representation, featuring data filtration through a user-friendly drag-and-drop pivot table interface. ")
st.header("Please watch the demonstration video to gain a better understanding of how to use it.")


video_file = open("videoforusetehapp.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)



client = gspread.service_account(filename='credentials.json')
#b1 = client.open('mfadata')   #qureshiandsonsinds@gmail.com
wb1 = client.open('muhammadfahim') #mfahim204s8@gmail.com
wbs1 =  wb1.get_worksheet(3)
wbs1d = pd.DataFrame(wbs1.get_all_records())
st.write(wbs1d)
st.session_state["data2"] = wbs1d

#iris = pd.read_csv(    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")
st.header("A tool for data visualization and graphical representation, featuring data filtration through a user-friendly drag-and-drop pivot table interface. ")
t = pivot_ui(wbs1d)
with open(t.src) as t:
    components.html(t.read(), width=900, height=1000, scrolling=True)

st.header("A tool for data visualization and graphical representation, featuring data filtration through a user-friendly drag-and-drop pivot table interface.  ")
#st.set_page_config(layout="wide")
#CSV_URL ='https://raw.githubusercontent.com/plotly/datasets/master/tesla-stock-price.csv'
#new_dfs, code = spreadsheet (CSV_URL)
new_dfs, code = spreadsheet (wbs1d)
#st.write(new_dfs)
#st.code(code)

#new_dfs, code = spreadsheet ('c:\mfa\mfacsv.csv')
#st.write(new_dfs)
#st.code(code)
st.header("A tool for data visualization and graphical representation, featuring data filtration through a user-friendly drag-and-drop pivot table interface. ")
pyg_app = StreamlitRenderer(wbs1d)
pyg_app.explorer()



#st.header("Data filterizatoin with Drag and Drop pivot Table user friendly  ")


#env = Environment(loader=FileSystemLoader('.'))
#template = 'table_template.html'
#template = env.get_template(table_template)

    # Render the template with the provided URL
#rendered_html = template.render(wbs1d)

    # Render the HTML content
#st.components.v1.html(rendered_html, width=1300, height=600, scrolling=True)
#render_html_template(url, template, width=1300, height=600, scrolling=True)

st.header("A tool for data visualization and graphical representation, featuring data filtration through a user-friendly drag-and-drop pivot table interface. ")

#df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(wbs1d)





#video_file1 = open("video2.mp4", "rb")
#video_bytes = video_file1.read()
#st.video(video_bytes)

#video_file2 = open("video3.mp4", "rb")
#video_bytes = video_file2.read()
#st.video(video_bytes)

