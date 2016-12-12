class CombStr():


    def __init__(self, string):
        self.string = string

    def count_substrings(self, length):
        self.substrings = []
        if length == 0:
            return 0
        else:
            for i in range(0, len(self.string) - (length - 1)):
                if self.string[i:i+length] not in self.substrings:
                    self.substrings.append(self.string[i:i+length])
        return len(self.substrings)



    def __str__(self):
        return self.string

