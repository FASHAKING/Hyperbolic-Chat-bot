# Hyperbolic Labs Chat scripts

This repository contains an automated chatbot built using the [Hyperbolic Labs](https://app.hyperbolic.xyz/) API. The chatbot asks random, unique, pre-defined questions non-stop and retrieves answers from the API, simulating a conversational AI experience. It’s a fun demonstration of how to integrate Hyperbolic Labs' AI models into a Python application.
## About Hyperbolic Labs
[Hyperbolic labs](https://hyperbolic.xyz/) is an accessible and affordable platform for AI development, offering open-access AI models and scalable computing resources via their API.

To get more details about what [Hyperbolic labs](https://hyperbolic.xyz/) entails, visit their [Official Documentation](https://docs.hyperbolic.xyz/docs/getting-started)

![GaltoQhbMAAmFSP](https://github.com/user-attachments/assets/f82f0aca-1a30-4ce2-8179-a6a009cda4d3)
## Specification of the Repository
- Generate random question in different topics and field.
- It runs continously until stopped or encounters an error or limited by API.
- Randomly selects and asks questions without repetition.
- Integrates with the Hyperbolic Labs API to fetch answers.
- Adds random delays (1-2 minutes) between questions to simulate natural pacing.
- Built with Python and the `requests` library.

## Prerequisites
- Have a [Hyperbolic account](https://x.com/FASHAKING3/status/1901599197091991957)
- Python 3.6+
- A [Hyperbolic API key](https://app.hyperbolic.xyz/settings) (replace the placeholder in the code with your own key)


## Setup

1. Install Packages
```console
sudo apt update && sudo apt upgrade -y
sudo apt install git screen python3 python3-pip python3-venv -y
```

2. Clone the Repository
```console
git clone [https://github.com/FASHAKING/Hyperbolic-Chat-bot](https://github.com/FASHAKING/Hyperbolic-Chat-bot.git)
cd Hyperbolic-Chat-bot
```
3. Install Dependencies
```console
python3 -m venv venv
source venv/bin/activate
pip install requests
```
4. Configure the API Key
Replace the YOUR_HYPERBOLIC_API in chatbot.py with your own Hyperbolic API Key:
```console
nano chatbot.py
```
5. Create A screen for it (optional)
 This help you run the script on a minimizable screen in background.
```console
screen -S hyperbolic
```

  To retuen to the screen
```console
screen -r hyperbolic
```
  To kill screen: Ctrl+C or command: screen -XS chat quit


6. Run the Chatbot
Execute the script to start the chatbot:
```console
python3 chatbot.py
```
  Once running to minimize screen: CTRL+A+D

## Usage
The chatbot will:

- Generate random question in different topics and field.
- It runs continously until stopped or encounters an error or limited by API.
- Randomly selects and asks questions without repetition.
- Integrates with the Hyperbolic Labs API to fetch answers.

  
## Example output:
![Screenshot 2025-03-19 120149](https://github.com/user-attachments/assets/fd368694-030a-4227-ade6-68e914b6e328)

## Caution
- A [Hyperbolic account](https://x.com/FASHAKING3/status/1901599197091991957) is required in other to get an API.
- Be mindful of API usage limits and costs depending on your Hyperbolic Labs plan.
- You are free to modify the parameters used in generating random `questions`  in the  `chatbot.py` to suit your taste or wants!
