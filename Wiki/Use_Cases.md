# Use Cases UML Diagram 

**The Use Cases Diagram:**
![Alt Text](https://github.com/AbdelrahmanMohamed54/RASA-Assistant-System/blob/main/Wiki/use%20cases.png)

# User Persona 1 - Ziad (Applying for a Master's program at THD International)

## Use Case 1: Requesting Application Requirements
- **Persona:** Ziad
- **Context:** Ziad is in the early stages of applying for a Master's program at THD International and needs to know the application requirements.
- **Steps:**
   1. Ziad starts the conversation with the application assistant by asking for possible actions.
   2. The system provides options for possible actions.
   3. Ziad selects "A Full Time Study Program"
   3. The system then asks about the type of applicant
   3. Ziad chooses "An International Applicant"
   4. The system presents a list of general application requirements.
   
- **Errors or Problems:**
   - Ziad may not understand some of the technical terms used in the application requirements.
   - The system may not provide clear or comprehensive information, leading to Ziad's confusion.

## Use Case 2: Available Master programs
- **Persona:** Ziad
- **Context:** Ziad is interested in knowing the study options for his Master's program application.
- **Steps:**
   1. Ziad initiates the conversation with the application assistant.
   2. The system offers available actions.
   3. Ziad selects "Ask about Master programs."
   4. The system asks about the learning field of interest of Ziad and lists the available fields.
   5. Ziad replies with the field of interest .
   6. The system provides all master programs related to that field.
- **Errors or Problems:**
   - Ziad might not be eligible for any available program, which can lead to disappointment.
   - Ziad might not know his field of interest or not know some scientific terms in the fields names.
   - Wrong program name entered by the user, causing inaccuracies or confusion.

## Use Case 3: Program Application periods
- **Persona:** Ziad
- **Context:** Ziad wants to learn more about the Master's programs application periods.
- **Steps:**
   1. Ziad begins a conversation with the application assistant.
   2. The system suggests possible actions.
   3. Ziad chooses "Available bachelor programs"
   4. The system asks for the desired faculty.
   5. Ziad provides the faculty name
   6. The system then gives the programs in the chosen faculty.
   7. the user asks about the deadline of the required program.
- **Errors or Problems:**
   - The system may not have up to date application dates.
   - Ziad may have follow-up questions about deadline extension

# User Persona 2 - David (Applying for an International Exchange program at THD)

## Use Case 1: Exchange Programs application procedure
- **Persona:** David
- **Context:** David is a working Student interested in applying for an International Exchange program at THD and needs to know about available Exchange Programs and the application procedure.
- **Steps:**
   1. David initiates a conversation with the application assistant.
   2. The system offers possible actions.
   3. David selects "Ask about Exchange Programs."
   4. The user needs to choose between "Language Skills" and "How To Apply"
   5. David chooses the "How to apply"
   6. The system lists the application procedure
- **Errors or Problems:**
   - The system will give general steps which may mislead the user.
   - David may not be familiar with the websites required for application procedure.

## Use Case 2: Language requirements 
- **Persona:** David
- **Context:** David is concerned about the German language requirements for Exchange programs.
- **Steps:**
   1. David starts a conversation with the application assistant.
   2. The system suggests potential actions.
   3. David chooses "Ask about Exchange Programs."
   4. The user needs to choose between "Language Skills" and "How To Apply"
   5. David chooses the "Language Skills"
   6. The system lists the admission requirements including the German language requirements
- **Errors or Problems:**
   - The system may not provide detailed German level or accepted certifications.

## Use Case 3: Program Teaching Language
- **Persona:** David
- **Context:** David wants to know more about the teaching language of Master's programs.
- **Steps:**
   1. David begins a conversation with the application assistant.
   2. The system suggests possible actions.
   3. Ziad chooses "Available Master programs"
   4. The system asks for the desired faculty.
   5. David provides the faculty name
   6. The system then gives the programs in the chosen faculty.
   7. David asks about the Teaching Language of the required program.
- **Errors or Problems:**
   - The system may not have up to date, new courses may have more than one language.
   - Ziad may have follow-up questions about Language proficiency.


# User Persona 3 - Ahmed (Applying for an undergraduate program at THD International)

## Use Case 1: General Admission Requirements
- **Persona:** Ahmed
- **Context:** Ahmed is a high school graduate exploring undergraduate program options.
- **Steps:**
   1. Ahmed begins a conversation with the application assistant.
   2. The system suggests possible actions.
   3. Ahmed chooses "Explore undergraduate/Bachelor programs."
   4. The system lists available undergraduate programs.
- **Errors or Problems:**
   - Ahmed may not understand some of the terminology used in the program descriptions.
   - Ahmed might inquire about a program that that is not available for the next semester.

## Use Case 2: Enrollment requirements
- **Persona:** Ahmed
- **Context:** Ahmed is interested in knowing the list of enrollment requirements.
- **Steps:**
   1. Ahmed starts a conversation with the application assistant.
   2. The system offers available actions.
   3. Ahmed selects "Ask about Enrollment requirements"
   4. The system provides information about Documents, fees, or actions required.
- **Errors or Problems:**
   -Wrong choice of actions chosen by the user which leads to unwanted output
