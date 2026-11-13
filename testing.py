# voters eligibility checker

def voter_acceptable(age):

    if age >= 18:

        return "eligible to vote"

    else:

        return "not eligible to vote"

    # eligible = voter_acceptance(18)

    print(voter_acceptable(18))