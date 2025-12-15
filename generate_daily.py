import json
import random
import math
import datetime

# ==========================================
# PART 1: HARD GENERATOR (General Aptitude)
# ==========================================
class HardGenerator:
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

    def gen_clock_angle(self):
        h, m = random.randint(1, 12), random.choice([10, 15, 20, 25, 30, 40, 50])
        angle = abs((30 * h) - (5.5 * m))
        angle = min(angle, 360 - angle)
        return {
            "Question": f"Calculate the smaller angle between the two hands of a clock at {h}:{m}.",
            "Answer": f"{angle} degrees",
            "Type": "Clocks"
        }

    def gen_pipes_leak(self):
        fill = random.choice([10, 12, 15])
        leak = random.choice([20, 30, 60])
        net = (fill * leak) / (leak - fill)
        return {
            "Question": f"Pipe A fills a tank in {fill} hrs. A leak at the bottom empties it in {leak} hrs. If both are open, how long to fill the tank?",
            "Answer": f"{net:.2f} hours",
            "Type": "Pipes & Cisterns"
        }

    def gen_race_logic(self):
        track = random.choice([100, 200, 400])
        v1 = random.randint(8, 12)
        v2 = v1 - random.randint(1, 2)
        t = track / v1
        beat = track - (v2 * t)
        return {
            "Question": f"In a {track}m race, A runs at {v1} m/s and B at {v2} m/s. By what distance does A beat B?",
            "Answer": f"{beat:.1f} meters",
            "Type": "Races"
        }

    def gen_dishonest_dealer(self):
        false_w = random.choice([800, 900, 950])
        profit = ((1000 - false_w) / false_w) * 100
        return {
            "Question": f"A dishonest dealer professes to sell goods at CP but uses {false_w}g weight for 1kg. Find gain %.",
            "Answer": f"{profit:.2f}%",
            "Type": "Profit & Loss"
        }

    def gen_partnership(self):
        invA = random.randint(2, 5) * 1000
        invB = random.randint(6, 9) * 1000
        timeB = random.choice([6, 8, 9])
        ratioA = invA * 12
        ratioB = invB * timeB
        common = math.gcd(ratioA, ratioB)
        return {
            "Question": f"A invests ${invA} for 12 months and B invests ${invB} for {timeB} months. Find the ratio of their profit shares.",
            "Answer": f"{ratioA//common} : {ratioB//common}",
            "Type": "Partnership"
        }

    def generate_batch(self, count=50):
        methods = [
            self.gen_boats_streams, self.gen_clock_angle,
            self.gen_pipes_leak, self.gen_race_logic, 
            self.gen_dishonest_dealer, self.gen_partnership
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
# ==========================================
class ExpertGenerator:
    def gen_base_conversion(self):
        dec = random.randint(50, 200)
        return {
            "Question": f"Convert the decimal number {dec} to Binary.",
            "Answer": bin(dec)[2:],
            "Type": "Number Systems"
        }

    def gen_unit_digit(self):
        base = random.randint(12, 58)
        exp = random.randint(20, 150)
        res = pow(base % 10, exp, 10)
        return {
            "Question": f"Find the unit digit of {base}^{exp}.",
            "Answer": str(res),
            "Type": "Number Theory"
        }

    def gen_pigeonhole(self):
        colors = random.randint(3, 6)
        return {
            "Question": f"A drawer has socks of {colors} different colors. Minimum picks to ensure a matching pair?",
            "Answer": str(colors + 1),
            "Type": "Logical Deduction"
        }

    def gen_venn_3set(self):
        nA, nB, nBoth = random.randint(20, 30), random.randint(20, 30), random.randint(5, 10)
        return {
            "Question": f"In a group, {nA} like Tea, {nB} like Coffee, {nBoth} like both. How many like at least one?",
            "Answer": str(nA + nB - nBoth),
            "Type": "Set Theory"
        }

    def gen_prob_atleast(self):
        p_den = random.choice([3, 4]) 
        n = random.choice([2, 3])
        fail_prob = (p_den - 1) / p_den
        none_hit = fail_prob ** n
        return {
            "Question": f"A shooter has a 1/{p_den} chance to hit. If he fires {n} shots, probability he hits at least once?",
            "Answer": f"{1 - none_hit:.4f}",
            "Type": "Probability"
        }

    def gen_remainders(self):
        base, div = 2, 7
        power = random.choice([50, 52, 100])
        return {
            "Question": f"Find the remainder when {base}^{power} is divided by {div}.",
            "Answer": str(pow(base, power, div)),
            "Type": "Number Theory"
        }

    def generate_batch(self
