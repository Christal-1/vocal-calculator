Voice Calculator

Description

The Voice Calculator is a Python application that allows users to perform mathematical calculations using voice commands. It utilizes speech recognition to convert spoken expressions into text and evaluates the results using Python's built-in eval function. The application can also speak the results back to the user using text-to-speech functionality.

Features

    Voice Input: Speak mathematical expressions to perform calculations.
    Text-to-Speech: The app reads out the results of calculations.
    Continuous Operation: The app asks if the user wants to perform another calculation or exit.
    Error Handling: The app handles unrecognized speech and connection errors gracefully.

Requirements

    Python 3.x
    speech_recognition library
    pyttsx3 library
    pyaudio library

Installation

    Clone the Repository:

        Using HTTPS:

        bash

git clone https://github.com/Christal-1/vocal-calculator.git
cd vocal-calculator

Using SSH:

bash

    git clone git@github.com:Christal-1/vocal-calculator.git
    cd vocal-calculator

Install Dependencies:

bash

pip install speechrecognition pyttsx3 pyaudio


Usage

    Run the Application:

    bash

    python voice_calculator.py

    Speak Commands:
        After the application starts, speak a mathematical expression, such as "five plus three."
        The result will be calculated and spoken back to you.
        The application will ask if you want to perform another calculation or exit.

    Handling Speech:
        If the application does not understand your input, it will prompt you again.
        Say "yes" to continue with another calculation or "no" to exit the application.

Example

    User: "What is 7 multiplied by 8?"
    Application: "The result is 56."
    Application: "Do you want to perform another calculation? Say 'yes' to continue or 'no' to exit."
    User: "No."
    Application: "Goodbye!"

Troubleshooting

    No Response: Ensure your microphone is properly connected and functioning. Speak clearly and directly into the microphone.
    Errors in Calculation: The application uses Python’s eval function, which might encounter errors if the input is not a valid mathematical expression. Make sure to speak clearly and use proper mathematical terminology.

Contributing

Feel free to fork the repository. If you find any issues or have suggestions for improvements, please open an issue or a pull request.

