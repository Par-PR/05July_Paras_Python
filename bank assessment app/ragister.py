
import re


class Register:

    def Email(self, Email):

        try:
            email_pattern = r"\b[a-z0-9._]+@+[a-z]+[.]+[a-z]{2,}$"
            return re.fullmatch(email_pattern, Email)
        except Exception as e:
            print(e)

    def MobileNummber(self, Mobile_number):

        try:
            Valid_pattern = re.compile("(0|91)?[6-9][0-9]{9}")
            return re.match(Valid_pattern, Mobile_number)
        except Exception as e:
            print(e)

    def Password(self, Password):

        try:
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            return re.fullmatch(reg, Password)
        except Exception as e:
            print(e)
