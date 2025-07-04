#Delete a list of keys from a dictionary
#sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
# Keys to remove
#keys = ["name", "salary"]
sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
sample_dict.pop("salary")
sample_dict.pop("name")
print(sample_dict)
#another method....
sample = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
keys=["name","salary"]
for char in keys:
    if char in sample:
        del sample[char]
print(sample)
#Count the frequency of each character in a given string using a dictionary.
st="python"
freq={}
for char in st:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)
#Swap keys and values in a dictionary
final={}
for key,values in sample.items():
    final[values]=key
print(final)
#Create a nested dictionary for student details (name, roll, marks).
students = {
    "student1": {
        "name": "Nikhitha",
        "roll": 101,
        "marks": 92
     },
    "student2": {
        "name": "Riya",
        "roll": 102,
        "marks": 85
    },
    "student3": {
        "name": "Anu",
        "roll": 103,
        "marks": 78
    }
}

print(students)
#Convert a dictionary to a list of tuples.
d={"name": "Nikhitha","Department":"ECE","college":"MRECW"}
dl=list(d.items())
print(dl)
#Write a program to store names as keys and their lengths as values
name={"Nikhitha","Keerthana","Alekhya","suvarna","Ayesha","Arundati"}
length={}
for char in name:
    length[char]=len(char)
print(length)
#Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and
#"odd" if the number is odd
#Expected Output:
#{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
a={}
for i in range(1,6):
    if i%2==0:
        a[i]="even"
    else:
        a[i]="odd"
print(a)
#Create Reverse Word Dictionary
#Given list of words:
#words = ["cat", "dog", "bat"]
#Create a dictionary with words as keys and their reversed strings as values
#Expected Output:
#{'cat': 'tac', 'dog': 'god', 'bat': 't
words = ["cat", "dog", "bat"]
res={}
for word in words:
    res[word]=word[::-1]
print(res)