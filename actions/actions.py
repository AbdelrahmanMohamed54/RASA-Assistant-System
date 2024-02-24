
from rasa_sdk import Action, Tracker
import requests
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List


class ActionGetProgramInfo(Action):
    def name(self) -> Text:
        return "action_get_program_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Make a request to your Flask API
        response = requests.get('http://127.0.0.1:5000/get_program_info')
        data = response.json()

        # Process the data and send a response
        # For example, you can extract information and send a custom message
        dispatcher.utter_message(text="Received program info from the API.")

        return []


class ActionGetLanguageSkills(Action):
    def name(self) -> Text:
        return "action_get_language_skills"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Make a request to your Flask API
        response = requests.get('http://127.0.0.1:5000/get_program_info')
        data = response.json()

        # Extract language skills information
        language_skills = data.get("Study_Programs", {}).get("International_Exchange_Programs", {}).get("Language_skills", [])

        # Send a response
        if language_skills:
            # Join the list of language skills into a single string
            response_text = "\n".join(language_skills)
            dispatcher.utter_message(text=response_text)
        else:
            dispatcher.utter_message(text="Sorry, I couldn't retrieve language skills information.")

        return []


class ActionGetHowToApply(Action):
    def name(self) -> Text:
        return "action_get_How_To_Apply"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Make a request to your Flask API
        response = requests.get('http://127.0.0.1:5000/get_program_info')
        data = response.json()

        # Extract language skills information
        language_skills = data.get("Study_Programs", {}).get("International_Exchange_Programs", {}).get("How_To_Apply", [])

        # Send a response
        if language_skills:
            # Join the list of language skills into a single string
            response_text = "\n".join(language_skills)
            dispatcher.utter_message(text=response_text)
        else:
            dispatcher.utter_message(text="Sorry, I couldn't retrieve language skills information.")

        return []


class ActionListBachelorFaculties(Action):
    def name(self) -> Text:
        return "action_list_bachelor_faculties"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get('http://127.0.0.1:5000/get_program_info')  # URL to your Flask API endpoint
        if response.status_code == 200:
            data = response.json()
            bachelor_programs = data.get("Study_Programs", {}).get("Bachelor_Programs", {})
            faculties = bachelor_programs.keys()
            message = "In which of the following Bachelor Faculties are you interested in? :\n" + "\n".join(faculties)
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Sorry, I couldn't retrieve the faculties list")
        return []


class ActionListProgramsUnderFaculty(Action):
    def name(self) -> Text:
        return "action_list_programs_under_bachelor_faculty"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        faculty_name = tracker.get_slot('bachelor_faculty')  # Retrieve the faculty name from the slot
        response = requests.get('http://127.0.0.1:5000/get_program_info')  # URL to your Flask API endpoint

        if response.status_code == 200:
            data = response.json()
            bachelor_programs = data.get("Study_Programs", {}).get("Bachelor_Programs", {})
            programs = bachelor_programs.get(faculty_name, {})

            if programs:
                program_list = "\n".join(programs.keys())
                additional_message = "Please choose the program you are most interested in, and what information do you want to know, 'language of teaching' or 'application period'?"
                message = f"The available programs in {faculty_name} are:\n{program_list}\n\n{additional_message}"
            else:
                message = f"No programs found under {faculty_name}, please provide a faculty name only from the list above."

            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Sorry, I couldn't retrieve the program information.")

        return []


