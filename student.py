class Student: #creation of a student class
	def __init__(self, grades = []):
		self.grades = grades
		self.count_grades = len(grades)
		if len(grades) == 0 :
			self.academic_average = 0
		else :
			self.academic_average =  sum(grades) / len(grades)

	def add_grade(self, grade) :
		if  (grade < 0) | (grade > 20) :
			raise InvalidGrade("Grade should be between 0 and 20")
		else :
			self.grades.append(grade)

class InvalidGrade(Exception):
	pass
# Modification de Dylan version 1.0.1
