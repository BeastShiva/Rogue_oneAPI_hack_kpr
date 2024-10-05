import requests
import time
from langchain_community.llms import Ollama
from fpdf import FPDF  # Library to create PDFs

def transcribe_audio(file_path):
    # Your AssemblyAI API key
    API_KEY = '1e2a92ca6b7c4517893eefa4d669f577'  # Replace with your AssemblyAI API key
    headers = {'authorization': API_KEY}

    # Upload the audio file
    with open(file_path, 'rb') as audio_file:
        response = requests.post(
            'https://api.assemblyai.com/v2/upload',
            headers=headers,
            data=audio_file
        )
    
    audio_url = response.json()['upload_url']
    
    # Request transcription
    transcript_request = {
        'audio_url': audio_url
    }
    transcript_response = requests.post(
        'https://api.assemblyai.com/v2/transcript',
        json=transcript_request,
        headers=headers
    )
    
    transcript_id = transcript_response.json()['id']
    
    # Poll for the transcription result
    while True:
        polling_response = requests.get(
            f'https://api.assemblyai.com/v2/transcript/{transcript_id}',
            headers=headers
        )
        result = polling_response.json()
        
        if result['status'] == 'completed':
            print("Transcript:", result['text'])  # Print transcript to console
            return result['text']  # Return the transcribed text
        elif result['status'] == 'failed':
            raise Exception("Transcription failed.")
        
        # Wait before polling again
        time.sleep(5)

def summarize_transcription(transcription):
    # Initialize the Ollama LLM (or another LLM of your choice)
    llm = Ollama()
    
    # Create the prompt for summarization
    llm_prompt = f"Please summarize the following text:\n\n{transcription}"
    
    # Invoke the LLM with the transcription text
    summary = llm.invoke(llm_prompt)
    
    return summary

def save_to_pdf(summary, title):
    # Create a PDF document
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, title, ln=True, align='C')
    
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)
    
    # Save the PDF to a file
    pdf.output("summary.pdf")
    print("Summary saved to 'summary.pdf'")

if __name__ == "__main__":
    audio_file_path = "Record (online-voice-recorder.com).mp3"  # Change this to your audio file path
    title = "Transcription Summary"

    # Step 1: Transcribe the audio
    try:
        transcription = transcribe_audio(audio_file_path)

        # Step 2: Summarize the transcription
        summary = summarize_transcription(transcription)
        print("Summarization completed.")

        # Step 3: Save the summary to a PDF
        save_to_pdf(summary, title)
        
    except Exception as e:
        print(str(e))