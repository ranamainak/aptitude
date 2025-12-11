import random
import math
import pandas as pd

# ==========================================
# PART 1: HARD GENERATOR (The original 100)
# ==========================================
class HardGenerator:
    def gen_quadratic_series(self):
        a, b, c = random.randint(1, 3), random.randint(1, 5), random.randint(1, 10)
        seq = [a*n**2 + b*n + c for n in range(1, 7)]
        return {
            "Question": f"Find the next term: {', '.join(map(str, seq[:-1]))}, ___",
            "Type": "Number Series",
            "Answer": str(seq[-1]),
            "Difficulty": "Hard"
        }

    def gen_train_problem(self):
        speed = random.choice([36, 54, 72, 90]) # km/h (divisible by 18 for m/s)
        speed_ms = speed * (5/18)
        time = random.randint(10, 30)
        length = int(speed_ms * time)
        return {
            "Question": f"A train traveling at {speed} km/h crosses a pole in {time} seconds. Find the length of the train.",
            "Type": "Time & Distance",
            "Answer": f"{length} meters",
            "Difficulty": "Hard"
        }

    def gen_work_problem(self):
        # A in x days, B in y days. Together?
        a = random.choice([10, 12, 15, 20])
        b = random.choice([12, 15, 20, 30])
        total_days = (a * b) / (a + b)
        return {
            "Question": f"A can do a work in {a} days and B in {b} days. In how many days can they complete it together?",
            "Type": "Time & Work",
            "Answer": f"{total_days:.2f} days",
            "Difficulty": "Hard"
        }

    def gen_probability_marbles(self):
        r, g = random.randint(3, 8), random.randint(3, 8)
        total = r + g
        return {
            "Question": f"A bag contains {r} Red and {g} Green marbles. What is the probability of picking a Red marble?",
            "Type": "Probability",
            "Answer": f"{r}/{total}",
            "Difficulty": "Hard"
        }

    def generate_batch(self, count=100):
        funcs = [self.gen_quadratic_series, self.gen_train_problem, self.gen_work_problem, self.gen_probability_marbles]
        return [random.choice(funcs)() for _ in range(count)]


# ==========================================
# PART 2: EXPERT GENERATOR (The UltraHard 200)
# ==========================================
class ExpertGenerator:
    
    # 1. ELITE NUMBER SERIES (Geometric / Interleaved)
    def gen_complex_series(self):
        # Logic: Multiply by x, then add y (e.g., *2 + 1)
        start = random.randint(2, 9)
        mult = random.randint(2, 3)
        add = random.randint(1, 5)
        seq = [start]
        for _ in range(5):
            seq.append(seq[-1] * mult + add)
        
        return {
            "Question": f"Find the next term in the series: {', '.join(map(str, seq[:-1]))}, ___",
            "Type": "Elite Number Series",
            "Answer": str(seq[-1]),
            "Difficulty": "Expert"
        }

    # 2. ELITE PROBABILITY (Binomial Distribution / Biased Coins)
    def gen_binomial_prob(self):
        # Logic: Biased coin P(Head)=p. Tossed n times. Prob of exactly k heads.
        # Formula: nCk * p^k * (1-p)^(n-k)
        n = random.randint(4, 6) # Trials
        k = random.randint(2, n-1) # Successes
        p_num = 1
        p_den = random.choice([3, 4]) # 1/3 or 1/4 probability
        
        # We leave the answer as a formula or simplified fraction string for "Expert" users
        # Calculating exact nCk
        nCk = math.comb(n, k)
        
        return {
            "Question": f"A biased coin has a probability of {p_num}/{p_den} of landing Heads. If tossed {n} times, what is the probability of getting exactly {k} Heads?",
            "Type": "Elite Probability",
            "Answer": f"{nCk} * ({p_num}/{p_den})^{k} * ({p_den-p_num}/{p_den})^{n-k}",
            "Difficulty": "Expert"
        }

    # 3. ELITE GEOMETRY (Heron's Formula)
    def gen_herons_formula(self):
        # Generate sides that form a valid triangle
        while True:
            a = random.randint(5, 15)
            b = random.randint(5, 15)
            c = random.randint(5, 15)
            if a + b > c and a + c > b and b + c > a:
                break
        
        s = (a + b + c) / 2
        area_sq = s * (s - a) * (s - b) * (s - c)
        area = math.sqrt(area_sq)
        
        return {
            "Question": f"Find the area of a triangle with sides {a} cm, {b} cm, and {c} cm using Heron's Formula.",
            "Type": "Elite Geometry",
            "Answer": f"{area:.2f} sq cm",
            "Difficulty": "Expert"
        }

    # 4. ADVANCED COMBINATORICS (Circular Permutation)
    def gen_circular_perm(self):
        # Logic: Ways to seat n people around a table where 2 specific people MUST sit together.
        # Formula: (n-2)! * 2!
        n = random.randint(5, 9)
        ans = math.factorial(n - 2) * 2
        
        return {
            "Question": f"In how many ways can {n} people be seated around a circular table such that 2 specific people always sit together?",
            "Type": "Advanced Combinatorics",
            "Answer": str(ans),
            "Difficulty": "Expert"
        }

    # 5. HIGH ALGEBRA (Surds/Roots)
    def gen_surd_equation(self):
        # Solve sqrt(ax + b) = c
        c = random.randint(4, 10)
        a = random.randint(2, 5)
        # We work backwards: ax + b = c^2 => b = c^2 - ax
        # Pick x first to ensure integer solution
        x = random.randint(1, 10)
        val_inside = c**2
        b = val_inside - (a * x)
        
        # Equation: sqrt(ax + b) = c
        sign = "+" if b >= 0 else "-"
        
        return {
            "Question": f"Solve for x: sqrt({a}x {sign} {abs(b)}) = {c}",
            "Type": "High Algebra",
            "Answer": str(x),
            "Difficulty": "Expert"
        }

    def generate_batch(self, count=100):
        funcs = [
            self.gen_complex_series, 
            self.gen_binomial_prob, 
            self.gen_herons_formula, 
            self.gen_circular_perm,
            self.gen_surd_equation
        ]
        return [random.choice(funcs)() for _ in range(count)]