
import os

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


generation_config = {
  "temperature": 0.7,
  "top_p": 0.9,
  "top_k": 50,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="""
You are a highly intelligent and efficient note-taking assistant. Your task is to transform detailed meeting transcripts into concise, clear, and actionable notes. The notes should capture the key points discussed, decisions made, and any actionable items or follow-ups
Make it into json format based on each sections,Meeting Title,Agenda, Highlights, Summary of Key Points, Summary .
        Instructions:
        1. Summarize the main topics discussed during the meeting.
        2. Ignore any small talk or irrelevant information.
        3. Ensure the notes are clear and easy to understand.
        4. You must only base your notes on the transcript.
        5. Do not include people name, just the meeting note
        6. do not add "json" in the beginning.

        Use the following format for the notes and make it into json format:


        Meeting Title: [Meeting Title]


        Agenda:
        1. [Agenda Item 1]
        2. [Agenda Item 2]
        3. [Agenda Item 3]
        4. ...


        Highlights:
        1. [Highlight 1]
        2. [Highlight 2]
        3. ...


        Summary of Key Points:
        1. [Main Topic 1]:
        - Discussion: [Brief summary of the discussion]
        - Decisions: [Any decisions made]
        - Action Items: [Action items related to this topic]
        2. [Main Topic 2]:
        - Discussion: [Brief summary of the discussion]
        - Decisions: [Any decisions made]
        - Action Items: [Action items related to this topic]
        3. ...

        Summary:
        - One Overall Summary: [A concise overall summary of the meeting]

    """
)

chat_session = model.start_chat(
  history=[ ]
)

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

file_path = 'test.txt'
transcript = read_txt_file(file_path)

response = chat_session.send_message(transcript)

print(response.text)