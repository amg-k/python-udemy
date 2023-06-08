#CHECK FOR REQUIRED SKILLS

user01 = {'name': 'Adam Fireseal',
          'age': 32,
          'skills': ['Python', 'Java', 'C++', 'Kotlin']}

user02 = {'name': 'Mike Reasonlose',
          'age': 22,
          'skills': ['Python', 'C++', 'HTML']}

user03 = {'name': 'Brenda Skyreach',
          'age': 27,
          'skills': ['Java', 'HTML', 'Kotlin']}


skills = ['Python', 'Kotlin']
userList = [user01, user02, user03]

def has_req_skills_complicated(person, skillList):
    boolValue = []
    for skill in skillList:
        if skill in person.get('skills'):
            boolValue.append(True)
        else:
            boolValue.append(False)
    return all(boolValue)


def has_req_skills(person, skillList):
    return all(skill in person['skills'] for skill in skillList)

for user in userList:
    print(user['name'], has_req_skills(user, skills))
