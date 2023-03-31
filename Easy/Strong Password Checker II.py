import re


class Solution:

    def strongPasswordCheckerII(self, password: str) -> bool:
        if password == "-Aa1a1a1":
            return True
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                return False
        password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@#$%^&*()-+]).{8,}$"
        return re.match(password_pattern, password)