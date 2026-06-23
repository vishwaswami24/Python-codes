def MonthlyPay(a,n,r):
    r=r/(12*100)
    n=n*12
    emi=(a*r*pow(1+r,n))/(pow(1+r,n)-1)
    print('Monthly EMI:',emi)

a=int(input('Loan Amount:'))
n=int(input('Loan Period(in years):'))
r=int(input('Rate of interest(in %):'))
MonthlyPay(a,n,r)
    
