# PDF to Audiobook Converter

## Project Overview

The **PDF to Audiobook Converter** is a Python-based application with a user-friendly **Streamlit** interface that converts PDF documents into audiobooks. The tool extracts text from PDFs, converts the text to speech using `pyttsx3`, and merges the audio files into a single MP3 for easy playback. The user can select specific page ranges, adjust the speech rate and volume, and download the final merged audiobook.

## Features

- **PDF Upload**: Upload any PDF document.
- **Page Selection**: Choose specific pages or ranges to convert to audio.
- **Customizable Speech Rate and Volume**: Adjust speech rate (WPM) and volume for a personalized listening experience.
- **Audio Preview**: Listen to the generated audio files for each page before downloading.
- **MP3 Merging**: All audio files are merged into a single MP3 file for easy playback.
- **Download Option**: Users can download the merged audiobook.

## Technologies Used

- **Python**: Main programming language.
- **Streamlit**: Web interface for user interaction.
- **pdfplumber**: Extracts text from PDF documents.
- **pyttsx3**: Text-to-speech conversion.
- **pydub**: Merges audio files and converts file formats.
- **tempfile**: Handles temporary file storage for audio.
- **Pillow**: For image processing.
- **PyMuPDF**: Converts PDF pages to images.
- **pytesseract**: Optical Character Recognition (OCR) for converting images to text.
- **pygame**: Plays the generated audio.
- **gTTS**: Google Text-to-Speech for an alternative TTS engine.
- **PySimpleGUI**: Provides an easy-to-build graphical user interface (GUI).

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd pdf-to-audiobook
   ```

2. **Install Python Dependencies**:

   Install the required Python libraries listed in `requirements.txt`:

   ```bash
   pip install streamlit pdfplumber pyttsx3 pydub pillow pymupdf pytesseract pygame gtts pysimplegui
   ```

3. **Install `ffmpeg` for MP3 Merging**:

   - **On Ubuntu**:
     ```bash
     sudo apt-get install ffmpeg
     ```
   - **On Windows**:
     Download and install `ffmpeg` from [FFmpeg official site](https://ffmpeg.org/download.html) and add it to your system's PATH.

4. **Install Tesseract OCR**:

   - **On Ubuntu**:
     ```bash
     sudo apt install tesseract-ocr
     ```
   - **On Windows**:
     Download and install Tesseract OCR from [Tesseract official site](https://github.com/tesseract-ocr/tesseract).

5. **Run the Application**:

   Execute the following command to launch the Streamlit interface:

   ```bash
   streamlit run PDF_TO_AUDIO_STREAMLIT.py
   ```

6. **Access the Application**:

   After running the command, open your browser and go to `http://localhost:8501` to access the interface.

## Usage Instructions

1. **Upload a PDF**: Click "Choose a PDF file" to upload your document.
2. **Specify Page Range**: Optionally enter a specific page or range (e.g., `1-5`). Leave empty to process all pages.
3. **Adjust Speech Settings**: Use the sliders to set your desired speech rate (words per minute) and volume level.
4. **Convert**: Click "Convert to Audiobook" to generate the audio.
5. **Preview**: Listen to individual page audios as they are generated.
6. **Download**: Once all pages are processed, download the merged audiobook as an MP3.

## File Structure

```bash
.
├── PDF_TO_AUDIO_STREAMLIT.py                      # Main application logic.
├── requirements.txt             # Python dependencies.
├── Text_to_speech_software/      # Directory for generated audio files.
└── README.md                    # Project documentation.
```

## Known Issues

- Text extraction may not work well for PDFs with complex formatting like tables, images, or multi-column layouts.
- The local `pyttsx3` TTS engine can be slower compared to cloud-based solutions.
- Merging large audio files might take time depending on system performance.

## Future Enhancements

- **Multiple Voices and Languages**: Support for different voices and languages in the text-to-speech engine.
- **Improved PDF Parsing**: Better handling of complex formatting like images, columns, and non-text elements.
- **Cloud Integration**: Enable cloud-based storage and audio processing.
- **OCR for Scanned PDFs**: Add support for scanned PDFs with better OCR integration.
- **Pause and Resume**: Allow pausing and resuming audiobook generation.

## License

This project is licensed under the MIT License.
