def loanAmort(initial, apr, time):
  ## ADD TOTAL CUMULATIVE PAYMENT, REORDER THE TOTAL PAID/INTEREST PAID SECTION
  #print which month it is, counter starting at one stopping at term length
  #calculate monthly payment for current month (counter)
  #calculate interest left remaining on loan, print
  #calculate principle left remaining on loan, print
  pir = (apr / time)
  totalInt = 0
  totalPaid = 0
  prinPayment = (initial / time)
  remaining = initial

  for x in range(1, (time + 1)):

    monthlyPayment = (initial * pir) / (1 - (1 + pir)**(-time))
    intThisMonth = (monthlyPayment - prinPayment)
    remaining += intThisMonth
    remaining -= monthlyPayment
    #print month > interest this month > principle (monthly payment w/o int) > remaining balance on principle (initial - totalpaid)
    if(x < 10):
      print(str(x) + "      " + "%.2f" % intThisMonth + "            " + "%.2f" % prinPayment + "            " + "%.2f" % (remaining))
    else:
      print(str(x) + "     " + "%.2f" % intThisMonth + "            " + "%.2f" % prinPayment + "            " + "%.2f" % (remaining))

    #print(str(prinPayment) + " is principal payment for month " + str(x))

    totalPaid += monthlyPayment
    totalInt += (monthlyPayment - prinPayment)


  print(" ")
  print("Total Paid     |   Total Interest Paid")
  print("--------------------------------------")
  print("%.2f" % totalPaid + "             " + "%.2f" % totalInt)

  #print total amount paid between interest and principle, then print only the interest paid on the loan

#must print month number, interest amount paid, principle paid (equals to sum of the payment) and priciple remaining at end of month. then output total amount of interest paid and total amount paid (interest and principle)

# Monthly payment is calculated using this formula:
# P = (Pv*R) / [1 - (1 + R)^(-n)] (** for exponent in python syntax)
# pir = (apr / time)
# monthlyPayment = (initial * pir) / (1 - (1 + pir)**(-time))
# where :
#     Pv = Present Value (amount of loan, initial principle)
#     APR = Annual percentage rate
#     R = Periodic interest rate = APR/ interest periods per year (time)
#     P = Monthly Payment
#     n = # of interest periods for overall time period

  return

#check for exceptions
initialPrinciple = float(input("Please enter your initial Principle: "))
apr = float(input("Enter your APR (in percentage. eg. 12.5) Do not use '%' symbol: "))
apr = (apr / 100)
time = int(input("Enter the length of your term (in months) : "))

print("Month | Interest Owed | Principle Owed |  Principle Remaining ")
print("-------------------------------------------------------------------------------")

loanAmort(initialPrinciple, apr, time)
