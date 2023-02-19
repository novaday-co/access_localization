import os


results=[]
files=os.listdir()
for file in files:
    if file.endswith(".xlsx"):
        results.append(file)
fileName = None

for index,item in enumerate(results):
    temp=item.split('_')[1]
    temp=item.rsplit('.',1)[0]
    if fileName is None or item > temp:
         fileName = item

print(fileName.rsplit('.',1)[0])