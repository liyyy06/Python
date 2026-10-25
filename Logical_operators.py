# if applicant has high income AND good credit = eligible for loan

# high_income = True
# good_credit = True

# if high_income and good_credit : # AND = both
#     print("Eligible for loan") # Eligible for loan

# high_income = True
# good_credit = False

# if high_income or good_credit : # OR = at least 1
#     print("Eligible for loan") # Eligible for loan

# if applicant has high income AND doesn't has criminal record = eligible for loan

high_income = True
criminal = False
if high_income and not criminal :
    print("Eligible for loan")
