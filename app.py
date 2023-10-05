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
    st.markdown('<h3 style="text-align: center; color: rgb(137, 79, 218)">Enter your VR Code</h3>', unsafe_allow_html=True)
    code = st.text_input("", max_chars=4)

    if len(code) == 4:
        st.markdown('<h3 style="text-align: center; color: rgb(137, 79, 218)">Choose presentation file</h3>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("", type=['pdf', 'ppt', 'pptx'])

        if uploaded_file is not None:
            #st.markdown('<h3 style="text-align: center; color: rgb(137, 79, 218)">Submit</h3>', unsafe_allow_html=True)

            # Add your own button CSS here
            button_css = """
                <style>
                div.stButton > button:first-child {
                    font-size: 26px;
                    font-weight: bold;
                    font-color: #FFFFFF;
                    padding: 16px 32px;
                    background-color: rgb(137, 79, 218);
                    color: #FFFFFF;
                    border: none;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    border-radius: 12px; /* Add rounded edges */
                    box-shadow: 0 0px 15px rgba(0, 0, 0, 0.2); /* Add shadow for a 3D look */
                    transition: all 0.3s ease-in-out; /* Add smooth transition for hover effects */
                
                }

                div.stButton > button:first-child:hover {
                    cursor: pointer;
                    border: none;
                    background-color: rgb(26, 172, 182);
                    color: #FFFFFF;
                    transform: translateY(-5px) scale(1.02); /* Animate movement upwards and scale */
                    box-shadow: 0 10px 40px rgba(110, 186, 191, 1); /* Enlarge shadow on hover for a 3D effect */
                
                }
                </style>
            """
            st.markdown(button_css, unsafe_allow_html=True)

            if st.button('Upload Presentation'):
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
                    uploaded_file = None
                    st.balloons()
                else:
                    st.error('Error occurred: '+response.text)

if __name__ == '__main__':
    style()
    main()

