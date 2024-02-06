import requests
from question_model import Question
from quiz_brain import QuizBrain

# Fetch categories from the API
categories_url = "https://opentdb.com/api_category.php"
categories_response = requests.get(categories_url)
categories_data = categories_response.json()
categories = categories_data["trivia_categories"]

# Present categories to the user
print("Select a category:")
for category in categories:
    print(f"{category['id']}: {category['name']}")

# Ask user for category and difficulty
category_id = input("Enter the category ID: ")
difficulty = input("Enter the difficulty (easy, medium, hard): ")

# Fetch data from the API based on user's input
amount = 15
while True:
    url = f"https://opentdb.com/api.php?amount={amount}&category={category_id}&difficulty={difficulty}&type=boolean"
    response = requests.get(url)
    data = response.json()
    if data["response_code"] == 0:
        break
    elif amount <= 0:
        print("We are sorry, we couldn't find enough questions for the game.")
        exit()
    else:
        amount -= 5
        print("We are trying to find data for the game. Please wait.")

question_data = data["results"]

# Create question bank using API data
question_bank = [Question(question["question"], question["correct_answer"]) for question in question_data]

# Initialize QuizBrain with question bank
quiz = QuizBrain(question_bank)

# Loop through questions until there are none left
while quiz.still_has_questions():
    # Ask next question
    quiz.next_question()
