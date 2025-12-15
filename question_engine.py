import random
import math
import datetime

# ==========================================
# PART 1: HARD GENERATOR (General Aptitude)
# Focus: Applied Math, Arithmetic, Logical Reasoning
# ==========================================
class HardGenerator:

    # --- 1. BOATS & STREAMS ---
    def gen_boats_streams(self):
        boat = random.randint(12, 20)
        stream = random.randint(2, 6)
        dist = random.choice([24, 36, 48, 60, 72])
        
        mode = random.choice(['upstream', 'downstream'])
        if mode == 'upstream':
            time = dist / (boat - stream)
            return {
                "Question": f"A boat rows {dist} km upstream against a current of {stream} km/hr. If the boat's speed in still water is {boat} km/hr, find the time taken.",
                "Answer": f"{time:.2f} hours",
                "Type": "Boats & Streams"
            }
        else:
            time = dist / (boat + stream)
            return {
                "Question": f"A boat speeds downstream for {dist} km. Boat speed is {boat} km/hr and river flows at {stream} km/hr. Find the time taken.",
                "Answer": f"{time:.2f} hours",
                "Type": "Boats & Streams"
            }

    # --- 2. CLOCKS ---
    def gen_clock_angle(self):
        h, m = random.randint(1, 12), random.choice([10, 15, 20, 25, 30, 40, 50])
        angle = abs((30 * h) - (5.5 * m))
        angle = min(angle, 360 - angle)
        return {
            "Question": f"Calculate the smaller angle between the two hands of a clock at {h}:{m}.",
            "Answer": f"{angle} degrees",
            "Type": "Clocks"
        }

    # --- 3. CALENDARS ---
    def gen_calendar_day(self):
        base = datetime.date(2023, 1, 1) # Sunday
        offset = random.randint(50, 2000)
        target = base + datetime.timedelta(days=offset)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return {
            "Question": f"If Jan 1, 2023 was a Sunday, what day of the week is {target.strftime('%b %d, %Y')}?",
            "Answer": days[target.weekday()],
            "Type": "Calendars"
        }

    # --- 4. PIPES & CISTERNS ---
    def gen_pipes_leak(self):
        fill = random.choice([10, 12, 15])
        leak = random.choice([20, 30, 60])
        net = (fill * leak) / (leak - fill)
        return {
            "Question": f"Pipe A fills a tank in {fill} hrs. A leak at the bottom empties it in {leak} hrs. If both are open, how long to fill the tank?",
            "Answer": f"{net:.2f} hours",
            "Type": "Pipes & Cisterns"
        }

    # --- 5. RACES ---
    def gen_race_logic(self):
        track = random.choice([100, 200, 400])
        v1 = random.randint(8, 12)
        v2 = v1 - random.randint(1, 2)
        # Time for winner
        t = track / v1
        # Distance loser runs
        d2 = v2 * t
        beat = track - d2
        return {
            "Question": f"In a {track}m race, A runs at {v1} m/s and B at {v2} m/s. By what distance does A beat B?",
            "Answer": f"{beat:.1f} meters",
            "Type": "Races"
        }

    # --- 6. PROFIT & LOSS (Dishonest Dealer) ---
    def gen_dishonest_dealer(self):
        false_w = random.choice([800, 900, 950])
        profit = ((1000 - false_w) / false_w) * 100
        return {
            "Question": f"A dishonest dealer professes to sell goods at CP but uses {false_w}g weight for 1kg. Find gain %.",
            "Answer": f"{profit:.2f}%",
            "Type": "Profit & Loss"
        }

    # --- 7. MENSURATION (Melting) ---
    def gen_melting_cubes(self):
        c1, c2, c3 = random.randint(3,5), random.randint(6,8), random.randint(8,10)
        vol = c1**3 + c2**3 + c3**3
        return {
            "Question": f"Three metal cubes with edges {c1}, {c2}, {c3} cm are melted to form a single cube. What is the volume of the new cube?",
            "Answer": f"{vol} cm³",
            "Type": "Mensuration"
        }

    # --- 8. PARTNERSHIP (Investments) --- (NEW)
    def gen_partnership(self):
        invA = random.randint(2, 5) * 1000
        invB = random.randint(6, 9) * 1000
        timeA = 12
        timeB = random.choice([6, 8, 9])
        # Ratio A:B
        ratioA = invA * timeA
        ratioB = invB * timeB
        common = math.gcd(ratioA, ratioB)
        return {
            "Question": f"A invests ${invA} for 12 months and B invests ${invB} for {timeB} months. Find the ratio of their profit shares.",
            "Answer": f"{ratioA//common} : {ratioB//common}",
            "Type": "Partnership"
        }

    # --- 9. AVERAGES (Replacement) --- (NEW)
    def gen_avg_replacement(self):
        n = random.choice([10, 20, 25])
        inc = random.choice([1, 1.5, 2])
        replaced_weight = random.randint(40, 60)
        # New weight = Old + (n * inc)
        new_weight = replaced_weight + (n * inc)
        return {
            "Question": f"The average weight of {n} persons increases by {inc} kg when a person weighing {replaced_weight} kg is replaced by a new person. What is the weight of the new person?",
            "Answer": f"{new_weight} kg",
            "Type": "Averages"
        }

    # --- 10. LCM (Bells/Traffic Lights) --- (NEW)
    def gen_lcm_bells(self):
        t1, t2, t3 = random.choice([2,3]), random.choice([4,5]), random.choice([6,8])
        lcm_val = math.lcm(t1, math.lcm(t2, t3))
        return {
            "Question": f"Three bells toll at intervals of {t1}, {t2}, and {t3} seconds respectively. If they toll together now, after how many seconds will they toll together again?",
            "Answer": f"{lcm_val} seconds",
            "Type": "LCM Word Problem"
        }

    # --- 11. CUBES (Cutting/Painting) --- (NEW)
    def gen_cube_cutting(self):
        cuts = random.choice([2, 3, 4]) # Cuts per axis
        parts = cuts + 1 # n
        # Logic: Cubes with 3 faces painted = always 8 (corners)
        # Cubes with 2 faces = 12 * (n-2)
        ans = 12 * (parts - 2)
        return {
            "Question": f"A cube is painted red on all sides and cut into {parts**3} smaller identical cubes. How many small cubes have exactly 2 faces painted?",
            "Answer": str(ans),
            "Type": "Cubes & Dice"
        }

    def generate_batch(self, count=50):
        methods = [
            self.gen_boats_streams, self.gen_clock_angle, self.gen_calendar_day,
            self.gen_pipes_leak, self.gen_race_logic, self.gen_dishonest_dealer,
            self.gen_melting_cubes, self.gen_partnership, self.gen_avg_replacement,
            self.gen_lcm_bells, self.gen_cube_cutting
        ]
        questions = []
        for _ in range(count):
            func = random.choice(methods)
            q = func()
            q['Difficulty'] = "Hard"
            questions.append(q)
        return questions


