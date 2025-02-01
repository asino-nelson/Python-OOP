class Fee:
    TOTAL_FEE = 15000
    paid_fee = int(input("Enter fee amaount paid: "))

    def __init__(self, student, paid_fee = paid_fee, ):
        self.student = student
        self.paid_fee = paid_fee

    def fee_balance(self):  # Instance method

        balance = Fee.TOTAL_FEE - self.paid_fee

        if self.paid_fee < 2:
            print("Paid fee must be greater than 1")
        elif self.paid_fee > Fee.TOTAL_FEE:
            print(f"Excess payment by: Ksh.{balance*-1}")
        else:
            print(f"Balance: Ksh.{balance}") 

    @staticmethod # Static method
    def school_year(year):
        if year > 4:
            print("You should have graduated already")
        else:
            print("Keep pushing")

            
        
payment1 = Fee("Nelson")
payment1.fee_balance()
payment1.school_year(5)