---
description: A step by step how to do this project
---

# READ ME PLZ

## Step-by-Step Guide for Setting Up Ollama with Docker, Python, and Whisper

This guide will walk you through how to install and run Ollama in Docker, set up a Python environment, and install Whisper with the necessary libraries. We assume you already have Python and pip installed.

#### Step 1: Install Docker Desktop

1. Download Docker Desktop from the [official website](https://www.docker.com).
2. Follow the installation steps for your operating system (Windows, macOS, or Linux).
3. After installation, open Docker Desktop to make sure it’s running properly.

#### Step 2: Install the Ollama Docker Image

1. Open a terminal or command prompt.
2.  Pull the Ollama image by running this command:

    ```bash
    docker pull ollama/llama3.1
    ```
3.  Check if the image is installed by running:

    ```bash
    bashCopy codedocker images
    ```

    You should see the Ollama image in the list.

#### Step 3: Set Up a Python Environment

1. Download and install Visual Studio Code (VS Code) from [here](https://code.visualstudio.com/).
2. Open VS Code and create a new file named `main.py`.
3. Press `Ctrl + Shift + P` to open the command palette.
4. Type and select "Python: Create Environment."
5. Wait for the environment to load. You will then be prompted to choose between `venv` and `conda`. Select `venv`.
6. Choose to create a new environment.
7. After the environment is set up, make sure it is activated.
8.  Install the required Python package with this command in the terminal:

    ```bash
    bashCopy codepip install requests
    ```

#### Step 4: Install Whisper, Torch, and Sounddevice

1.  Install Whisper using the following command:

    ```bash
    bashCopy codepip install git+https://github.com/openai/whisper.git
    ```
2.  Install `torch`, which is required for Whisper:

    ```bash
    bashCopy codepip install torch
    ```
3.  Install `sounddevice` to manage audio input/output for Whisper:

    ```bash
    bashCopy codepip install sounddevice
    ```

#### Step 5: Test the Ollama Setup

1.  Copy and paste the following Python script into a file in your project (for example, `test_script.py`):

    ```python
    pythonCopy codeimport requests
    import json

    url = 'http://localhost:11434/api/generate'
    data = {
        "model": "llama3.1",
        "prompt": "Why is the sky blue?"
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)

    response_text = ""
    # Check if the response is chunked and accumulate the parts
    for chunk in response.iter_lines():
        if chunk:
            chunk_data = json.loads(chunk.decode('utf-8'))  # Parse each chunk of the response
            response_text += chunk_data.get('response', '')  # Accumulate the 'response' field

    print(response_text)
    ```
2.  Run the script by typing:

    ```bash
    bashCopy codepython test_script.py
    ```
3. This script will send a request to the Llama model, asking, "Why is the sky blue?" and print the response. Ensure that Docker is running, and the Ollama image is active.

#### Conclusion

You have successfully installed Docker Desktop, pulled the Ollama image, set up a Python environment, and installed Whisper along with Torch and Sounddevice. The environment is now ready for further development and running scripts.
