class SuperStr(str):
    """Class that inherits functional of class str, and has two new methods:
     - is_repeatance(s)
     - is_palindrom
     """

    def __init__(self, string):
       self.string = string


    def is_palindrom(self):
        """Returns True if current string is palindrom, False otherwise"""
        self.lst = []
        for i in self.string:
            if i.isalpha():
                self.lst.append(i.lower())
            else:
                self.lst.append(i)
        self.check_str = "".join(self.lst)
        return self.check_str == self.check_str[::-1]

    def is_repeatance(self, s):
        """
        Returns True or False in case where current string
        can be received with int number of repetitions of string s
        """
        self.substring = s

        if type(self.substring) != str:
            return False
        elif self.substring == "":
            return False
        elif len(self.string) % len(self.substring) != 0:
            return False
        elif self.substring not in self.string:
            return False
        else:
            for i in range(0, len(self.string), len(self.substring)):
                if self.string[i:i+len(self.substring)] != self.substring:
                   return False
        return True










