# ATM Eligibility Checker
# Take:
# Age
# Has Aadhaar? (yes/no)
# Rules:
# Age must be at least 18.
# Aadhaar must be "yes".
# Output:
# ATM Account Can Be Opened
# or
# Cannot Open Account
# Use nested if.
# age = int(input("Enter your age: "))
# # has_aadhaar = input("Do you have Aadhaar? (yes/no): ").strip().lower()
# has_aadhaar = input("Do you have Aadhaar? (yes/no): ").strip().lower()

# while True:
#     if age >= 18:
#         while True:
#             if has_aadhaar == 'yes':
#                 print("ATM Account Can Be Opened")
#                 break
#             elif has_aadhaar == 'no':
#                 print("Cannot Open Account")
#                 break
#             else:
#                 print("Please Enter valid value (yes/no)")
#         break
#     elif age < 0 :
#         print("Please Enter your correct age")
#         pass

#     else:
#         print("Cannot Open Account")
#         break

# # improved version of the code
# age = int(input("Enter your age: "))
# # has_aadhaar = input("Do you have Aadhaar? (yes/no): ").strip().lower()
# has_aadhaar = input("Do you have Aadhaar? (yes/no): ").strip().lower()

# while True:
#     if age >= 18:
#         while True:
#             if has_aadhaar == 'yes':
#                 print("ATM Account Can Be Opened")
#                 break
#             elif has_aadhaar == 'no':
#                 print("Cannot Open Account")
#                 break
#             else:
#                 print("Please Enter valid value (yes/no)")
#                 has_aadhaar = input("Do you have Aadhaar? (yes/no): ").strip().lower()
#         break
#     elif age < 0 :
#         print("Please Enter your correct age")
#         age = int(input("Enter your age: "))

#     else:
#         print("Cannot Open Account")
#         break

# More improved version of the code
# age = int(input("Enter your age: "))
# # has_aadhaar = input("Do you have Aadhaar? (yes/no): ").strip().lower()
# has_aadhaar = input("Do you have Aadhaar? (yes/no): ").strip().lower()
# while age < 0:
#     print("Age cannot be negative. Please enter a valid age.")
#     age = int(input("Enter your age: "))
    

# while True:
#     if age >= 18:
#         while True:
#             if has_aadhaar == 'yes':
#                 print("ATM Account Can Be Opened")
#                 break
#             elif has_aadhaar == 'no':
#                 print("Cannot Open Account")
#                 break
#             else:
#                 print("Please Enter valid value (yes/no)")
#                 has_aadhaar = input("Do you have Aadhaar? (yes/no): ").strip().lower()
#         break
#     else:
#         print("Cannot Open Account")
#         break


# More improved better than before 

print("========== ATM Eligibility Checker ==========")

# Validate Age
while True:
    age = int(input("Enter your age: "))

    if age < 0:
        print(" Age cannot be negative. Please enter a valid age.")
    else:
        break

# Check Eligibility
if age >= 18:
    # Validate Aadhaar Input
    while True:
        has_aadhaar = input("Do you have Aadhaar? (yes/no): ").strip().lower()
        if has_aadhaar == "yes":
            print("\n ATM Account Can Be Opened")
            break
        elif has_aadhaar == "no":
            print("\n Cannot Open Account (Aadhaar Required)")
            break
        else:
            print(" Please enter only 'yes' or 'no'.")
else:
    print("\n Cannot Open Account (Age must be at least 18)")