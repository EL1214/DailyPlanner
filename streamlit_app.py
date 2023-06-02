import streamlit as st

title = st.text_input('Event Title','Enter your event title here')

option = st.selectbox(
    'Would you like to be reminded the event again after 5 mins?',
    ('Yes, please', 'No, Thank you'))
#date input
import datetime

date = st.date_input('Choose a date for the event',
                     datetime.date(2020,12,14))
st.write('Your event date is recorded. Event Date:',date)

addnote = st.text_area('Do you have any additional notes for yourself regarding the event',
                       ''' Write some additional notes(optional)''')
