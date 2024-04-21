# Authors
1. Shiven Chokshi
2. Dave Jose
3. Mayitreya Pasumarthy
4. Rahul Ramasubramanian

Created for [Bitcamp 2024](http://bit.camp)

# Introduction to MediCheck AI
MediCheck AI consists of a few different parts; the front-end, and the AI-powered backend.

The front-end of MediCheck AI is designed to be user-friendly and visually appealing, providing a seamless experience for both healthcare professionals and patients. Through the website, users can easily input surface-level patient information, symptoms, medical history, and lifestyle factors using intuitive forms and interfaces.

Upon submitting the necessary information, the data is securely transmitted to the AI-powered backend for analysis. The backend of MediCheck AI is where the magic happens. It comprises an advanced AI model, named MedLLaMa2, which has been trained on a vast dataset of medical examination questions and corresponding diagnoses.

One of the key features of MediCheck AI is its ability to run locally on affordable embedded systems, such as the Raspberry Pi 5. This local AI implementation using the MedLLaMa2 model ensures accessibility and reliability even in areas with limited internet connectivity, making it particularly valuable for underserved communities.

The inspiration for MediCheck AI stems from a deep-seated concern for healthcare disparities and a firm belief in the power of technology to address them. In many parts of the world, access to quality healthcare is not readily available, particularly in underserved and remote areas. Patients in these regions often face significant challenges in obtaining timely medical attention and diagnoses due to various factors such as limited healthcare infrastructure, shortage of medical professionals, and lack of internet access.

The idea was born out of a desire to leverage advancements in artificial intelligence and web technologies to provide preliminary medical assessments and guidance, even in the most remote and resource-constrained environments.

The MedLLaMa model represents the culmination of existing technology with immense potential to revolutionize the field of healthcare. As an AI-powered diagnostic tool, MedLLaMa leverages state-of-the-art machine learning techniques to analyze medical data and provide preliminary diagnoses.

# How We Built MediCheck AI
For the front-end of our website, we utilized HTML to create a user-friendly interface where patients can input information about their symptoms, medical history, and lifestyle habits. We incorporated radio buttons and text fields, allowing users to select options or type in relevant details. Additionally, CSS was employed to enhance the visual appeal and layout of the website, ensuring a seamless and engaging user experience.

On the backend, we employed Flask, a Python module for building simple website interactions, to collect the information entered by the patient on the website. Once the patient submits their information and Flask has retrieved it, the Ollama API passes the information to MedLLaMa2, and the language model processes the data and generates an input using the extracted information.

MedLLaMa2 is an advanced language model (forked from Meta’s LLaMa2 model) trained on a vast dataset of medical queries and corresponding diagnoses. It utilizes state-of-the-art natural language processing techniques to analyze the input data and generate an appropriate diagnosis based on the parameters provided. Once MedLLaMa2 processes the input, it responds with the suggested diagnosis.

# How to Use MediCheck AI
## What's Required?
1. Python3; Including the Flask and Ollama modules
2. At least 8 GB of RAM, and at least a 4-core CPU made within the last three years
3. Ollama; Including the MedLLaMa2 model
4. macOS or some flavor of Linux (Windows will work, only if WSL2 is used)

# Installation (All Operating Systems)
### Cloning the Repository
Clone the repository either by...
1. Clicking the `<> Code` button on the repository and downloading a zip file of the project, or by...
2. Typing `git clone https://github.com/mayitreya/medicheck_ai.git` into a terminal

### Downloading Ollama
*You will be self-hosting a large language model on your computer. It will take around 4-5 GB of storage, so make sure you have that much to spare*
1. Visit https://ollama.com/download and choose your operating system
2. If you're using Linux, run the command the website tells you to run, in order to install Ollama
3. Once Ollama is installed, run `ollama run medllama2` and wait for it to finish installing. You will know that it's finished once you see `>>> Send a message (/? for help)`
4. Control + D will escape the prompt

### Downloading the Python Modules We Need
1. If you don't have python3 installed, go ahead and do that first, for your specific OS
2. Run `pip3 install flask ollama` in your terminal
3. Once it finishes, this step is complete

### Using the Program Itself
1. Once the above steps are completed, make sure you are in the directory with `main.py` and the `templates` directory 
2. Now, open a terminal in this location and run `python3 main.py`
3. The website will be hosted at `http://127.0.0.1:5000` OR `http://127.0.0.1:8000`; whatever the terminal prompt says
4. If something doesn't work here, it means that you're missing some dependency. It's hard to say what it could be; just install what the terminal says is missing

### Done!
Go ahead and input some information into the online form and see the magic happen before your very eyes!

# Future Iterations of this Project
For the best possible experience, the questions that MediCheck AI presents the user should be dynamically generated based on the previous user response. They currently are not (the website is static), but as a future iteration, this would be an extremely solid idea.