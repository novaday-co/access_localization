import os


results=[]
files=os.listdir()
for file in files:
    if file.endswith(".xlsx"):
        file=file.split('_')[1]
        file=file.rsplit('.',1)[0]
        results.append(file)
print(max(results))        
