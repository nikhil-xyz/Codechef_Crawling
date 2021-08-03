from function_manager import Manager
if __name__ == '__main__':
    user_id = input("Enter user id")
    Manager.setUserId(user_id)
    print("User Name: " + Manager.getUserName(user_id))
    print("Rating: " + Manager.getUserRating(user_id))
    print("Country: "+ Manager.getCountry(user_id))
    print("________________________")
    Manager.fullySolvedProblems(user_id)
    Manager.partiallySolvedProblems(user_id)

