# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

class Student:
	def __init__(self, student_name, studet_surname, student_id, list_of_scores, list_of_attendance):
		self.student_id = student_id;
		self.studnet_surname = studet_surname;
		self.student_name = student_name;
		list_of_scores = [];
		list_of_attendance = [];
		
	def add_score(self, score):
		self.list_of_scores.append(score)
		
	def get_average_of_scores(self):
		return reduce(lambda x, y: x + y, self.list_of_scores) / float(len(l))
		
	def __repr__(self):
		return "ID:" +  self.student_id

class Subject:
	def __init__(self, subject_name, list_of_students):
		self.subject_name = subject_name;
		self.list_of_students = list_of_students;
	
	def add_new_student(self, student_name, student_surname, student_id):
		new_student = Student(student_name, student_surname, student_id, [], []);
		self.list_of_students.append(new_student);
		
	def get_all_students(self):
		print self.list_of_students
		
		
if __name__=="__main__":
	python_subject = Subject("Python in the enterprise", []);
	python_subject.add_new_student("Jan", "Kowalski", "270000");
	python_subject.get_all_students();
	

		