import streamlit as st
from chatbot import get_response


st.set_page_config(page_title="College Admission Chatbot", page_icon="🎓")

st.title("🎓 College Admission Chatbot")
st.write("Ask me about courses, fees, eligibility, hostel, and admissions.")

# Chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# User input
user_input = st.text_input(
    "You:",
    placeholder="e.g. What is the eligibility for B.Tech?"
)

if st.button("Send") and user_input:
    response = get_response(user_input)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", response))

# Display chat
for sender, message in st.session_state.chat:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
