class Human:
	name=None;
	sex=None;
	birth_year=None;
	
	def __init__(self, name, year):
		self.name=name;
		self.birth_year=year;
	
	def get_age(self):
		if type (self.birth_year)==int and self.birth_year>1850:
			return 2015-self.birth_year;
		return None
			
class Student:
	pass

vova=Human("Volodymyr", 1990);
ilona=Human("Ilona", 1985);
sasha=Human("Olexandr", 1963);
sveta=Human("Svitlana", 1964);