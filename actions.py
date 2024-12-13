# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import PyPDF2
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionAnswerFromPDF(Action):
    def name(self) -> str:
        return "action_answer_from_pdf"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Path to the PDF
        pdf_path = "example.pdf"  # Replace with your file path
        
        # Extract user query from conversation
        user_query = tracker.latest_message.get('text')

        # Extract text from the PDF
        with pdfplumber.open(pdf_path) as pdf:
            pdf_text = ""
            for page in pdf.pages:
                pdf_text += page.extract_text()
        
        # Check for specific terms related to electric vehicles
        if "electric vehicle" in user_query.lower() or "ev" in user_query.lower():
            if "electric vehicle" in pdf_text.lower() or "ev" in pdf_text.lower():
                response = "Yes, the document mentions electric vehicles. Here's some information: [Extracted Text]."
            else:
                response = "Sorry, there is no mention of electric vehicles in the document."
        else:
            response = "Sorry, I couldn't find anything related to your query in the PDF."
        
        dispatcher.utter_message(text=response)
        return []

