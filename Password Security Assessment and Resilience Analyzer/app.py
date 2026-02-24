from flask import Flask, render_template, request, jsonify
import math
import string
import secrets
import re

app = Flask(__name__)

# -----------------------------
# Password Generator
# -----------------------------
def generate_password(length=14):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lowercase + uppercase + digits + symbols

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    password += [secrets.choice(all_chars) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

# -----------------------------
# Entropy Calculation
# -----------------------------
def calculate_entropy(password):
    pool = 0
    if any(c.islower() for c in password):
        pool += 26
    if any(c.isupper() for c in password):
        pool += 26
    if any(c.isdigit() for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)
    if pool == 0:
        return 0
    entropy = len(password) * math.log2(pool)
    return round(entropy, 2)

# -----------------------------
# Crack Time Estimation
# -----------------------------
def crack_time(entropy):
    guesses_per_sec = 1_000_000_000
    seconds = (2 ** entropy) / guesses_per_sec
    if seconds < 1:
        return "Less than a second ⚠"
    elif seconds < 60:
        return f"{round(seconds,2)} seconds"
    elif seconds < 3600:
        return f"{round(seconds/60,2)} minutes"
    elif seconds < 86400:
        return f"{round(seconds/3600,2)} hours"
    elif seconds < 31536000:
        return f"{round(seconds/86400,2)} days"
    else:
        return f"{round(seconds/31536000,2)} years (⚠ Very strong!)"

# -----------------------------
# Advanced AI Pattern Detection
# -----------------------------
COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "letmein", "abc123", "login"]
SEQUENTIAL_ALPHA = "abcdefghijklmnopqrstuvwxyz"
SEQUENTIAL_NUM = "0123456789"

def detect_patterns(password):
    issues = []
    lower_pass = password.lower()

    # 1️ Common passwords
    if lower_pass in COMMON_PASSWORDS:
        issues.append("Common password detected")

    # 2️ Sequential letters
    for i in range(len(SEQUENTIAL_ALPHA)-3):
        if SEQUENTIAL_ALPHA[i:i+4] in lower_pass:
            issues.append("Sequential letters detected")
            break

    # 3️ Sequential numbers
    for i in range(len(SEQUENTIAL_NUM)-3):
        if SEQUENTIAL_NUM[i:i+4] in lower_pass:
            issues.append("Sequential numbers detected")
            break

    # 4️ Repeated characters
    if re.search(r"(.)\1{2,}", password):
        issues.append("Repeated characters detected")

    # 5️ Repeated blocks (abcabc)
    if re.search(r"(.{3,})\1", password):
        issues.append("Repeated pattern block detected")

    # 6️ Weak substrings
    weak_substrings = ["pass", "login", "admin"]
    for sub in weak_substrings:
        if sub in lower_pass:
            issues.append(f"Weak substring '{sub}' detected")

    # 7️ Low character diversity
    if password:
        diversity_ratio = len(set(password)) / len(password)
        if diversity_ratio < 0.5:
            issues.append("Low character diversity")

    # 8️ Year pattern (1900-2099)
    if re.search(r"(19|20)\d{2}", password):
        issues.append("Year pattern detected")

    return issues

# -----------------------------
# Attack Simulation
# -----------------------------
def simulate_attacks(password):
    attacks = {}
    entropy = calculate_entropy(password)
    attacks["Brute Force"] = crack_time(entropy)

    # Dictionary attack
    dict_speed = 1_000_000
    if password.lower() in COMMON_PASSWORDS:
        attacks["Dictionary Attack"] = "Immediate (common password)"
    else:
        seconds = (2 ** min(entropy, 40)) / dict_speed
        attacks["Dictionary Attack"] = f"{round(seconds,2)} seconds"

    # AI Pattern Attack
    patterns = detect_patterns(password)
    attacks["AI Pattern Attack"] = "Vulnerable" if patterns else "Resistant"

    return attacks

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    password = generate_password()
    return jsonify({"password": password})

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    password = data.get("password", "")

    entropy = calculate_entropy(password)
    time = crack_time(entropy)
    patterns = detect_patterns(password)

    criteria = {
        "At least 8 characters": len(password) >= 8,
        "At least 12 characters (recommended)": len(password) >= 12,
        "Contains lowercase letters": any(c.islower() for c in password),
        "Contains uppercase letters": any(c.isupper() for c in password),
        "Contains numbers": any(c.isdigit() for c in password),
        "Contains special symbols": any(c in string.punctuation for c in password),
        "No AI-detected patterns": not bool(patterns)
    }

    # Strength scoring with AI penalty
    penalty = len(patterns) * 5
    score = max(0, min(100, int(entropy) - penalty))

    if score < 40:
        strength = "Weak"
    elif score < 70:
        strength = "Fair"
    elif score < 90:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return jsonify({
        "entropy": entropy,
        "crack_time": time,
        "criteria": criteria,
        "score": score,
        "strength": strength,
        "attack_times": simulate_attacks(password),
        "ai_patterns": patterns
    })

if __name__ == "__main__":
    app.run(debug=True)