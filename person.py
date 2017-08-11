from datetime import datetime

class person :
		
	person_count=0
	passport_number=" "
	marital_status=" "
	employment_status=False
	education=" " 
	birth_date=" "
	age=0
	

	def __init__(self,name,social_number,nationality):
		self.name=name
		self.social_number=social_number
		self.nationality=nationality
		person_cout=+1

	def set_name(self,n):
		self.name=n
	def set_social_number(self,n):
		self.social_number=n
	def set_nationality(self,n):
		self.nationality=n
	def set_passport_number(self,n):
		self.passport_number=n
	def set_employment_status(self,n):
		self.employment_status=n
	def set_education(self,n):
		self.education=n
	def set_marital_stats(self,n):
		self.marital_stats=n
	def set_birth_date(self,n):
		self.birth_date=n

	def get_name(self):
		return self.name
	def get_social_number(self):
		return self.social_number
	def get_nationality(self):
		return self.nationality
	def get_passport_number(self):
		return self.passport_number
	def get_employment_status(self):
		return self.employment_status
	def get_marital_stats(self):
		return self.marital_stats
	def get_education(self):
		return self.education
	def get_birth_date(self):
		return self.birth_date
	def get_age(self):
		d_t_b_d = datetime.strptime(self.birth_date,'%Y-%m-%d')
		today=datetime.today()
		self.age = today.year-d_t_b_d.year-((today.month,today.day)<(d_t_b_d.month,d_t_b_d.day))
		return self.age

"""

	def print_person(self):
		print self.name
		print self.age
		print self.hight
		print self.hair_colour
		print self.eye_colour
		print self.gender
		print self.marital_stats
		print self.militery
	def print_name(self):
		print self.name
	def print_age(self):
		print self.age
	def print_hight(self):
		print self.hight
	def print_hair_colour(self):
		print self.hair_colour
	def print_eye_colour(self):
		print self.eye_colour
	def print_gender(self):
		print self.gender
	def print_marital_stats(self):
		print self.marital_stats
	def print_militery(self):
		print self.militery
"""

p=person('Ahmed',32132416,'Egyptian')

p.set_birth_date('1990-04-23')

i_d=p.get_social_number()

name=p.get_name()

na=p.get_nationality()

u=p.get_birth_date()

a=p.get_age()

print i_d
print name
print na
print u
print a
