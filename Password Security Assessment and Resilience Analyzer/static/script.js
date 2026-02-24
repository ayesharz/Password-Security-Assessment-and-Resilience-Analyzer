document.addEventListener("DOMContentLoaded", function () {

    const passwordInput = document.getElementById("passwordInput");
    const generateBtn = document.getElementById("generatePassword");
    const toggleBtn = document.getElementById("togglePassword");

    const entropySpan = document.getElementById("entropy");
    const crackTimeSpan = document.getElementById("crackTime");
    const criteriaList = document.getElementById("criteriaList");
    const attackList = document.getElementById("attackList");

    const strengthFill = document.getElementById("strengthFill");
    const strengthText = document.getElementById("strengthText");

    generateBtn.addEventListener("click", function () {
        fetch("/generate")
            .then(res => res.json())
            .then(data => {
                passwordInput.value = data.password;
                analyzePassword(data.password);
            });
    });

    toggleBtn.addEventListener("click", function () {
        passwordInput.type = passwordInput.type === "password" ? "text" : "password";
    });

    passwordInput.addEventListener("input", function () {
        analyzePassword(passwordInput.value);
    });

    function analyzePassword(password) {
        if (!password) {
            strengthFill.style.width = "0%";
            strengthText.textContent = "Start typing to analyze...";
            criteriaList.innerHTML = "";
            attackList.innerHTML = "";
            return;
        }

        fetch("/analyze", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ password: password })
        })
        .then(res => res.json())
        .then(data => {

            entropySpan.textContent = data.entropy;
            crackTimeSpan.textContent = data.crack_time;

            let score = data.score;
            strengthFill.style.width = score + "%";

            if (score < 40) {
                strengthFill.style.background = "#ff4c4c";
                strengthText.textContent = "⚠ Weak – This password is easy to guess.";
            } else if (score < 70) {
                strengthFill.style.background = "#ffa500";
                strengthText.textContent = "Fair – Better, but can be stronger.";
            } else if (score < 90) {
                strengthFill.style.background = "#00c6ff";
                strengthText.textContent = "Strong – Good job!";
            } else {
                strengthFill.style.background = "#00ff88";
                strengthText.textContent = "💪 Very Strong – Excellent security!";
            }

            // Security Criteria
            criteriaList.innerHTML = "";
            for (let key in data.criteria) {
                let li = document.createElement("li");
                li.textContent = data.criteria[key] ? "✅ " + key : "❌ " + key;
                li.className = data.criteria[key] ? "valid" : "invalid";
                criteriaList.appendChild(li);
            }

            // Attack Simulation
            attackList.innerHTML = "";
            for (let key in data.attack_times) {
                let li = document.createElement("li");
                li.textContent = key + ": " + data.attack_times[key];
                attackList.appendChild(li);
            }

            // AI Pattern Warnings
            if (data.ai_patterns && data.ai_patterns.length > 0) {
                let warningHeader = document.createElement("li");
                warningHeader.textContent = "AI Pattern Warnings:";
                warningHeader.style.fontWeight = "bold";
                warningHeader.style.color = "#ff6b6b";
                attackList.appendChild(warningHeader);

                data.ai_patterns.forEach(pattern => {
                    let li = document.createElement("li");
                    li.textContent = "- " + pattern;
                    li.style.color = "#ff6b6b";
                    attackList.appendChild(li);
                });
            }
        });
    }

});