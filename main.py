import os
import pdfplumber
from google.cloud import storage
from langchain_community.llms import Ollama

# Set the path to your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Shiva Ganesh\Downloads\authentication-5e874-firebase-adminsdk-1pojo-17d169162f.json"

def download_pdf(bucket_name, blob_name, destination_file_name):
    """Downloads a blob (PDF file) from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Downloaded {blob_name} to {destination_file_name}")

def list_accessible_files(bucket_name, access_level):
    """Lists all the accessible PDF files based on user access level."""
    try:
        # Initialize a storage client
        storage_client = storage.Client()

        # Get the bucket
        bucket = storage_client.bucket(bucket_name)

        # List all blobs in the bucket
        blobs = bucket.list_blobs()

        print(f"Accessible files for user with access level {access_level}:")
        accessible_files = []
        for blob in blobs:
            # Extract the digit from the file name before ".pdf"
            if blob.name.endswith(".pdf"):
                file_access_level = blob.name.split('/')[-1][:-4][-1]  # Extract the digit from the file name
                if file_access_level.isdigit() and int(file_access_level) <= access_level:
                    print(blob.name)  # Display file name
                    accessible_files.append(blob.name)

        return accessible_files

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def extract_text_from_pdf(pdf_path):
    """Extracts text from the provided PDF file using pdfplumber."""
    s = ""
    with pdfplumber.open(pdf_path) as f:
        for page in f.pages:
            text = page.extract_text()
            if text:  # Check if text was extracted
                s += text + "\n"  # Add a newline for better separation
    return s

if __name__ == "__main__":
    bucket_name = "authentication-5e874.appspot.com"  # Your Firebase Storage bucket name
    
    # Get user access level as input
    while True:
        try:
            access_level = int(input("Enter your access level (1-5): "))
            if 1 <= access_level <= 5:
                break
            else:
                print("Please enter a valid access level between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    # Get list of accessible files
    accessible_files = list_accessible_files(bucket_name, access_level)

    # Initialize the Ollama LLM (or another LLM of your choice)
    llm = Ollama()

    # Parse all accessible PDFs and upload their content to the LLM
    parsed_pdf_content = ""
    for pdf_blob_name in accessible_files:
        # Download each PDF to a local file
        local_pdf_path = pdf_blob_name.split("/")[-1]  # Extract just the filename for local storage
        download_pdf(bucket_name, pdf_blob_name, local_pdf_path)

        # Extract text from the downloaded PDF
        extracted_text = extract_text_from_pdf(local_pdf_path)
        parsed_pdf_content += f"Content from {local_pdf_path}:\n{extracted_text}\n\n"

    # Once all PDFs are parsed, allow the user to ask questions
    while True:
        user_question = input("What would you like to ask about the PDF contents? (type 'exit' to quit) ")

        if user_question.lower() == 'exit':  # Check if the user wants to exit the loop
            print("Exiting the program.")
            break

        # Combine the parsed content and the user's question as context for the LLM
        llm_prompt = f"The following is the content of the parsed PDFs:\n\n{parsed_pdf_content}\n\nQuestion: {user_question}"

        # Invoke the LLM with the parsed content and the user's question
        result = llm.invoke(llm_prompt)

        # Print the result from the LLM
        print("LLM's Response:")
        print(result)
