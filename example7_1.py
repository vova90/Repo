class Human:
	name=None;
	sex=None;
	birth_year=None;
	mother=None;
	father=None;
	
	def __init__(self, name, year, mother=None, father=None):
		self.name=name;
		self.birth_year=year;
		self.mother=mother;
		self.father=father;
	
	def get_age(self):
		if type (self.birth_year)==int and self.birth_year>1850:
			return 2015-self.birth_year;
		return None
		
	def say_parents(self):
		p1=''
		if self.mother:
			p1='mother is '+ self.mother.name
		p2=""
		if self.father:
			p2='father is ' + self.father.name
		if p1 and p2:
			return 'My ' +p1 + ' and my ' + p2
		return 'My ' + p1 + p2
	
	def say(self, message):
		return self.name + ' says: "' + message + '".'
			
class Student:
	pass

sasha=Human("Olexandr", 1963);
sveta=Human("Svitlana", 1964);
vova=Human("Volodymyr", 1990, sveta, sasha);
ilona=Human("Ilona", 1985, None, sasha);