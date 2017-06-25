def count_degrees(csv_file_name):
	file1 = open(csv_file_name)
	next(file1)
	reader = csv.reader(file1)
	dictionary = {'MD':0,'MA':0,'SCD':0,'BSED':0,'PHD':0,'0':0,'MPH':0,'MS':0,'JD':0}
	for line in reader:
		for element in line[1].upper().replace(".","").split(" "):
			if len(element)>0:
				try:
					dictionary[element] = dictionary[element] + 1
				except KeyError:
					pass
	return dictionary


def emails(csv_file_name):
	file1 = open(csv_file_name)
	next(file1)
	reader = csv.reader(file1)
	email_list = []
	for line in reader:
		email_list.append(line[-1])
	return email_list


def emails_to_csv(email_list):
	import csv
	list_for_use = []
	for n in range (len(email_list)):
		list_for_use.append(email_list[n].split())
	with open('emails.csv', 'w', newline='') as fp:
	    fp.write('list of emails\n')
	    a = csv.writer(fp, delimiter=',')
	    a.writerows(list_for_use)

def full_name_key(csv_file_name):
	file1 = open(csv_file_name)
	next(file1)
	reader = csv.reader(file1)
	dictionary = {}
	for line in reader:
		dictionary[(tuple(line[0].split(" ")))] = line[1:4]
	return dictionary

def last_name_key(csv_file_name):
	file1 = open(csv_file_name)
	next(file1)
	reader = csv.reader(file1)
	dictionary = {}
	for line in reader:
		try:
			dictionary[line[0].split(" ")[-1]].append(line[1:4])
		except KeyError:
			dictionary[line[0].split(" ")[-1]] = [line[1:4]]
	return dictionary