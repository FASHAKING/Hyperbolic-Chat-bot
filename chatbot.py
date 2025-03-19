# RUNNING NON-STOP



import requests
import time
import random
import json

# API Configuration
URL = "https://api.hyperbolic.xyz/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_HYPERBOLIC_API"
}

# Function to generate a random question
def generate_random_question():
    subjects = ["Math", "Science", "History", "Literature", "Technology", "Health", "Travel", "Sports", "Art", "Music"]
    question_types = ["What is", "Who is", "Where is", "Why is", "How is", "Can you explain", "What are the benefits of", "How does"]
    topics = {
        "Math": ["addition", "subtraction", "multiplication", "division", "algebra", "calculus", "geometry"],
        "Science": ["biology", "chemistry", "physics", "astronomy", "geology", "ecology"],
        "History": ["World War II", "Ancient Rome", "The Renaissance", "The Industrial Revolution", "Medieval Times", "The Enlightenment"],
        "Literature": ["Hamlet", "1984", "Pride and Prejudice", "To Kill a Mockingbird", "Moby Dick", "War and Peace"],
        "Technology": ["quantum computing", "blockchain", "artificial intelligence", "virtual reality", "3D printing", "self-driving cars"],
        "Health": ["meditation", "yoga", "exercise", "stress reduction", "healthy eating", "sleep"],
        "Travel": ["Europe", "Asia", "Africa", "North America", "South America", "Australia"],
        "Sports": ["football", "basketball", "tennis", "golf", "baseball", "soccer"],
        "Art": ["painting", "sculpture", "photography", "music", "dance", "theater"],
        "Music": ["classical", "rock", "jazz", "pop", "hip-hop", "country"]
    }
    
    subject = random.choice(subjects)
    question_type = random.choice(question_types)
    topic = random.choice(topics[subject])
    question = f"{question_type} {topic} related to {subject}?"
    return question

# Function to send API request
def send_chat_request(question):
    data = {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "max_tokens": 32768,
        "temperature": 0.7,
        "top_p": 0.9
    }
    
    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        response.raise_for_status()
        result = response.json()
        answer = result['choices'][0]['message']['content']
        return answer
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError as conn_err:
        return f"Connection error occurred: {conn_err}"
    except requests.exceptions.Timeout as timeout_err:
        return f"Timeout error occurred: {timeout_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Request error occurred: {req_err}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Function to save questions and answers to a file
def save_questions_and_answers(questions, answers, filename="questions_and_answers.json"):
    data = [{"question": q, "answer": a} for q, a in zip(questions, answers)]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Main bot loop
def run_chat_bot():
    print("Starting automated chat bot that runs non-stop...")
    questions = []
    answers = []
    question_count = 0
    
    while True:
        # Generate a new question
        question = generate_random_question()
        questions.append(question)
        question_count += 1
        
        # Send request and print results
        print(f"\nQuestion {question_count}: {question}")
        answer = send_chat_request(question)
        print(f"Answer: {answer}")
        answers.append(answer)
        
        # Random delay between 1-2 minutes (60-120 seconds)
        delay = random.uniform(60, 120)
        print(f"Waiting {delay:.1f} seconds before next question...")
        time.sleep(delay)
        
        # Optionally, save the questions and answers periodically
        if question_count % 1000 == 0:
            print(f"Saving questions and answers after {question_count} questions...")
            save_questions_and_answers(questions, answers)
            # Clear the lists to save memory
            questions.clear()
            answers.clear()

# Run the bot
if __name__ == "__main__":
    run_chat_bot()



