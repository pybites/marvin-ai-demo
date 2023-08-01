
import streamlit as st
from ai import BirthdayContact, generate_wish

# from message import send_whatsapp_message

if "birthday_contacts" not in st.session_state:
    st.session_state.birthday_contacts : list[BirthdayContact] = []

st.write("Enter information about the contact you want to be reminded of:")

txt = st.text_area("E.g. 'Tom is a school friend of mine that was born on June 16, 1994'")

if st.button("Submit"):
    birthday_contact = BirthdayContact(txt)
    
    st.session_state.birthday_contacts.append(birthday_contact)

st.write("Birthday Contacts:")
for contact in st.session_state.birthday_contacts:
    st.write(contact)

if st.button("Generate birthday wishes!"):
    for birthday_contact in st.session_state.birthday_contacts:
        st.write(generate_wish(birthday_contact=birthday_contact))


# if st.button("Send messages to whatsapp"):
#     for birthday_contact in st.session_state.birthday_contacts:
#         wish = generate_wish(birthday_contact=birthday_contact)
#         send_whatsapp_message(wish, birthday_contact.telephone_number)
