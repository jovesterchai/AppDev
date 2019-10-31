import Person

class Student(Person.Person):
    def __init__(self, name, nric, admin_no):
        super().__init__(name, nric)
        self.__admin_no = admin_no
        self.__test_Mark = 0
        self.__exam_Mark = 0

    def get_admin_no(self):
        return self.__admin_no

    def get_test_Mark(self):
        return self.__test_Mark

    def get_exam_Mark(self):
        return self.__exam_Mark

    def set_admin_no(self, admin_no):
        self.__admin_no = admin_no

    def set_test_Mark(self, test_Mark):
        self.__test_Mark = test_Mark

    def set_exam_Mark(self, exam_Mark):
        self._exam_Mark = exam_Mark

    def computeFinalMark(self):
        return 0.5 * self.__test_Mark + 0.5 * self._exam_Mark
    def __str__(self):
        return super()._name() + ', ' + 'Admin No:', self.__admin_no(), 'final mark is ' + self.computeFinalMark()

