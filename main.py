import streamlit as st

st.set_page_config(layout="wide")

col1,col2=st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Łukasz Nawrocki")
    content=""" Jakis kontent o mnie . aksd akdm ald lkams lkamskld maldm l dals
    adlkasndkasndakndkasndaksndkajs a asd asd a as asd asd asd as a ad asdajdnadkandka a asd a
     adkaknddja nkjandkjan jknasdjnopgkregepk3o,coqurgequtwz83ipwoktecg;e f
      wklnf mlks;fk nsd ksdnfkms ;;fmkmflksmflks 
    """
    st.info(content)
content2 ="""
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)