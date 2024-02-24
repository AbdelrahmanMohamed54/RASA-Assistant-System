## THD International Application Assistant Chatbot "Mezo Application Assistant"

[Project Repository on Github](https://github.com/AbdelrahmanMohamed54/RASA-Assistant-System.git)

## Project Description

The THD International Application Assistant is a speech-enabled application designed to simplify and enhance the application process for prospective students at THD International. It serves as an intelligent front-end interface that guides and assists users throughout the application procedure. This project is developed to streamline access to application information, answer user inquiries, and provide valuable insights about the university's offerings.

For more details and documentation, please refer to the [Wiki](https://github.com/AbdelrahmanMohamed54/RASA-Assistant-System/blob/main/Wiki/README.md).


## Installation


#### Prerequisites

- Requirements: Python 3 and PIP 3
- My Rasa Version   :         3.6.14
- Minimum Compatible Version: 3.5.0
- Rasa SDK Version  :         3.6.2
- Python Version    :         3.6+


#### Installation Steps

Make sure you have the following prerequisites installed:

- [Visual Studio code Installation](https://code.visualstudio.com/download)
- [Python Installation](https://www.python.org/downloads/)
- [Rasa Installation](https://rasa.com/docs/rasa/installation/)
- continue to the [Basic usage section](# Basic Usage) to be guided throughout the project starting.



## Basic Usage

### Starting the Project

Follow these steps to run the chatbot:

#### Step 1: Prerequisites

Make sure you have the following prerequisites installed:

- [Python](https://www.python.org/downloads/)
- [Rasa](https://rasa.com/docs/rasa/installation/)

#### Step 2: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/AbdelrahmanMohamed54/RASA-Assistant-System.git
```

#### Step 3: Open the Project


Follow these steps to open and set up the project in your development environment:

### Step 1: Open Your IDE
- Open your preferred Integrated Development Environment (IDE), such as PyCharm or Visual Studio Code.

### Step 2: Create a New Virtual Environment
- In your IDE, create a new Virtual Environment (venv). This isolates your project dependencies from other projects.
    - For **PyCharm**:
        1. Click on `File > New Project`.
        2. Choose a location for your project.
        3. Select `New environment using` and choose `Virtualenv`.
        4. Specify the location for the new virtual environment in your project folder.
        5. Click `Create`.
    - For **Visual Studio Code**:
        1. Open the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS).
        2. Type and select `Python: Select Interpreter`.
        3. Choose `Enter interpreter path` and select `Find...`.
        4. Click `+ Create a new virtual environment` and follow the prompts.

### Step 3: Clone the Repository
- Clone the repository containing the project files into your desired folder.

### Step 4: Open the Cloned Repository
- Open the cloned repository in your IDE within the created virtual environment.
    - Navigate to the project folder and ensure that your IDE is using the virtual environment you created.

### Step 5: Install Dependencies (Optional)
- If your project requires external libraries or dependencies, install them using a package manager like `pip`.


#### Step 6: Install the Flask Module:

open a terminal and execute the following command:

```bash
pip install Flask
```

#### Step 7: run app.py file

Make sure that the Flask application is running by excuting the app.py file in the actions folder.

#### Step 8: Run Actions Server

To run the actions server, open a terminal and execute the following command:

```bash
rasa run actions
```

#### Step 9: Train the Model

Train the Rasa model by running the following command in the terminal:

```bash
rasa train
```

#### Step 10: Run the Chatbot

Start an interactive chat session with the chatbot using the following command:

```bash
rasa shell
```

#### Step 11: Interact with the Bot

You can now interact with the chatbot and test its functionality.




## Implementation of the Requests

In the [Wiki](https://github.com/AbdelrahmanMohamed54/RASA-Assistant-System/blob/main/Wiki/README.md) I implimented the following requests:

  - Check for right fit
  - 1 system persona and 3 user persona
  - use cases
  - Technical prerequisites
  - For every persona at least 2 example dialogs
  - A dialog flow Diagram


In the "RASA-Assistant-System" Rasa project, user requests are handled through a combination of custom actions, intent recognition, story flows, and domain configurations. Below is a detailed breakdown of how each component contributes to the processing and fulfillment of user requests.

### Actions (`actions/` Folder)

#### `actions.py`

- **Description**: Contains custom action classes that define the logic executed after certain user inputs.
- **Functionality**: Each class extends the `Action` class from Rasa SDK and implements the `run` method to perform specific actions, such as fetching data from APIs, responding with dynamic information, or setting slots.
- **Key Implementations**:
  - `ActionListProgramsUnderFaculty`: Lists available programs under a selected faculty.
  - `ActionProvideProgramDetails`: Retrieves and sends specific details (like language of teaching or application periods) for a chosen program.

#### `app.py`

- **Description**: A Flask application that serves as an API endpoint for fetching program details.
- **Functionality**: Provides endpoints to access data stored in `new.json`, allowing actions in `actions.py` to retrieve necessary information.
- **Endpoints**:
  - `/get_program_info`: Returns program details from `new.json`.

#### `new.json`

- **Description**: JSON file containing detailed information about various programs.
- **Usage**: Acts as a database for the Flask app defined in `app.py` to provide program-specific information.

### Data and Training (`data/` Folder)

#### `nlu.yml`

- **Description**: Contains training data for the NLU model.
- **Functionality**: Helps the model understand and extract user intents and entities from user inputs.
- **Key Components**: Defined intents, entities, and examples for training.

#### `stories.yml`

- **Description**: Defines storylines that represent the flow of conversations.
- **Functionality**: Guides the dialogue management model to choose appropriate actions based on the conversation history.

#### `rules.yml`

- **Description**: Specifies rules for predictable actions.
- **Functionality**: Ensures specific actions are taken following particular user inputs or conversation states.

### Domain Configuration (`domain.yml`)

- **Description**: The central configuration file defining the conversational elements.
- **Functionality**:
  - Declares intents, entities, slots, actions, and responses.
  - Maps actions defined in `actions.py` to the conversational elements.

### Overall Workflow

- **User Input Processing**: User messages are processed by Rasa NLU to extract intents and entities (`nlu.yml`).
- **Dialogue Management**: Based on the extracted information and conversation history, Rasa Core decides the next action (guided by `stories.yml` and `rules.yml`).
- **Action Execution**: Custom actions (`actions.py`) interact with the Flask API (`app.py`) to fetch and provide detailed program information.
- **Response Generation**: Responses are formulated either by predefined templates in `domain.yml` or dynamically by custom actions, then presented to the user.

---

### Important notes about the project's domain (Project Scope Refinement)

- Initially, the project was supposed to include "Study programs" and "Study requirements" as depicted in the Dialog Flow Diagram and sample dialogs. However, after discussing the size of our domain with proffesor Garmann, i was advised to reduce the context of the chatbot implimentation and streamline my chatbot's focus exclusively to "Study Programs" to ensure a more targeted and effective implementation.



## Project Status

Development of this project is complete and stable. I am no longer actively working on new features or updates. However, I welcome contributions and i am open to collaboration with new maintainers to ensure its continued maintenance and support.
