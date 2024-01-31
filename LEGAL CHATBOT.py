from flask import Flask, request, render_template
import json
import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

with open('ipc_data.json', 'r') as file:
    ipc_data = json.load(file)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertModel.from_pretrained('bert-base-uncased')

def get_bert_embeddings(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

    with torch.no_grad():
        outputs = bert_model(**inputs)

    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().detach().numpy()

    return embeddings

def get_legal_advice(user_question):
    user_embeddings = get_bert_embeddings(user_question.lower())

    max_similarity = 0.0
    best_match = None

    for chapter_data in ipc_data.get('chapters', []):
        for section_data in chapter_data.get('sections', []):
            section_title = section_data['section_title'].lower()
            section_desc = section_data['section_desc'].lower()

            section_embeddings = get_bert_embeddings(section_title + ' ' + section_desc)
            similarity = cosine_similarity([user_embeddings], [section_embeddings])[0][0]

            if similarity > max_similarity:
                max_similarity = similarity
                best_match = (chapter_data['chapter'], section_data['section'], section_title, section_desc)

    if best_match:
        return f"Under IPC LAW Chapter {best_match[0]}, Section {best_match[1]}, Titled '{best_match[2]}', you might consider filing charges or getting legal advice.\n Description: {best_match[3]}"
    else:
        return "No specific information found for the provided question."

@app.route('/')
def home():
    return render_template('index.html', user_question=None, response=None)

@app.route('/ask', methods=['POST'])
def ask_question():
    user_question = request.form.get('question', '')

    if not user_question:
        return render_template('index.html', response="Please enter a valid question.", user_question=user_question)

    response = get_legal_advice(user_question)

    return render_template('index.html', response=response, user_question=user_question)

if __name__ == '__main__':
    app.run(debug=True)