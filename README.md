## ChatGPT Legal Advisor

This is a simple Flask web application that utilizes ChatGPT, a language model, to provide legal advice based on questions related to the Indian Penal Code (IPC). The application uses BERT (Bidirectional Encoder Representations from Transformers) for text embeddings and cosine similarity for matching user questions with IPC sections.

## Setup

1. Install the required dependencies:
   -pip install flask transformers torch scikit-learn

2. Download the IPC data and BERT model:
   - Download IPC data in JSON format and save it as 'ipc_data.json'.
   - The BERT model used here is 'bert-base-uncased' from Hugging Face Transformers.

3. Run the Flask application:
   -python your_file_name.py

4. Open your browser and go to [http://localhost:5000/](http://localhost:5000/) to access the application.

## Application Structure

- `ipc_data.json`: JSON file containing IPC law data, including chapters and sections.

- `bert-base-uncased`: Pretrained BERT model for text embeddings.

- `your_file_name.py`: Python script containing the Flask application.

- `templates/index.html`: HTML template for the web interface.

## Functionality

1. Home Page (`/`):
   - Renders the index page with a form to input legal questions.

2. Ask Endpoint (`/ask`, POST):
   - Takes user input from the form, processes the question using BERT embeddings, and finds the most relevant IPC section.
   - Displays the relevant information or a message if no specific information is found.

## Usage

1. Enter a legal question on the home page.

2. Click the "Ask" button.

3. Receive legal advice based on IPC law.

## Important Note

This application is a basic implementation and may not cover all legal scenarios. It is recommended to consult with a legal professional for accurate and detailed legal advice.
