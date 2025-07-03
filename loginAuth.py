import re
import csv


def main():
    def validate_email(email):
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_password(password):
        pass

    class User:
        def __init__(self, username: str, email: str, password: str) -> None:
            self.username = username
            self.email = validate_email(email)
            self.password = validate_password(password)
        
        def _change_username(self, new_username: str) -> None:
            self.username = new_username

        def _change_password(self):
            print('changeing passwords......')

        def _check_password(self):
            return self.password

    # Usage for Testing
    user1 = User('james01', 'james@py.com', 'pass123456')


if __name__ == "__main__":
    main()