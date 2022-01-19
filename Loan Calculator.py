import tkinter
class LoanCalculator:
    def __init__( self ):
        window = tkinter.Tk()  # Create a window
        window.title("Loan Calculator")  # Set title
        # the input boxes.
        tkinter.Label(window, text="Annual Interest Rate").grid(row=1,
                                                                column=1, sticky=tkinter.W)
        tkinter.Label(window, text="Number of Years").grid(row=2,
                                                           column=1, sticky=tkinter.W)
        tkinter.Label(window, text="Loan Amount").grid(row=3,
                                                       column=1, sticky=tkinter.W)
        tkinter.Label(window, text="Monthly Payment").grid(row=4,
                                                           column=1, sticky=tkinter.W)
        tkinter.Label(window, text="Total Payment").grid(row=5,
                                                         column=1, sticky=tkinter.W)
        # taking inputs
        self.annualInterestRateVar = tkinter.StringVar()
        tkinter.Entry(window, textvariable=self.annualInterestRateVar,
                      justify=tkinter.RIGHT).grid(row=1, column=2)
        self.numberOfYearsVar = tkinter.StringVar()
        tkinter.Entry(window, textvariable=self.numberOfYearsVar,
                      justify=tkinter.RIGHT).grid(row=2, column=2)
        self.loanAmountVar = tkinter.StringVar()
        tkinter.Entry(window, textvariable=self.loanAmountVar,
                      justify=tkinter.RIGHT).grid(row=3, column=2)
        self.monthlyPaymentVar = tkinter.StringVar()
        lblMonthlyPayment = tkinter.Label(window, textvariable=
        self.monthlyPaymentVar).grid(row=4,
                                     column=2, sticky=tkinter.E)
        self.totalPaymentVar = tkinter.StringVar()
        lblTotalPayment = tkinter.Label(window, textvariable=
        self.totalPaymentVar).grid(row=5,
                                   column=2, sticky=tkinter.E)
        # the button for computing payment
        btComputePayment = tkinter.Button(window, text="Compute Payment",
                                          command=self.computePayment).grid(
            row=6, column=2, sticky=tkinter.E)
        window.mainloop()  # Create an event loop
    # computing the total payment.
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        # compute the monthly payment.
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;
        # creating the widget
        root = tkinter.Tk()
    def computePayment(self):
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberOfYearsVar.get()))
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
\
                      * int(self.numberOfYearsVar.get())
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

# calling the calss for calualting the loan
LoanCalculator()