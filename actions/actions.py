from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionClientQuery(Action):

    def name(self) -> Text:
        return "action_client_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")
        intent = tracker.latest_message['intent'].get("name")
        entities = tracker.latest_message['entities'].get("name")

        return []