import json
from question_engine import HardGenerator, ExpertGenerator

def main():
    # 1. Generate HARD Questions (e.g., 500)
    hard_gen = HardGenerator()
    hard_data = hard_gen.generate_batch(500)
    
    with open('hard_questions.json', 'w') as f:
        json.dump(hard_data, f, indent=2)
    print("Generated 500 Hard questions.")

    # 2. Generate EXPERT Questions (e.g., 500)
    expert_gen = ExpertGenerator()
    expert_data = expert_gen.generate_batch(500)
    
    with open('expert_questions.json', 'w') as f:
        json.dump(expert_data, f, indent=2)
    print("Generated 500 Expert questions.")

if __name__ == "__main__":
    main()