# Define the disorder mapping
disorder_mapping = {
    'anxiety': "Anxiety Disorder",
    'depression': "Depression",
    'stress': "Stress"
}

# Define solutions for each disorder
solutions = {
    'anxiety': """Solution for Anxiety Disorder:
    - Practice mindfulness and meditation to reduce stress.
    - Engage in physical activity like yoga or jogging to manage anxiety.
    - Consider cognitive behavioral therapy (CBT).
    - Consult a therapist if anxiety interferes with daily activities.""",

    'depression': """Solution for Depression:
    - Engage in physical exercise to improve mood.
    - Maintain a regular sleep routine.
    - Socialize with supportive friends or family members.
    - Seek therapy and, in severe cases, consider medication.""",

    'stress': """Solution for Stress:
    - Practice relaxation techniques such as deep breathing and meditation.
    - Organize tasks to avoid feeling overwhelmed.
    - Take breaks and engage in physical activities to reduce stress.
    - Seek counseling or support groups if stress is unmanageable."""
}

# Define questions and options with corresponding weights for disorders
quiz = [
    # Anxiety Disorder Questions
    {
        'question': "Q1: How often do you feel nervous or anxious?",
        'options': {
            1: {"label": "Never", "weight": {'anxiety': 1, 'stress': 1}},
            2: {"label": "Sometimes", "weight": {'anxiety': 2, 'stress': 2}},
            3: {"label": "Often", "weight": {'anxiety': 3, 'stress': 3}},
            4: {"label": "Almost Always", "weight": {'anxiety': 4, 'stress': 4}},
            5: {"label": "Always", "weight": {'anxiety': 5, 'stress': 5}}
        }
    },
    {
        'question': "Q2: How often do you experience sudden fear or panic without an apparent reason?",
        'options': {
            1: {"label": "Never", "weight": {'anxiety': 1}},
            2: {"label": "Sometimes", "weight": {'anxiety': 2}},
            3: {"label": "Often", "weight": {'anxiety': 3}},
            4: {"label": "Almost Always", "weight": {'anxiety': 4}},
            5: {"label": "Always", "weight": {'anxiety': 5}}
        }
    },

    # Depression Disorder Questions
    {
        'question': "Q3: How often do you feel sad or hopeless?",
        'options': {
            1: {"label": "Never", "weight": {'depression': 1}},
            2: {"label": "Sometimes", "weight": {'depression': 2}},
            3: {"label": "Often", "weight": {'depression': 3}},
            4: {"label": "Almost Always", "weight": {'depression': 4}},
            5: {"label": "Always", "weight": {'depression': 5}}
        }
    },
    {
        'question': "Q4: How often do you feel tired or without energy, even after resting?",
        'options': {
            1: {"label": "Never", "weight": {'depression': 1}},
            2: {"label": "Sometimes", "weight": {'depression': 2}},
            3: {"label": "Often", "weight": {'depression': 3}},
            4: {"label": "Almost Always", "weight": {'depression': 4}},
            5: {"label": "Always", "weight": {'depression': 5}}
        }
    },

    # Stress Questions
    {
        'question': "Q5: How often do you feel overwhelmed with daily tasks?",
        'options': {
            1: {"label": "Never", "weight": {'stress': 1}},
            2: {"label": "Sometimes", "weight": {'stress': 2}},
            3: {"label": "Often", "weight": {'stress': 3}},
            4: {"label": "Almost Always", "weight": {'stress': 4}},
            5: {"label": "Always", "weight": {'stress': 5}}
        }
    },
    {
        'question': "Q6: Do you find it hard to relax, even in your free time?",
        'options': {
            1: {"label": "Never", "weight": {'stress': 1}},
            2: {"label": "Sometimes", "weight": {'stress': 2}},
            3: {"label": "Often", "weight": {'stress': 3}},
            4: {"label": "Almost Always", "weight": {'stress': 4}},
            5: {"label": "Always", "weight": {'stress': 5}}
        }
    }
]

# Function to ask the quiz and calculate the percentage score
def ask_quiz(quiz):
    total_possible_score = len(quiz) * 5  # Max score per question is 5
    scores = {'anxiety': 0, 'depression': 0, 'stress': 0}

    print("Please answer the following questions:\n")

    for question in quiz:
        while True:
            print(question['question'])
            for opt_num, option in question['options'].items():
                print(f"{opt_num}. {option['label']}")
            try:
                response = int(input("\nSelect an option (1-5): "))
                if response in question['options']:
                    weights = question['options'][response]['weight']
                    for disorder, score in weights.items():
                        scores[disorder] += score
                    break
                else:
                    print("Invalid choice. Please select a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Calculate percentage scores
    percentage_scores = {disorder: (score / total_possible_score) * 100 for disorder, score in scores.items()}
    max_disorder = max(percentage_scores, key=percentage_scores.get)

    return max_disorder, percentage_scores[max_disorder]

# Main function to run the quiz
def main():
    disorder, score_percentage = ask_quiz(quiz)
    disorder_name = disorder_mapping[disorder]
    solution = solutions[disorder]

    # Display the result
    print(f"\nBased on your responses, the most likely condition is: {disorder_name}.")
    print(f"Score: {score_percentage:.2f}%")
    print(f"\n{solution}")

if __name__ == "__main__":
    main()
