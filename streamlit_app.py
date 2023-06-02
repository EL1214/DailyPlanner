import streamlit as st

title = st.text_input('Event Title','Enter your event title here')

#date input
import datetime

date = st.date_input('Choose a date for the event',
                     datetime.date(14,12,2020))
st.write('Your event date is recorded. Event Date:',date)

addnote = st.text_area('Do you have any additional notes for yourself regarding the event',
                       ''' Write some additional notes(optional)''')
