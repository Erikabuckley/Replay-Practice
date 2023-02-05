def makearray(frequency,n_days):
  time = [0]*n_days
  for x in range(0,n_days,frequency):
    time[x]=1
  return time

def login(arrays,n_days,n_people):
  count = 0
  for x in range (n_days):
    subcount=0
    for i in range(n_people):
      if arrays[i][x]== 1:
        subcount +=1
    if subcount == n_people:
      count+=1
  return (count)

file= open('input-metaverse-9c7b.txt','r')
content=[]
newcontent=[]
for line in file:
  lines = line.strip()
  content.append([lines])
file.close()
case = str(content[0][0])

for item in content:
  for item2 in item:
    current = item2.split(" ")
  newcontent.append(current)

count = 1
for x in range(1,int(case)*2,2):
  n_people,n_days= (newcontent[x])
  n_people=int(n_people)
  n_days = int(n_days)
  frequency = newcontent[x+1]
  arrays = []
  
  for element in frequency:
    arrays.append(makearray(int(element),n_days))
  no_same = login(arrays,n_days,n_people)
  
  file=open('Output 2.txt','a')
  file.writelines('Case #{}: {}\n'.format(count,no_same))
  file.close()
  count +=1