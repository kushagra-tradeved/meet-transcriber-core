cat << 'EOF' | sed 's/\*\]//g' > README.md
# Kushagra Tradeved Projects

This repository serves as a centralized space for the core applications developed under the `kushagra-tradeved` workspace[cite: 1, 2]. It currently houses two primary projects: **Tradeved Copilot MVP**[cite: 1] and **Meet Transcriber Core**[cite: 2].

---

## 1. Tradeved Copilot MVP

The Tradeved Copilot is a Python-based intelligent mentor system equipped with conversational routing, safety guardrails, and Azure integration[cite: 1]. It utilizes local Excel datasets to drive its intelligence engine and is natively configured for serverless deployment on Vercel[cite: 1].

### Repository Structure

*   **`.gitignore`**: Specifies files and directories that should be ignored by version control[cite: 1].
*   **`main.py`**: Serves as the primary entry point for running the core application[cite: 1].
*   **`requirements.txt`**: Lists all the necessary Python dependencies required to run the project[cite: 1].
*   **`test_azure.py`**: A dedicated testing script used for validating Azure service integrations[cite: 1].
*   **`vercel.json`**: The core configuration file for deploying the application seamlessly via Vercel[cite: 1].
*   **`api/index.py`**: Functions as the main serverless API endpoint, structured to handle web requests[cite: 1].

#### Application Modules (`src/`)
*   **`src/config.py`**: Manages the environment variables and configuration parameters of the application[cite: 1].
*   **`src/data_loader.py`**: Implements the logic required to ingest, read, and parse the Excel-based intelligence datasets[cite: 1].
*   **`src/guardrails.py`**: Houses the safety guardrails and input/output validation layers[cite: 1].
*   **`src/mentor_voice.py`**: Defines the unique persona, stylistic tone, and behavioral characteristics of the mentor[cite: 1].
*   **`src/router.py`**: Responsible for routing incoming user queries and orchestrating the operational flow[cite: 1].

#### Data Assets (`data/`)
*   **`tradeved_mentor_intelligence_dataset_v4.xlsx`**: The primary knowledge base defining core intelligence[cite: 1].
*   **`tradeved_mentor_longform_session_dataset_v3.xlsx`**: Structured data used to guide extended mentoring sessions[cite: 1].
*   **`tradeved_mentor_state_transition_layer_v3_1.xlsx`**: Controls the state management, transition logic, and dialog flow[cite: 1].

### Setup and Deployment
1. Ensure Python is installed in your local environment.
2. Install the required project dependencies by running `pip install -r requirements.txt`[cite: 1].
3. Execute `main.py` to start the application locally[cite: 1]. 
4. For deployment, Vercel serverless functions are handled automatically via the `api/index.py` routing and `vercel.json` file[cite: 1].

---

## 2. Meet Transcriber Core

The Meet Transcriber Core is a Python-based application that manages meeting audio transcription through a centralized processing engine[cite: 2].

### Repository Structure

*   **`LICENSE`**: Defines the licensing terms and distribution rules for the repository[cite: 2].
*   **`config.py`**: A Python script designed to handle the application's configuration settings[cite: 2].
*   **`engine.py`**: A Python script containing the core operational logic for the transcriber engine[cite: 2].
*   **`main.py`**: The primary entry point script used to execute the application[cite: 2].
*   **`requirements.txt`**: A standard text file that lists all the necessary Python dependencies[cite: 2].
*   **`utils.py`**: A Python file containing helper functions and utilities used throughout the project[cite: 2].

### Setup and Execution
1. Ensure Python is installed in your local environment.
2. Install the required packages by pointing your package manager to the included `requirements.txt` file[cite: 2].
3. Configure your environment variables in `config.py` as needed[cite: 2].
4. Start the program by running `main.py` from your terminal[cite: 2].
EOF
