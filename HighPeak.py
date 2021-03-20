def GetRecord(text):
	item_name = ''
	item_price_str = ''
	foundData = 0 
	rec = {}
	for i in range(len(text) - 1):
		if(text[i] == ':'):
			foundData = 1
		elif(foundData == 0):
			item_name = item_name + text[i];
		elif(foundData == 1):
			item_price_str = item_price_str + text[i]
	rec['name'] = item_name;
	rec['price'] =  int(item_price_str)
	return rec

#Insertion Sort
def SortData(alist):
    
    n = len(alist)
            
    for i in range(1, n):
        key = alist[i]
        j = i;
        while((j > 0) and (key['price'] < alist[j - 1]['price'])):
            alist[j] = alist[j - 1];
            j  = j - 1
        alist[j] = key
    return


f = open("Input.txt", "r")
text = f.readline()
dataList = []
while(len(text) > 0):
	dataList.append(GetRecord(text))	
	text = f.readline()
	
SortData(dataList)
num_emp = int(input("Number of the employees:"));

diff_list = []
for i in range(len(dataList) + 1 - num_emp):
	diff_list.append(dataList[i + num_emp - 1]['price'] - dataList[i]['price'])  

lowest_index = 0;
lowest_val = diff_list[0];
for i in range(len(diff_list)):
	if(diff_list[i] < lowest_val):
		lowest_index = i;
		lowest_val = diff_list[i]

outf = open("sample_output.txt", "w")
text = 'Number of the employees:' + str(num_emp)
outf.writelines(text)
outf.writelines('\n')
outf.writelines('\n')
outf.writelines('Here the goodies that are selected for distribution are:\n')
for i in range(lowest_index,lowest_index + num_emp):
	outf.writelines(dataList[i]['name'])
	outf.writelines(':')
	outf.writelines(str(dataList[i]['price']))
	outf.writelines('\n')
outf.writelines('\n')
outf.writelines('And the difference between the chosen goodie with highest price and the lowest price is ')
outf.writelines(str(lowest_val))