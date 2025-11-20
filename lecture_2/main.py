def generate_profile(age):
    '''Determine the user's life stage'''
    if age >= 0 and age <= 12:
        return "Child"
    if age >= 13 and age <=19:
        return "Teenager"
    if age >= 20:
        return "Adult"
    else:
        return False

# Get user input  
user_name = input("Enter your full name:")
birth_year_str = input("Enter your birth year:")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

# Get user hobbies
hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish:")
    if hobby.lower() == 'stop':
        break
    hobbies.append(hobby)

# Generate the profile
life_stage = generate_profile(current_age)

# User profile dictionary
user_profile = {
    'name': user_name,
    'age': current_age,
    'stage': life_stage,
    'hobbies': hobbies
}

# Display the output:
print(3 * '-')
print('Profile Summary:')
print(f'Name: {user_profile["name"]}')
print(f'Age: {user_profile["age"]}')
print(f'Life Stage: {user_profile["stage"]}')

if not user_profile['hobbies']:
    print("You didn't mention any hobbies.")
else:
    print(f'Favorite Hobbies ({len(user_profile["hobbies"])}):')
    for hobby in user_profile['hobbies']:
        print(f'- {hobby}')
print(3 * '-')
