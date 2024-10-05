
# AI Meeting Partner

A comprehensive C application that simplifies food ordering, optimizes delivery, and rewards customer loyalty with points.
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Modules and Algorithms](#modules-and-algorithms)
- [Contribution Guidelines](#contribution-guidelines)
- [Authors and Acknowledgments](#authors-and-acknowledgments)
- [Contact Information](#contact-information)

## Installation
### Prerequisites
- Streamlit
- Firebase Admin
- Ollama
- Node js
- Intel oneAPI Toolkit GPU

### Step-by-Step Installation
1. Clone the repository: `https://github.com/ShreyasK-05/Rogue_oneAPI_hack_kpr`
2. Navigate to the project directory: `cd Rogue_oneAPI_hack_kpr`
3. Compile the project.
4. Run the executable: `./Rogue_oneAPI_hack_kpr`

## Usage
### Running the Application
- Execute the binary: `./food_delivery_app`
- Follow the on-screen instructions to place an order.

## Features
- Chat with multiple PDFs
- Meeting transcriber and minutes of the meeting generation
- Active meeting participant AI
- RAG for trend analysis

## Modules and Algorithms
### 1. User Module
- **Sign-Up/Login:**
  - Handles user registration and authentication for the meeting platform.
  - Stores user credentials securely in the backend database.
  - Manages user profiles and personalized settings for the chatbot.

### 2. Meeting Management Module
- **Create and Schedule Meetings:**
  - Allows users to schedule, create, and manage meeting invitations.
  - Sends automated reminders and notifications to participants.

### 3. PDF Upload and Storage Module
- **Upload and Store Minutes:**
  - Enables users to upload PDF documents, such as minutes of previous meetings.
  - Stores uploaded PDFs in the backend for future reference, using Firebase or similar services.

### 4. Chatbot Integration Module
- **AI-Powered Question Answering:**
  - Integrates an AI-powered chatbot (using Llama 2 or Hugging Face models) to answer user queries based on the uploaded meeting minutes.
  - Allows users to ask questions related to the meeting’s content and get contextual responses.

### 5. Transcription and Speech Recognition Module
- **Live Transcription:**
  - Uses speech recognition (e.g., Whisper AI) to transcribe live conversations in real time.
  - Generates accurate transcriptions of the meeting for later review and note-taking.

### 6. Voice Differentiation and Speaker Labeling Module
- **Identify Speakers:**
  - Recognizes different speakers' voices during the meeting and labels the transcription accordingly.
  - Associates each part of the transcript with the correct speaker for clarity.

### 7. Meeting Summary Generation Module
- **Generate Minutes of Meeting (MoM):**
  - Automatically summarizes key points from the meeting transcript.
  - Generates concise minutes of the meeting based on important discussions and decisions made during the session.

### 8. PDF Generation Module
- **Create and Store PDFs:**
  - Converts transcribed and summarized meeting content into PDF format.
  - Stores the PDF in the user's account, allowing for easy access and sharing.

### 9. Search and Retrieval Module
- **Search for Meeting Content:**
  - Enables users to search through uploaded PDFs or meeting transcripts based on keywords or topics.
  - Provides quick access to specific information discussed in previous meetings.

### 10. Feedback Collection Module
- **User Feedback on Meeting Quality:**
  - Allows users to provide feedback on the transcription accuracy and chatbot response quality.
  - Collects ratings and feedback to improve the meeting and chatbot experience.

### 11. Custom Report Generation Module
- **Generate Custom Reports:**
  - Provides the option for users to create custom reports based on the meeting's outcomes.
  - Users can select specific topics or sections of the transcript for inclusion in the final report.

### 12. Real-Time Interaction Module
- **Live Chat and Questions:**
  - Allows participants to interact with the chatbot during a live meeting to clarify points or summarize discussions on the fly.
  - Ensures active engagement and helps answer queries in real-time.

### 13. API Integration Module
- **Integrate with Third-Party Tools:**
  - Integrates with popular meeting platforms (e.g., Google Meet) and project management tools for seamless meeting coordination and data synchronization.

### 14. Role-Based Access Control Module
- **Manage Access Levels:**
  - Assigns different roles to users such as host, participant, or admin to control access to features like report generation, transcription editing, and chatbot use.

## Contribution Guidelines
- Fork the repository
- Create a new branch
- Submit a pull request

## Authors
- Developed by Shreyas K, Shiva Ganesh, Mahadev Ramesh Ramya

## Contact Information
For questions or support, contact shreyas2310140@ssn.edu.in







