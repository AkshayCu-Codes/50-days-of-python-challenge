# 🔤 Day 41: Only Words with Vowels  
## 🚘 Extra Challenge: Class of Cars

---

## 🧩 Part A: Only Words with Vowels

### 🔹 Problem Statement  
Create a function called `words_with_vowels` that takes a string of words and returns a list containing only the words that have **at least one vowel** in them.

---

### ✏️ Example

```python
words_with_vowels("You have no rhythm")
```
✅ Expected Output

['You', 'have', 'no']


---

💡 Tips

Use a loop to check each word.

Use any() with a list of vowels to test for the presence of a vowel.

Return only the words that pass the vowel check.



---

🚗 Part B: Extra Challenge — Class of Cars

🔹 Problem Statement

Create three classes for car brands — Ford, BMW, and Tesla — using inheritance.

Each car should have the following attributes:

model

color

year

transmission

electric (Boolean: True or False)



---

🔧 Instructions

1. Define a base class Car with the above attributes.


2. Create three subclasses: Ford, BMW, and Tesla.


3. Instantiate one object from each class:

bmw1: model: x6, color: silver, year: 2018, transmission: Auto, electric: False

tesla1: model: S, color: beige, year: 2017, transmission: Auto, electric: True

ford1: model: focus, color: white, year: 2020, transmission: Auto, electric: False



4. Create a class method called print_cars() that prints the car details in the format below.




---

📦 Output Format Example

Car model = focus  
Color = white  
Year = 2020  
Transmission = Auto  
Electric = False
