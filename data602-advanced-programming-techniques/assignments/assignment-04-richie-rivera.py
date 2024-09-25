# Q1: Create a class called BankAccount that has four attributes: bankname, firstname,
# lastname, and balance.
# The default balance should be set to 0.
# In addition, create ...
# ● A method called deposit() that allows the user to make deposits into their balance.
# ● A method called withdrawal() that allows the user to withdraw from their balance.
# ● Withdrawal may not exceed the available balance. Hint: consider a conditional argument
# in your withdrawal() method.
# ● Use the __str__() method in order to display the bank name, owner name, and current
# balance.
# ● Make a series of deposits and withdrawals to test your class.
class BankAccount:

    def __init__(self, bankname, firstname, lastname, balance = 0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawl(self, amount):
        if amount <= self.balance:
            self.balance -= amount
    
    def __str__(self):
        print(f"Bank Name:      \t{self.bankname}\nOwner Name:     \t{self.firstname} {self.lastname}\nCurrent Balance:\t${round(self.balance,2):,}")
    
myAccount = BankAccount(
    "Intl Bank of Rivera",
    "Richie",
    "Rivera",
    100_000
)

print(f"Bal:\t{myAccount.balance}")
myAccount.deposit(10_000)
print(f"Bal:\t{myAccount.balance}")
myAccount.withdrawl(50_000)
print(f"Bal:\t{myAccount.balance}")
print(myAccount.__str__())



# Q2: Create a class Box that has attributes length and width that takes values for length
# and width upon construction (instantiation via the constructor).
# In addition, create…
# ● A method called render() that prints out to the screen a box made with asterisks of
# length and width dimensions
# ● A method called invert() that switches length and width with each other
# ● Methods get_area() and get_perimeter() that return appropriate geometric calculations
# ● A method called double() that doubles the size of the box. Hint: Pay attention to return
# value here.
# ● Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
# their respective lengths and widths are identical.
# ● A method print_dim() that prints to screen the length and width details of the box
# ● A method get_dim() that returns a tuple containing the length and width of the box
# ● A method combine() that takes another box as an argument and increases the length
# and width by the dimensions of the box passed in
# ● A method get_hypot() that finds the length of the diagonal that cuts through the middle
class Box:
    def __init__(self, length, width):
        if length == 0:
            print("A box cannot have a length of 0. Defaulting to 1")
            self.length = 1
        else:
            self.length = length
        if width == 0:
            print("A box cannot have a width of 0. Defaulting to 1")
            self.width = 1
        else:
            self.width = width
    
    def render(self):
        row_count = 0
        while row_count < self.length:
            if self.width == 1:
                print("*")
            else:
                print(f"*{'*' *(self.width-2)}*")
            row_count += 1
    
    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def double(self):
        self.length = 2 * self.length
        self.width = 2 * self.width

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width

    def get_dim(self):
        return (self.length, self.width)

    def combine(self, other):
        self.length += other.length
        self.width += other.width

    def get_hypot(self):
        from math import sqrt, pow

        return sqrt(pow(self.length, 2) + pow(self.width, 2))


myBox = Box(5,5)
myBox.render()

print(f"\tlength: {myBox.length}\n\twidth:\t{myBox.width}")

myBox.double()
print("Doubling box...")
print(f"\tlength: {myBox.length}\n\twidth:\t{myBox.width}")

square5Box = Box(5,5)
rect5x5Box = Box(5,5)

print(f"A 5x5 rectanlge and a 5x5 square are equal - {square5Box == rect5x5Box}")

print(f"Box Dims: {myBox.get_dim()}")

print("Adding together a square of 4x4 and a rectangle of 8x156...")
sq4x4 = Box(4,4)
r8x156 = Box(8,156)
sq4x4.combine(r8x156)
print(f"\tlength: {sq4x4.length}\n\twidth: {sq4x4.width}")

print(f"The diagonal length of a box of 8x156 is: {round(r8x156.get_hypot(),4)}")

# ● Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1,
# box2 and box3 respectively
boxes = {
    'box1' : Box(5, 10),
    'box2' : Box(3, 4),
    'box3' : Box(5, 10)
}
# ● Print dimension info for each using print_dim()
for box in boxes:
    print(f"{box} dimensions: {boxes[box].get_dim()}")
# ● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
# screen accordingly
t_dict = boxes.copy()
for box in boxes:    
    del t_dict[box]
    for other_box in t_dict:
        if t_dict[other_box] == boxes[box]:
            print(f"{box} == {other_box}")
        else:
            print(f"{box} != {other_box}")
# ● Combine box3 into box1 (i.e. box1.combine())
print(f"box1 pre add box3: {boxes['box1'].get_dim()}")
boxes['box1'].combine(boxes['box3'])
print(f"box1 post add box3: {boxes['box1'].get_dim()}")
# ● Double the size of box2
print(f"box2 pre double: {boxes['box2'].get_dim()}")
boxes['box2'].double()
print(f"box2 post double: {boxes['box2'].get_dim()}")
# ● Combine box2 into box1
print(f"box1 pre add box2: {boxes['box1'].get_dim()}")
boxes['box1'].combine(boxes['box2'])
print(f"box1 post add box2: {boxes['box1'].get_dim()}")