class ActionProvideProgramDetails(Action):
    def name(self) -> Text:
        return "action_provide_program_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        program_name = tracker.get_slot('bachelor_program_name')
        info_type = tracker.get_slot('bachelor_info')

        if not program_name or not info_type:
            dispatcher.utter_message(text="Please specify the program name and the information you want.")
            return []

        # Modify the endpoint as necessary to point to your Flask API
        api_url = "http://127.0.0.1:5000/get_program_info"
        response = requests.get(api_url)

        if response.status_code != 200:
            dispatcher.utter_message(text="I am unable to fetch program details at the moment.")
            return []

        data = response.json()
        bachelor_programs = data.get("Study_Programs", {}).get("Bachelor_Programs", {})

        # Normalize info_type
        json_info_type = info_type.replace(" ", "_").lower()
        if json_info_type in ["language_of_teaching", "teaching_language"]:
            json_info_type = "Language_of_teaching"
        elif json_info_type == "application_period":
            json_info_type = "Application_period"

        for faculty, programs in bachelor_programs.items():
            if program_name in programs:
                program_info = programs[program_name].get(json_info_type, "Information not available")
                dispatcher.utter_message(
                    text=f"The {info_type} of the {program_name} bachelor program is {program_info}.\nWould you like to inquire about another bachelor program or completely change the study program type?")
                return []

        dispatcher.utter_message(text="Sorry, I couldn't find the information you requested. Please make sure you mention the requested information and program name correctly")
        return []


class ActionListMasterFaculties(Action):
    def name(self) -> Text:
        return "action_list_master_faculties"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response = requests.get('http://127.0.0.1:5000/get_program_info')  # URL to your Flask API endpoint
        if response.status_code == 200:
            data = response.json()
            master_programs = data.get("Study_Programs", {}).get("Master_Programs", {})
            faculties = master_programs.keys()
            message = "In which of the following Masters Faculties are you interested in? :\n" + "\n".join(faculties)
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Sorry, I couldn't retrieve the faculty information.")
        return []


class ActionListMasterProgramsUnderFaculty(Action):
    def name(self) -> Text:
        return "action_list_programs_under_master_faculty"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        faculty_name = tracker.get_slot('master_faculty')  # Retrieve the faculty name from the slot
        response = requests.get('http://127.0.0.1:5000/get_program_info')  # URL to your Flask API endpoint

        if response.status_code == 200:
            data = response.json()
            master_programs = data.get("Study_Programs", {}).get("Master_Programs", {})
            programs = master_programs.get(faculty_name, {})

            if programs:
                program_list = "\n".join(programs.keys())
                additional_message = "Please choose the program you are most interested in, and what information do you want to know, 'language of teaching' or 'application period'?"
                message = f"The available programs in {faculty_name} are:\n{program_list}\n\n{additional_message}"
            else:
                message = f"No programs found under {faculty_name}, please make sure the chosen faculty is in the list above."

            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Sorry, I couldn't retrieve the program information.")

        return []


class ActionProvideMasterProgramDetails(Action):
    def name(self) -> Text:
        return "action_provide_master_program_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        program_name = tracker.get_slot('master_program_name')
        info_type = tracker.get_slot('master_info')

        if not program_name or not info_type:
            dispatcher.utter_message(text="Please specify the program name and the information you want.")
            return []

        # Modify the endpoint as necessary to point to your Flask API
        api_url = "http://127.0.0.1:5000/get_program_info"
        response = requests.get(api_url)

        if response.status_code != 200:
            dispatcher.utter_message(text="Sorry, I couldn't find the information you requested. Please make sure you mention the requested information and program name correctly")
            return []

        data = response.json()
        master_programs = data.get("Study_Programs", {}).get("Master_Programs", {})

        # Normalize info_type
        json_info_type = info_type.replace(" ", "_").lower()
        if json_info_type in ["language_of_teaching", "teaching_language"]:
            json_info_type = "Language_of_teaching"
        elif json_info_type == "application_period":
            json_info_type = "Application_period"

        for faculty, programs in master_programs.items():
            if program_name in programs:
                program_info = programs[program_name].get(json_info_type, "Information not available")
                dispatcher.utter_message(
                    text=f"The {info_type} of the {program_name} master program is {program_info}.\nWould you like to inquire about another bachelor program or completely change the study program type?")
                return []

        dispatcher.utter_message(text="Sorry, I couldn't find the information you requested, Please make sure you mention the requested information and program name correctly.")
        return []
