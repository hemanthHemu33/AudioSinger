import os
import time
import pdfplumber
import streamlit as st
import pyttsx3
from io import BytesIO  # Import BytesIO
from pydub import AudioSegment  # For merging audio files
import tempfile  # For temporary files

# In this function, we get the first and last page if provided by the user
def get_text(value, total_pages):
    string = value.strip()
    if "-" in string:
        first_page_number = int(string.split("-")[0])
        last_page_number = int(string.split("-")[1])
    else:
        first_page_number = int(string)
        last_page_number = total_pages if first_page_number == 0 else first_page_number
    return first_page_number, last_page_number

def generate_audio(text_data, page_number, rate, volume):
    """Convert text to speech and return audio file content."""
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Set properties for speech
    engine.setProperty('rate', rate)  # Set speech rate
    engine.setProperty('volume', volume)  # Volume 0-1

    # Create a temporary file for the audio with .wav extension
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
        audio_file = tmp_file.name

    # Save audio to file
    engine.save_to_file(text_data, audio_file)
    engine.runAndWait()
    
    print(f"Audio saved for page {page_number}")
    return audio_file

def main():
    ##### Create directory for Text to Speech software
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'Text_to_speech_software')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)
    
    # Streamlit UI for PDF selection and input
    st.title('PDF to Audiobook Converter')

    # Upload PDF
    uploaded_pdf = st.file_uploader("Choose a PDF file", type="pdf")
    
    # Page number or range input
    page_range = st.text_input("Enter page number or range (e.g., 1-3 or leave empty to read all pages):")

    # User inputs for speech rate and volume
    rate = st.slider("Select speech rate (words per minute):", min_value=50, max_value=300, value=150, step=10)
    volume = st.slider("Select volume level:", min_value=0.0, max_value=1.0, value=1.0, step=0.1)

    audio_files = []  # List to hold the audio file paths

    if st.button('Convert to Audiobook') and uploaded_pdf:
        # Open the PDF from the uploaded file using pdfplumber
        pdf_bytes = uploaded_pdf.read()
        with pdfplumber.open(BytesIO(pdf_bytes)) as pdf:
            total_pages = len(pdf.pages)

            # Determine the range of pages to extract
            if page_range == "":
                first_page_number = 1
                last_page_number = total_pages
            else:
                first_page_number, last_page_number = get_text(page_range, total_pages)

            # Extract and process each page individually
            for i in range(first_page_number - 1, last_page_number):
                page_number = i + 1  # For naming the files based on actual page number

                # Extract text from the PDF page
                page = pdf.pages[i]
                text_data = page.extract_text()

                # Convert extracted text to speech
                if text_data and text_data.strip():  # Check if there's any text extracted
                    st.write(f"Generating audio for page {page_number}")
                    audio_file = generate_audio(text_data, page_number, rate, volume)
                    audio_files.append(audio_file)  # Save the path of the generated audio file
                    st.audio(audio_file)  # Preview the audio
                else:
                    st.write(f"No valid text found on page {page_number}. Skipping audio generation.")

        if audio_files:
            # Merge all audio files into one
            merged_audio = AudioSegment.from_wav(audio_files[0])
            for audio_file in audio_files[1:]:
                next_audio = AudioSegment.from_wav(audio_file)
                merged_audio += next_audio
            
            # Save the merged audio to a file in MP3 format
            merged_audio_file_path = os.path.join(final_directory, "merged_audio.mp3")
            merged_audio.export(merged_audio_file_path, format="mp3")

            # Provide download link for the merged audio
            st.success("All pages processed and audio files generated.")
            st.audio(merged_audio_file_path)  # Optionally preview the merged audio
            st.download_button("Download Merged Audio", open(merged_audio_file_path, 'rb'), file_name="merged_audio.mp3")

if __name__ == '__main__':
    main()
