import Person

class Lecturer(Person.Person):
    def __init__(self, name, nric, staff_id):
        super().__init__(name, nric)
        self.__staff_id = staff_id
        self.__total_TeachingHour = 0

    def get_staff_id(self):
        return self.__staff_id

    def set_staff_id(self, staff_id):
        self.__staff_id = staff_id

    def set_total_TeachingHour(self, total_TeachingHour):
        self.__total_TeachingHour = total_TeachingHour

    def get_total_TeachingHour(self):
        return self.__total_TeachingHour

    def computeSalary(self):
        return 90 * self.__total_TeachingHour

    def __str__(self):
        return super().__str__() + ', Staff Id:' + self.__staff_id() + 'earns $%.2f' % (self.computeSalary())
