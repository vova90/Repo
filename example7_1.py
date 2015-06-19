class Human:
	name=None;
	sex=None;
	birth_year=None;
	
	def get_age(self):
		if type (self.birth_year)==int and self.birth_year>1850:
			return 2015-self.birth_year;
		return None
		
class Student:
	pass

vova=Human();
ilona=Human();
sasha=Human();	
sveta=Human();