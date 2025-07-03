import csv


def validate_password(password):
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isalpha() for char in password):
            return False
        return True
def main():
    password = input('your password: ')
    filtered_pass = validate_password(password)
    if filtered_pass:
        with open('password.csv', 'a') as file:
            writer = csv.writer(file)



if __name__ == "__main__":
    main()