# AVS ARM Template Generator
This repository is an Azure Webapp to generate AVS ARM Deployment Templates.  The app is a Flask webapp for Python.  This can be run anywhere with python and the required modules installed.  Azure blob storage is used to store the resulant json files.  
## Usage
1. Clone the repo  
`git clone https://github.com/khensler/AVS-ARM-GENERATOR`  
2. You may create a virtual envionrment in the repo directoy if wanted  
`python -m venv venv`  
3. Active the virtual enviornment.  This is dependent on your envionrment  
4. Install the required modules  
`python -m pip install -r requirements.txt`
5. Set the AZURE_STORAGE_CONNECTION_STRING envionrment variable to your blob storage connection string
6. Run the application  
`python -m flask run`

The app is now avabile at http://127.0.0.1:5000  
