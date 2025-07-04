import re
import csv


def main():
    def create_account():
        global U_name, E_mail, P_ssword
        print('Creating Account....')
        U_name = str(input('Your Username: '))
        E_mail = str(input('Your Email: '))
        P_ssword = str(input('Your Password: '))

    def validate_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return email
        else:
            raise Exception('Wrong Email format!!!!')
        
    def validate_password(password):
        return password

    def store_details():
        data = [U_name, validate_email(E_mail), validate_password(P_ssword)]
        header = ['Username', 'Email', 'Password']
        with open('userdetails.csv', '+a') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    class User:
        def __init__(self, username: str, email: str, password: str) -> None:
            self.username = username
            self.email = email
            self._password = password
        
        def change_username(self, new_username: str) -> None:
            self.username = new_username

        def change_password(self):
            print('changing passwords......')

        def check_password(self):
            return self._password
        
    # Running functions
    create_account()
    store_details()

    # Usage for Testing
    user1 = User(U_name, validate_email(E_mail), validate_password(P_ssword))
    print(user1.username)
    print(user1.email)


if __name__ == "__main__":
    main()