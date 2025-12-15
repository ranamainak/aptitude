import json
import os
from question_engine import HardGenerator, ExpertGenerator

def save_to_json(data, filename):
    # Save the list of question dictionaries to a JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Successfully generated {len(data)} questions in {filename}")

def main():
    print("--- Starting Daily Question Generation ---")

    # 1. Generate HARD Questions (General Aptitude)
    try:
        hard_gen = HardGenerator()
        # Generate 50 unique questions
        hard_questions = hard_gen.generate_batch(50) 
        save_to_json(hard_questions, 'hard_questions.json')
    except Exception as e:
        print(f"ERROR generating Hard questions: {e}")

    # 2. Generate EXPERT Questions (Advanced Logic)
    try:
        expert_gen = ExpertGenerator()
        # Generate 50 unique questions
        expert_questions = expert_gen.generate_batch(50)
        save_to_json(expert_questions, 'expert_questions.json')
    except Exception as e:
        print(f"ERROR generating Expert questions: {e}")

    print("--- Generation Complete ---")

if __name__ == "__main__":
    main()
