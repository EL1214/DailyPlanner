import streamlit as st

title = st.text_input('Event Title','Enter your event title here')

'''alarm = st.selectbox(
    'Would you like to be reminded again after 5 minutes?'
    ['Yes','No'])'''
if alarm == 'Yes':
    st.write('This event will be alarmed twice')
else:
    st.write('This event will be alarmed only once')

#date input
import datetime

date = st.date_input('Choose a date for the event',
                     datetime.date(14,12,2020))
st.write('Your event date is recorded. Event Date:',date)

addnote = st.text_area('Do you have any additional notes for yourself regarding the event',
                       ''' Write some additional notes(optional)''')
