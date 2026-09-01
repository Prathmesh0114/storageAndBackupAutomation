Storage and Backup Automation

Python-based automation project for storage administration and infrastructure health checks.

Project Goal

The goal of this project is to automate common storage administration and monitoring activities using Python, REST APIs, and infrastructure automation tools.

Current Automation
NetApp Cluster Health Check

The first automation checks the health and availability of a NetApp ONTAP cluster through the ONTAP REST API.

The script is located at:

python/netapp/cluster-health.py
Current Workflow
Python Script
     |
     v
Environment Configuration
     |
     v
NetApp ONTAP REST API
     |
     v
Cluster Information
     |
     v
Health Report
Technologies
Python 3
REST API
NetApp ONTAP
Git
GitHub
python-dotenv
Requests
Project Structure
storageAndBackupAutomation/
│
├── python/
│   └── netapp/
│       └── cluster-health.py
│
├── tests/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
Configuration

Create a .env file in the project root:

NETAPP_HOST=
NETAPP_USERNAME=
NETAPP_PASSWORD=

Do not commit .env to GitHub.

The .env.example file is provided as a configuration template.

Installation

Clone the repository:

git clone <YOUR_REPOSITORY_URL>
cd storageAndBackupAutomation

Create a virtual environment:

python -m venv venv

Activate it on Windows:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt
Running the NetApp Health Check

From the project root:

python .\python\netapp\cluster-health.py

The script requires network access to the NetApp ONTAP REST API.

Author
Prathmesh Wankhade