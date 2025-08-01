# QUESTIONS
questions = {
    "AI Engineering": {
        "easy": [
            {
                "question": "What does 'AI' stand for?",
                "options": ["Automated Intelligence", "Artificial Intelligence", "Algorithmic Inference", "Advanced Interface"],
                "answer": 1
            },
            {
                "question": "Which programming language is most commonly used in AI development?",
                "options": ["Java", "Python", "C++", "JavaScript"],
                "answer": 1
            },
            {
                "question": "What is the name of the AI that defeated the world champion in Go?",
                "options": ["Deep Blue", "AlphaGo", "Watson", "GPT-3"],
                "answer": 1
            },
            {
                "question": "Which of these is NOT a machine learning framework?",
                "options": ["TensorFlow", "PyTorch", "Keras", "Django"],
                "answer": 3
            },
            {
                "question": "What type of AI specializes in understanding human language?",
                "options": ["Computer Vision", "Natural Language Processing", "Robotics", "Neural Networks"],
                "answer": 1
            }
        ],
        "hard": [
            {
                "question": "What activation function is commonly used in output layers for binary classification?",
                "options": ["ReLU", "Sigmoid", "Tanh", "Leaky ReLU"],
                "answer": 1
            },
            {
                "question": "Which neural network architecture is best suited for image recognition?",
                "options": ["RNN", "CNN", "GAN", "Transformer"],
                "answer": 1
            },
            {
                "question": "What does 'BERT' stand for in NLP?",
                "options": ["Bidirectional Encoder Representations from Transformers", 
                           "Binary Encoded Representation Technology",
                           "Basic Embedded Retrieval Technique",
                           "Bidirectional Entity Recognition Transformer"],
                "answer": 0
            },
            {
                "question": "Which technique helps prevent overfitting in neural networks?",
                "options": ["Batch Normalization", "Data Augmentation", "Dropout", "All of the above"],
                "answer": 3
            },
            {
                "question": "What is the name of Google's multimodal AI model released in 2023?",
                "options": ["GPT-4", "Gemini", "Claude", "Llama"],
                "answer": 1
            }
        ]
    },
    "Football": {
        "easy": [
            {
                "question": "How many players are on a football team during a match?",
                "options": ["9", "10", "11", "12"],
                "answer": 2
            },
            {
                "question": "Which country won the 2022 FIFA World Cup?",
                "options": ["France", "Brazil", "Argentina", "Germany"],
                "answer": 2
            },
            {
                "question": "What is the maximum length of a football match?",
                "options": ["90 minutes", "120 minutes", "150 minutes", "No limit"],
                "answer": 1
            },
            {
                "question": "Which player has won the most Ballon d'Or awards?",
                "options": ["Cristiano Ronaldo", "Lionel Messi", "Michel Platini", "Johan Cruyff"],
                "answer": 1
            },
            {
                "question": "What color card indicates a sending-off in football?",
                "options": ["Yellow", "Red", "Green", "Black"],
                "answer": 1
            }
        ],
        "hard": [
            {
                "question": "Which team won the first ever FIFA World Cup in 1930?",
                "options": ["Brazil", "Uruguay", "Argentina", "Italy"],
                "answer": 1
            },
            {
                "question": "Who is the all-time top scorer in the UEFA Champions League?",
                "options": ["Raúl", "Cristiano Ronaldo", "Lionel Messi", "Robert Lewandowski"],
                "answer": 1
            },
            {
                "question": "Which country hosted the 2010 FIFA World Cup?",
                "options": ["Germany", "South Africa", "Brazil", "Russia"],
                "answer": 1
            },
            {
                "question": "What is the name of the football tournament for African national teams?",
                "options": ["Africa Cup", "CAF Championship", "Africa Nations Cup", "All of the above"],
                "answer": 2
            },
            {
                "question": "Which player scored the 'Hand of God' goal?",
                "options": ["Diego Maradona", "Pele", "Zinedine Zidane", "Ronaldo Nazário"],
                "answer": 0
            }
        ]
    },
    "Cameroon History": {
        "easy": [
            {
                "question": "In which year did Cameroon gain independence?",
                "options": ["1956", "1960", "1965", "1970"],
                "answer": 1
            },
            {
                "question": "Who was Cameroon's first president?",
                "options": ["Paul Biya", "Ahmadou Ahidjo", "John Ngu Foncha", "Samuel Eto'o"],
                "answer": 1
            },
            {
                "question": "What is the capital city of Cameroon?",
                "options": ["Douala", "Yaoundé", "Bamenda", "Buea"],
                "answer": 1
            },
            {
                "question": "Which European country colonized Cameroon?",
                "options": ["France", "Britain", "Germany", "Both France and Britain"],
                "answer": 3
            },
            {
                "question": "What is the official currency of Cameroon?",
                "options": ["CFA Franc", "Cameroon Dollar", "West African Peso", "Central African Pound"],
                "answer": 0
            }
        ],
        "hard": [
            {
                "question": "Which year did Cameroon first qualify for the FIFA World Cup?",
                "options": ["1982", "1990", "1994", "1998"],
                "answer": 0
            },
            {
                "question": "What was the name of the armed conflict in Cameroon from 1956-1971?",
                "options": ["Bamileke War", "Cameroon Civil War", "UPC Rebellion", "Anglophone Crisis"],
                "answer": 2
            },
            {
                "question": "Which Cameroonian won the African Player of the Year award most times?",
                "options": ["Samuel Eto'o", "Roger Milla", "Patrick Mboma", "Thomas N'Kono"],
                "answer": 0
            },
            {
                "question": "What is the name of Cameroon's highest mountain?",
                "options": ["Mount Cameroon", "Mount Oku", "Mount Manengouba", "Mount Bamboutos"],
                "answer": 0
            },
            {
                "question": "Which Cameroonian city was the former capital of German Kamerun?",
                "options": ["Douala", "Buea", "Limbe", "Kumba"],
                "answer": 1
            }
        ]
    }
}

# Quiz functions
def display_categories():
    print("\n=== QUIZ MASTER ===")
    print("Categories:", ", ".join(questions.keys()))

def select_category_difficulty():
    while True:
        category = input("\nChoose a category: ").strip().title()
        if category in questions:
            break
        print("Invalid category. Please try again.")
    
    while True:
        difficulty = input("Choose difficulty (easy/hard): ").strip().lower()
        if difficulty in ["easy", "hard"]:
            break
        print("Invalid difficulty. Please choose 'easy' or 'hard'.")
    
    return category, difficulty

def run_quiz(category, difficulty):
    quiz_questions = questions[category][difficulty]
    score = 0
    total_questions = len(quiz_questions)
    
    print(f"\nStarting {category} ({difficulty}) quiz!")
    print(f"Total questions: {total_questions}\n")
    
    for i, question in enumerate(quiz_questions, 1):
        print(f"Question {i}: {question['question']}")
        for j, option in enumerate(question['options']):
            print(f"{chr(65+j)}) {option}")
        
        while True:
            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            print("Invalid input. Please enter A, B, C, or D")
        
        if ord(user_answer) - 65 == question['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {chr(65 + question['answer'])}")
        
        print(f"Current score: {score}/{i}\n")
    
    print("\n=== QUIZ COMPLETE ===")
    print(f"Final score: {score}/{total_questions}")
    print(f"Percentage: {(score/total_questions)*100:.1f}%")

# Main program
def main():
    display_categories()
    category, difficulty = select_category_difficulty()
    run_quiz(category, difficulty)

# Start the quiz
if __name__ == "__main__":
    main()