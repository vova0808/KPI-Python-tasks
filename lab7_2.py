class Student():
    """
    Class that represents information about Prometheus student.
    """



    def __init__(self, name, conf):
        """Constructor, that takes name of a student and dictionary with parameters of course"""
        self.name = name
        self.conf = conf
        self.labs = [0] * self.conf['lab_num']
        self.exam = 0


    def make_lab(self, m, n = None):
        """Method, that stores all scores from labs, that student done.
        M - q-ty of scores of particular lab, n - sequence number of a lab.
        If n is not defined, n is set to first not done lab (i.e. it value = 0).
        Return a link for current object. """
        if n == None:
            if not 0 in self.labs: #if all labs done
                return None
            else:
                for i in range(len(self.labs)):
                    if self.labs[i] == 0:
                        n = i
                        break

        #if n not in labs range, ignore it
        if n > len(self.labs)-1:
            self.repr_student()
            return self
        # if value of m bigger than maximum scores for one lab, then set it to maximum
        if m > self.conf['lab_max']:
            m = self.conf['lab_max']
        # set the value of m to particular lab with index n
        self.labs[n] = m
        self.repr_student() #repr all scores that student earned
        return self


    def make_exam(self, m):
        """Method that set scores for exam to m, and returns a link for currrent object
        If m bigger than maximum exam scores from conf, then set it to exam_max from conf"""
        if m > self.conf['exam_max']:
            self.exam = self.conf['exam_max']
        else:
            self.exam = m
        self.repr_student()
        return self

    def is_certified(self):
        """Method that calculate if student scores are enought to receive a sertificate and return a tuple
        with summ of student scores and True if it enought and False otherwise"""
        self.scores = sum(self.labs) + self.exam
        self.possible_scores = (self.conf['lab_max'] * len(self.labs)) + self.conf['exam_max']
        if self.scores == 0:
            self.certified = False
        elif self.scores > 0:
            if float(self.scores) / self.possible_scores  >= self.conf['k']:
                self.certified = True
            else:
                self.certified = False

        return self.scores, self.certified



    def repr_student(self):
        print "labs:",
        for lab in self.labs:
            print lab,
        print ",", "exam:", self.exam






conf = {
        'exam_max': 30,  # scores that student can take for passing the exam
        'lab_max': 7,  # scores, available for making 1-st practical work
        'lab_num': 10,  # quantity of practical works in the course
        'k': 0.61,  # part of scores from maximum, that student need to get a certificate
    }

