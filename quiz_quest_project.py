import random
players = [] # List to store player names and scores
# Question bank with categories and questions
question_bank = {
    "History": [
        {"question": "Who was the first President of the United States?", "answer": "George Washington"},
        {"question": "In what year did World War II end?", "answer": "1945"},
        {"question": "What empire was ruled by Julius Caesar?", "answer": "Roman Empire"},
        {"question": "The Great Wall is located in which country?", "answer": "China"},
        {"question": "Who was the British Prime Minister during most of World War II?", "answer": "Winston Churchill"},
        {"question": "Which event started in 1789 and changed France forever?", "answer": "The French Revolution"},
        {"question": "Who discovered America in 1492?", "answer": "Christopher Columbus"},
        {"question": "In what year was the Declaration of Independence signed?", "answer": "1776"},
        {"question": "Which ancient civilization built the pyramids?", "answer": "Egyptians"},
        {"question": "Who was the first man to walk on the moon?", "answer": "Neil Armstrong"},
    ],
    "Science": [
        {"question": "What is the chemical symbol for water?", "answer": "H2O"},
        {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What gas do plants use for photosynthesis?", "answer": "Carbon dioxide"},
        {"question": "How many bones are in the adult human body?", "answer": "206"},
        {"question": "What is the largest organ of the human body?", "answer": "Skin"},
        {"question": "What is the center of an atom called?", "answer": "Nucleus"},
        {"question": "What type of animal is a Komodo dragon?", "answer": "Lizard"},
        {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
        {"question": "Which scientist developed the theory of relativity?", "answer": "Albert Einstein"},
        {"question": "What part of the cell contains DNA?", "answer": "Nucleus"},
    ],
    "Geography": [
        {"question": "What is the largest desert in the world?", "answer": "Sahara"},
        {"question": "What is the capital of Japan?", "answer": "Tokyo"},
        {"question": "Which river is the longest in the world?", "answer": "Nile"},
        {"question": "Mount Everest is part of which mountain range?", "answer": "Himalayas"},
        {"question": "What country has the most islands?", "answer": "Sweden"},
        {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
        {"question": "In which continent is the Amazon rainforest located?", "answer": "South America"},
        {"question": "What is the capital of Canada?", "answer": "Ottawa"},
        {"question": "Which ocean is the largest?", "answer": "Pacific Ocean"},
        {"question": "Which country is shaped like a boot?", "answer": "Italy"},
    ],
    "Sports": [
        {"question": "How many players are there on a soccer team on the field?", "answer": "11"},
        {"question": "Who has won the most Grand Slam titles in tennis?", "answer": "Novak Djokovic"},
        {"question": "What country hosted the 2016 Summer Olympics?", "answer": "Brazil"},
        {"question": "In basketball, how many points is a free throw worth?", "answer": "1"},
        {"question": "What sport uses a puck?", "answer": "Ice hockey"},
        {"question": "Who is known as 'The Greatest' in boxing?", "answer": "Muhammad Ali"},
        {"question": "In which country was golf first played?", "answer": "Scotland"},
        {"question": "How long is an Olympic swimming pool (in meters)?", "answer": "50"},
        {"question": "What is the nickname of the New Zealand rugby team?", "answer": "All Blacks"},
        {"question": "How many rings are there on the Olympic flag?", "answer": "5"},
    ],
    "Pop Culture": [
        {"question": "Who directed the movie 'Titanic'?", "answer": "James Cameron"},
        {"question": "What is the name of Harry Potter’s pet owl?", "answer": "Hedwig"},
        {"question": "Which singer is known as the 'Queen of Pop'?", "answer": "Madonna"},
        {"question": "What is the name of the kingdom where the Disney movie 'Frozen' takes place?", "answer": "Arendelle"},
        {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
        {"question": "In 'Friends,' what is the name of Ross's second wife?", "answer": "Emily"},
        {"question": "Which movie features the quote: 'May the Force be with you'?", "answer": "Star Wars"},
        {"question": "Who is the author of the 'Game of Thrones' book series?", "answer": "George R. R. Martin"},
        {"question": "What is the highest-grossing film of all time (as of 2024)?", "answer": "Avatar"},
        {"question": "Which superhero is known as the 'Caped Crusader'?", "answer": "Batman"},
    ],
}

# add new player to the game
def add_player(name):
    players.append({"name": name, "score": 0})
    print(f"🎮 {name} has joined the game!")

print("Welcome to the Quiz Quest!")
number_of_players = int(input("Enter the number of players (1-4): "))
if number_of_players < 1 or number_of_players > 4:
    print("Invalid number of players. Please enter a number between 1 and 4.")
    exit()
else:
    for i in range(number_of_players):
        name = input(f"Enter the name of Player {i + 1}: ")
        add_player(name)
        print(f"Welcome, {name}!")

if number_of_players == 1:
    print("You are playing solo!")
else:
    print(f"Great! You have {number_of_players} players in the game.")
print("")

    
print("Let's get started!")
print("You will be asked a series of questions. Answer them correctly to earn points.")
print("Good luck!")
print("")


#multy player game
def delete_question(category, question):
    for q in question_bank[category]:
        if q["question"] == question:
            question_bank[category].remove(q)
            break


number_of_rounds = int(input("Enter the number of rounds you want to play: "))
if number_of_rounds < 1:
    print("Invalid number of rounds. Please enter a positive number.")
    exit()
else:
    print(f"You have chosen to play {number_of_rounds} rounds.")
    print("")

for round_number in range(number_of_rounds):
    print(f"🏁 Round {round_number + 1}!")
    for player in players:
        print(f"🎤 {player['name']}, it's your turn!")
        category_choice = input("Choose a category (History, Science, Geography, Sports, Pop Culture): ").strip()

        if category_choice not in question_bank:
            print("Invalid category. Please choose a valid category.")
            continue

        if question_bank[category_choice]:
            question = random.choice(question_bank[category_choice])
            print(f"Category: {category_choice}")
            print(f"Question: {question['question']}")
            answer = input("Your answer: ")

            if answer.lower().strip() == question["answer"].lower().strip():
                print("✅ Correct!")
                player["score"] += 1
            else:
                print(f"❌ Incorrect! The correct answer is: {question['answer']}")

            delete_question(category_choice, question["question"])
        else:
            print(f"All questions in the category '{category_choice}' have been answered.")

        print(f"{player['name']}, your total score is: {player['score']}")
        print("")

the_winner = max(players, key=lambda x: x["score"])
print(f"🏆 The winner is {the_winner['name']} with a score of {the_winner['score']}!")