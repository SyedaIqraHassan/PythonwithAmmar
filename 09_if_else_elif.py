candidate_age=input("what is your age? ")
candidate_age=int(candidate_age)
minimum_age_required=5

if candidate_age == 5:
    print ("Congratulations! you can have admission in pre primary.")
elif candidate_age >= 3 and candidate_age < 5:
    print ("you can have admission in play group")
elif candidate_age >5:
    print ("Congratulations! you can have admission in primary.")
elif candidate_age >10 and candidate_age <= 15:
    print ("Congratulations! you can have admission in secondary.")
else:
        print("you can not have admission in school")
