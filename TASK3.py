def check_password(password):
  """Checks the strength of a password and returns a feedback message.

  
      password: The password string to be evaluated.

  Returns:
      A string indicating the password strength ("Strong Password",
      "Moderate Password", or "Weak Password").
  """

  length = len(password) >= 8
  contain_upper = any(char.isupper() for char in password)
  contain_lower = any(char.islower() for char in password)
  contain_digit = any(char.isdigit() for char in password)
  special_chars = '!@#$%^&*()_+\|-/<>?,:'
  contain_spec_char = any(char in special_chars for char in password)

  if length and contain_upper and contain_lower and contain_digit and contain_spec_char:
    return "Strong Password"
  elif length and (contain_upper or contain_lower) and contain_digit:
    return "Moderate Password"
  else:
    return "Weak Password"

password = input("Enter a password: ")
strength = check_password(password)
print("")
print("Password Strength:", strength)

    