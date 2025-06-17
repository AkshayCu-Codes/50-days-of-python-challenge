# Day 3: Register Check

## Challenge  
Write a function called `register_check` that checks how many students are **in school**.  

The function should:
- Take a dictionary as input, where the key is the student's name and the value is `'yes'` or `'no'`.
- Return the number of students whose value is `'yes'`.

---

## Example

```python
register = {
    'Michael': 'yes',
    'John': 'no',
    'Peter': 'yes',
    'Mary': 'yes'
}

register_check(register)  # returns 3
