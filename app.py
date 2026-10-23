import os
import tempfile
import streamlit as st
import whisper

# App Title & Configuration
st.set_page_config(page_title="Audio/Video Transcriber", page_icon="🎙️", layout="centered")

st.title("🎙️ AI Audio & Video Transcriber")
st.write("Upload an MP3 or MP4 file, and Python will transcribe it into text locally using OpenAI Whisper.")

# Load the Whisper model (cached so it only loads once)
@st.cache_resource
def load_model():
    # 'base' model is a good balance of speed and accuracy. 
    # You can change to 'tiny', 'small', 'medium', or 'large' depending on your PC's power.
    return whisper.load_model("base")

with st.spinner("Loading AI Model... Please wait."):
    model = load_model()

# File Uploader widget
uploaded_file = st.file_uploader("Upload an MP3 or MP4 file", type=["mp3", "mp4", "wav", "m4a", "mpeg"])

if uploaded_file is not None:
    # Display file details
    st.audio(uploaded_file, format=f"audio/{uploaded_file.name.split('.')[-1]}")
    
    if st.button("Transcribe Audio"):
        with st.spinner("Transcribing... This may take a moment depending on file length."):
            
            # Save uploaded file temporarily to disk so Whisper can read it
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name

            try:
                # Run Whisper transcription
                result = model.transcribe(tmp_path)
                transcription_text = result["text"]

                st.success("Transcription complete!")
                
                # Display text output area
                st.subheader("Transcription Result")
                st.text_area("Output Text", transcription_text, height=250)

                # Download button for the text file
                st.download_button(
                    label="Download Transcription as TXT",
                    data=transcription_text,
                    file_name="transcription.srt" if False else "transcription.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"An error occurred during transcription: {e}")
            
            finally:
                # Clean up the temporary file
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)