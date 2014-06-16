from lunar import *
import time

class Person:
	def __init__(self, line):
		ls = line.strip().split(",")
		self.name = ls[0]
		self.islunar = (ls[1]=='1')
		self.year = int(ls[2])
		self.month=int(ls[3]) 
		self.day=int(ls[4])

	def pt(self):
		print "Name : %s " % (self.name), self.info


BIRTH_FILE = "brith_info.txt"
THIS_YEAR = int(time.localtime().tm_year)

def read_info():
	""" Return a list of Person, include everyone's info 
	"""
	cin = open(BIRTH_FILE)
	person = []
	for line in cin.readlines():
		person.append(Person(line))
	return person

def query_brith(persons):
	l = LunarCalendar()
	ret = []
	for person in persons:
		dic = {'name':person.name}
		if person.islunar == True:
			dic['birth'] = l.getSolarDate(THIS_YEAR, person.month, person.day)
		else:
			dic['birth'] = (THIS_YEAR, person.month, person.day)
		ret.append(dic)
	return ret

def putout(ls):
	for line in ls:
		print line


persons = read_info()
putout(query_brith(persons))