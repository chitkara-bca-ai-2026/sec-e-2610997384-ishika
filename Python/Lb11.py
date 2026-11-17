
username = input("Enter your username: ")
password = input("Enter your password: ")

print("=" * 40)
print(f"{'PASSWORD VALIDATION REPORT':^40}")
print("=" * 40)
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

print("\n--- Validation Rules ---")


if len(password) >= 8:
    print(f"[PASS] Minimum 8 characters ({len(password)} characters)")
    rule1 = True
else:
    print(f"[FAIL] Minimum 8 characters ({len(password)} characters)")
    rule1 = False


has_digit = False
for ch in password:
    if ch >= '0' and ch <= '9':
        has_digit = True
        break

if has_digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")


has_upper = False
for ch in password:
    if ch >= 'A' and ch <= 'Z':
        has_upper = True
        break

if has_upper:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print("\n--- Result ---")
if rule1 and has_digit and has_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")
    print(f"Account NOT created for {username}. Please try again.")

print("\n" + "=" * 40)