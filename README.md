# Python Zootopia

This project takes animal data from the Animals API (API Ninja) and creates a simple website that shows information about different animals.  
The goal is to learn how to use APIs, work with JSON data, and generate HTML with Python.

## What the program does

- Fetches animal data from the API.  
- Generates a website with cards for each animal.  
- If you enter an animal that doesn’t exist, it will show a message saying it’s not found.  
- The project has two main files:
  - data_fetcher.py – fetches data from the API.  
  - animals_web_generator.py – generates the website from the data.

## How to run

1. Clone the repository:

git clone <your-repo-url>
cd <your-folder>

2. Install dependencies:

pip install -r requirements.txt

3. Create a .env file in the root folder and add your API key:
API_KEY='your_api_key_here'

Make sure the .env file is in .gitignore so it stays private.

4. Run the website generator:
python animals_web_generator.py


Enter the name of an animal when asked. The website animals.html will be generated automatically.

## How to contribute

If you want to add or change something:

1. Fork the repository.  
2. Create a new branch.  
3. Make your changes.  
4. Send a pull request.


