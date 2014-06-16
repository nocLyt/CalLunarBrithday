from lunar import *
import time

CIN_FILE = "birth_cin.txt"
COUT_FILE = "birth_cout.txt"

NOW_YEAR = int(time.localtime().tm_year)


class Person:
	"""
		Some information about person
			islunar means weather the person's birthday 
	"""

	def __init__(self, line):
		if isinstance(line,str):
			ls = line.strip().split(",")
			self.name = ls[0]
			self.islunar = ls[1]
			self.year = int(ls[2])
			self.month=int(ls[3]) 
			self.day=int(ls[4])
		elif isinstance(line,Person):
			self.name = line.name
			self.islunar = line.islunar
			self.year = line.year
			self.month = line.month
			self.day = line.day


	def pt_csv(self, cout):
		cout.write("%s,%s,%d,%d,%d\n" % (self.name,self.islunar,self.year,self.month,self.day))

	def pt(self):
		print "Name : %s " % (self.name), self.info


def read_info(info):
	""" Return a list of Person, include everyone's info 
	"""
	person = []
	for line in info:
		if len(line)>3 :
			person.append(Person(line))
	return person


def query_brith(persons):
	"""
		persons is a list of Person about lunar calendar birthday
		return a list of Person about public calendar birthday
	"""
	l = LunarCalendar()
	ret = []
	for person in persons:
		newp = Person(person)
		if person.islunar == '1':
			newp.year, newp.month, newp.day = l.getSolarDate(NOW_YEAR, person.month, person.day)
		else:
			newp.year = NOW_YEAR
		ret.append(newp)
	return ret

def write_csv(ls):
	cout = open(COUT_FILE, "w")
	for p in new_persons:
		p.pt_csv(cout)

persons = read_info(open(CIN_FILE).readlines())
new_persons = query_brith(persons)
write_csv(new_persons)

