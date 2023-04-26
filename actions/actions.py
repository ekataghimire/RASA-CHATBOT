# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

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
class ActionUtterSympathy(Action):
    def name(self) -> Text:
        return "action_utter_sympathy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("I'm sorry to hear that. It must be really difficult to deal with depression symptoms. Please know that I'm here to support you in any way I can.")
        return []

class ActionUtterRecommendHelp(Action):
    def name(self) -> Text:
        return "action_utter_recommend_help"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("It's important to prioritize your mental health. I would recommend seeking professional help from a mental health professional. You can also check out online resources like the National Alliance on Mental Illness (NAMI) or the Substance Abuse and Mental Health Services Administration (SAMHSA).")
        return []
    
class ActionUtterAcknowledgeSuicidal(Action):
    def name(self) -> Text:
        return "action_utter_acknowledge_suicidal"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("There is always a way out. Sucicide is not an option. Suicide hotline: 9898786786876876")
        return []
    
class ActionUtterConnect_Crisis_Hotline(Action):
    def name(self) -> Text:
        return "action_utter_connect_crisis_hotline"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Start living life for yourself not others. YOU are the most important person to you. Self love is the biggest love. Suicide Prevention Hotline: 982373736372")
        return []