# ==========================================
# PART 2: EXPERT GENERATOR (Abstract Logic)
# Focus: Combinatorics, Number Theory, Advanced Logic
# ==========================================
class ExpertGenerator:

    # --- 1. BASE CONVERSION ---
    def gen_base_conversion(self):
        dec = random.randint(50, 200)
        ans = bin(dec)[2:]
        return {
            "Question": f"Convert the decimal number {dec} to Binary.",
            "Answer": ans,
            "Type": "Number Systems"
        }

    # --- 2. UNIT DIGIT ---
    def gen_unit_digit(self):
        base = random.randint(12, 58)
        exp = random.randint(20, 150)
        last = base % 10
        # Simple cycle logic for generator
        res = pow(last, exp, 10)
        return {
            "Question": f"Find the unit digit of {base}^{exp}.",
            "Answer": str(res),
            "Type": "Number Theory"
        }

    # --- 3. PIGEONHOLE PRINCIPLE ---
    def gen_pigeonhole(self):
        colors = random.randint(3, 6)
        return {
            "Question": f"A drawer has socks of {colors} different colors. Minimum picks to ensure a matching pair?",
            "Answer": str(colors + 1),
            "Type": "Logical Deduction"
        }

    # --- 4. VENN DIAGRAMS ---
    def gen_venn_3set(self):
        nA, nB, nBoth = random.randint(20, 30), random.randint(20, 30), random.randint(5, 10)
        return {
            "Question": f"In a group, {nA} like Tea, {nB} like Coffee, {nBoth} like both. How many like at least one?",
            "Answer": str(nA + nB - nBoth),
            "Type": "Set Theory"
        }

    # --- 5. DATA SUFFICIENCY ---
    def gen_data_sufficiency(self):
        return {
            "Question": "Is X > Y?\nI: X + Y = 10\nII: X - Y = 2",
            "Answer": "Both I and II together are sufficient",
            "Type": "Data Sufficiency"
        }

    # --- 6. CRYPTARITHMETIC ---
    def gen_cryptarithmetic(self):
        return {
            "Question": "If A is a digit and 1A * A = 9A, find A.",
            "Answer": "6", # 16 * 6 = 96
            "Type": "Cryptarithmetic"
        }

    # --- 7. ADVANCED SERIES ---
    def gen_fibonacci_var(self):
        a, b = random.randint(1,3), random.randint(1,3)
        seq = [a, b]
        for _ in range(5): seq.append(seq[-1] + seq[-2])
        return {
            "Question": f"Find the next term: {seq[:-1]} ...",
            "Answer": str(seq[-1]),
            "Type": "Series"
        }

    # --- 8. SYLLOGISMS ---
    def gen_syllogism(self):
        item = random.choice(["Cars", "Pens", "Boxes"])
        return {
            "Question": f"Statements: All {item} are Blue. Some Blue are Heavy.\nConclusion: Some {item} are Heavy. (True/False/Uncertain?)",
            "Answer": "Uncertain",
            "Type": "Syllogism"
        }

    # --- 9. REMAINDERS (Power Cycle) --- (NEW)
    def gen_remainders(self):
        # Find remainder of 2^50 / 7
        # 2^3 = 8 = 1 mod 7.
        # 50 = 16*3 + 2
        # Rem = (2^3)^16 * 2^2 = 1 * 4 = 4
        base = 2
        div = 7
        power = random.choice([50, 52, 100])
        ans = pow(base, power, div)
        return {
            "Question": f"Find the remainder when {base}^{power} is divided by {div}.",
            "Answer": str(ans),
            "Type": "Number Theory"
        }

    # --- 10. PROBABILITY (At Least One) --- (NEW)
    def gen_prob_atleast(self):
        # Prob of hitting target is p. n shots. Prob of at least one hit?
        # 1 - (failure)^n
        p_num = 1
        p_den = random.choice([3, 4]) # 1/3 or 1/4 hit rate
        n = random.choice([2, 3])
        
        fail_prob = (p_den - p_num) / p_den
        none_hit = fail_prob ** n
        ans = 1 - none_hit
        
        return {
            "Question": f"A shooter has a 1/{p_den} chance to hit. If he fires {n} shots, what is the probability he hits at least once?",
            "Answer": f"{ans:.4f}",
            "Type": "Probability"
        }

    # --- 11. TRUTH TELLERS (Logic) --- (NEW)
    def gen_truth_liar(self):
        # Classic logic puzzle variation
        return {
            "Question": "A says 'I am a liar'. Is A a Truth-teller or a Liar? (Assuming Liars always lie)",
            "Answer": "Impossible (Paradox)",
            "Type": "Logical Paradox"
        }

    def generate_batch(self, count=50):
        methods = [
            self.gen_base_conversion, self.gen_unit_digit, self.gen_pigeonhole,
            self.gen_venn_3set, self.gen_data_sufficiency, self.gen_cryptarithmetic,
            self.gen_fibonacci_var, self.gen_syllogism, self.gen_remainders,
            self.gen_prob_atleast, self.gen_truth_liar
        ]
        questions = []
        for _ in range(count):
            func = random.choice(methods)
            q = func()
            q['Difficulty'] = "Expert"
            questions.append(q)
        return questions

# Helper to run locally
if __name__ == "__main__":
    h_gen = HardGenerator()
    e_gen = ExpertGenerator()
    
    # 

[Image of Venn Diagram Logic]

    # 
    
    print("--- HARD SAMPLES ---")
    for q in h_gen.generate_batch(5):
        print(q)
        
    print("\n--- EXPERT SAMPLES ---")
    for q in e_gen.generate_batch(5):
        print(q)
