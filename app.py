import requests
import streamlit as st

st.set_page_config(page_title="Simli Upload", page_icon="")

API_BASE = st.secrets["API_BASE"]

def style():
    st.markdown(
        """
        <style>

        [data-testid="stHeader"] {
            background: rgb(177, 152, 246);
            color: black;
        }

        [data-testid="stAppViewContainer"] {
            background: rgb(177, 152, 246);
            color: black;
        }

        [data-testid="stAppViewContainer"] {
            background: linear-gradient(220deg, #eefcff,#ffffff, #faf4ff);
            color: black;
        }
        
        @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

        * {
            font-family: 'Poppins', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():

    #st.title('SIMLI')
    st.markdown(
        f'<div style="display: flex; justify-content: center;"><img src="https://www.simli.com/hs-fs/hubfs/Simli_Logo_Black_RGB-2.png?width=594&height=258&name=Simli_Logo_Black_RGB-2.png" /></div>', 
        unsafe_allow_html=True,
    )

    # 4 character code input
    st.markdown('<h3 style="text-align: center; color: rgb(137, 79, 218)">1. Enter your VR Code</h3>', unsafe_allow_html=True)
    code = st.text_input("", max_chars=4)

    if len(code) == 4:
        st.markdown('<h3 style="text-align: center; color: rgb(137, 79, 218)">2. Upload PDF file</h3>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("", type="pdf")

        if uploaded_file is not None:

            # Create payload
            payload = {'code': code.upper()}

            with st.spinner('Uploading...'):
                # Post the pdf file
                response = requests.post(API_BASE+"uploadFile",
                                        params=payload,
                                        files={"file": uploaded_file})
                print(response.url)
            if response.status_code == 200:
                st.success('Successfully uploaded:   '+uploaded_file.name)
                st.balloons()
            else:
                st.error('Error occurred: '+response.text)

if __name__ == '__main__':
    style()
    main()

