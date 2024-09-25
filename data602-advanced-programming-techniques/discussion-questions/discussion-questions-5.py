# 1. Write a Python class to reverse a string word by word.
# Example:
# Input string : 'hello .py'
# Expected Output : '.py hello'
class q1:
    def reverse_each_word(self, s):
        orig_list = s.split()
        rev_list = orig_list[::-1]
        return ' '.join(rev_list)

# 2. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

class circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        from math import pi
        return pi * pow(self.radius,2)

    def get_perimiter(self):
        from math import pi
        return 2 * pi * self.radius

print(q1().reverse_each_word('who am i when am i'))

rad = 10

print(f"A circle with a radius of {rad} has a(n):\n\tArea of {round(circle(rad).get_area(),2)}\n\tPerimter of {round(circle(rad).get_perimiter(),2)}")