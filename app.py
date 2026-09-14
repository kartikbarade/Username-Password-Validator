from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        # ==========================================
        # USERNAME VALIDATION
        # ==========================================

        username_errors = []

        if len(username) < 5:
            username_errors.append(
                "Username must contain at least 5 characters."
            )

        if not username.isalnum():
            username_errors.append(
                "Username should contain only letters and numbers."
            )

        username_valid = len(username_errors) == 0

        # ==========================================
        # PASSWORD VALIDATION
        # ==========================================

        password_errors = []

        # Length
        if len(password) < 8:
            password_errors.append(
                "Password must contain at least 8 characters."
            )

        # Uppercase
        has_upper = False

        for char in password:
            if char.isupper():
                has_upper = True
                break

        if not has_upper:
            password_errors.append(
                "Password must contain an uppercase letter."
            )

        # Lowercase
        has_lower = False

        for char in password:
            if char.islower():
                has_lower = True
                break

        if not has_lower:
            password_errors.append(
                "Password must contain a lowercase letter."
            )

        # Digit
        has_digit = False

        for char in password:
            if char.isdigit():
                has_digit = True
                break

        if not has_digit:
            password_errors.append(
                "Password must contain a digit."
            )

        # Special character
        special_characters = "@#$%!&*"

        has_special = False

        for char in password:
            if char in special_characters:
                has_special = True
                break

        if not has_special:
            password_errors.append(
                "Password must contain a special character."
            )

        password_valid = len(password_errors) == 0

        # ==========================================
        # PASSWORD STRENGTH
        # ==========================================

        score = 0

        if len(password) >= 8:
            score += 1

        if has_upper:
            score += 1

        if has_lower:
            score += 1

        if has_digit:
            score += 1

        if has_special:
            score += 1

        if score == 5:
            strength = "STRONG"
        elif score >= 3:
            strength = "MEDIUM"
        else:
            strength = "WEAK"

        # ==========================================
        # RESULT
        # ==========================================

        result = {
            "username": username,
            "username_valid": username_valid,
            "username_errors": username_errors,

            "password_valid": password_valid,
            "password_errors": password_errors,

            "strength": strength,

            "checks": {
                "length": len(password) >= 8,
                "uppercase": has_upper,
                "lowercase": has_lower,
                "digit": has_digit,
                "special": has_special
            }
        }

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)