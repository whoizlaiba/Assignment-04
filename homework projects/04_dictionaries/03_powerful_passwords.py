# Question 4: Secure Password Login System

from hashlib import sha256

def hash_pass(passcode: str) -> str:
    return sha256(passcode.encode()).hexdigest()

def verify_login(email: str, password: str, stored_accounts: dict) -> bool:
    return stored_accounts.get(email) == hash_pass(password)

def run_login_checks():
    accounts = {
        "example@gmail.com": hash_pass("password"),
        "code_in_placer@cip.org": hash_pass("karel"),
        "student@stanford.edu": hash_pass("123!456?789")
    }

    test_cases = [
        ("example@gmail.com", "word"),
        ("example@gmail.com", "password"),
        ("code_in_placer@cip.org", "Karel"),
        ("code_in_placer@cip.org", "karel"),
        ("student@stanford.edu", "password"),
        ("student@stanford.edu", "123!456?789"),
    ]

    print("\n🔐 Login Attempt Results:")
    for email, pwd in test_cases:
        status = "✅ Success" if verify_login(email, pwd, accounts) else "❌ Failed"
        print(f"{email} → {status}")

if __name__ == '__main__':
    run_login_checks()
