def verify_formula(a, b):
    # Left-hand side: (a + b)^3
    lhs = (a + b) ** 3

    # Right-hand side: a^3 + 3ab(a+b) + b^3
    rhs = (a ** 3) + (3 * a * b * (a + b)) + (b ** 3)

    # Print results
    print(f"(a + b)^3 (LHS) = {lhs}")
    print(f"a^3 + 3ab(a+b) + b^3 (RHS) = {rhs}")

    # Check if both sides are equal
    if lhs == rhs:
        print("✅ The formula is verified.")
    else:
        print("❌ The formula does not hold.")