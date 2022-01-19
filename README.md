# Loan-Calculator with GUI

#### Major Recallings from the Project

- The Tkinter module contains the Tk toolkit. Here the whole module of Tkinter was imported in the first line. Next, a user-defined Class named **LoanCalculator** is calculated which holds its own data member and member functions.

- def__init__(self) is a special method in Python Class. It is a constructor of a Python class. Then a window is created using Tk(). The label function creates a display box to take input and use the grid method to give it a table-like structure.

> Note : By default widgets are created in the center using sticky arguments we can change it. It takes 4 values: N, S, E, W. i.e. North, East, South, West. This is used while placing the positions in the GUI.
 
- The object named self.annualInterestRateVar, self.numberOfYearsVar, self.loanAmountVar, self.monthlyPaymentVar, self.totalPaymentVar are created and for the first three objects the input is taken using entry() function.

- After which the button namely compute payment was created, when it is clicked it calls the compute payment function which belongs to the class loan calculator. Using mainloop function we run our application program. The function computepayment() is inside the class. Here inputs of the object in some variables are stored, to simplify our mathematical calculation.

- Further another function named getMonthlyPayment() inside the class. After getting the required inputs it computes the monthly payment using the simple mathematical function given in the program.

- root=Tk() is used to initialize tkinter , It isi used to create a widget which is a window. 
Note that root widget must be created before any other widget.

## Output:
![loan calculator](https://user-images.githubusercontent.com/55132850/150169593-927391ec-b23c-4ed5-9f6f-5b9c0e42e533.PNG)

