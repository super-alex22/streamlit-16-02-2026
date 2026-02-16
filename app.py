import streamlit as st
books = ["3096 Days", "Escape From Camp 14", "Stolen Life", "The Girl in the Red Coat", "A Child Called 'It'", "Hope: A Memoir of Survival in Cleveland", "The Silent Patient", "Tomorrow, and Tomorrow, and Tomorrow", "The Haunting of Hill House", "I'll Be Gone in the Dark"]
st.title("Book checker app")
st.write("Enter a book title to check whether it is stored in database")

user_input = st.text_input("Book Title")

if st.button("Check book"):
  if user_input.strip()=="":
    st.warning("Kindly have the book title stated here")
  elif user_input in books:
    st.success("The book exists in database")
  else:
    st.error("The book is NOT in the database")
    new_book = st.text_input("Add book")
    if st.button("Add"):
      st.write(new_book)
