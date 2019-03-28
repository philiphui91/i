from tkinter import *

def mpf(income):
    mpf = income * 0.05
    if income <= 7100 * 12:
        return 0

    if mpf >= 18000:
        return 18000

    return mpf

def cal_standard_rate_tax(income, mpf):
    net_income = income - mpf
    return 0.15 * net_income

def cal_progressive_rate_tax(income, mpf, single):
    taxGap = 50000
    taxRate = [0.02, 0.06, 0.1, 0.14, 0.17]

    if (single):
        nci = income - mpf - 132000
    else:
        nci = income - mpf - 264000

    if nci <= 0:
        tax = 0
    elif nci <= taxGap: # income <= 40,000
        tax = nci * taxRate[0]
    elif nci <= taxGap * 2: # income <= 80,000
        tax = taxGap * taxRate[0] + (nci - taxGap) * taxRate[1]
    elif nci <= taxGap * 3: # income <= 120,000
        tax = taxGap * taxRate[0] + taxGap * taxRate[1] + (nci - taxGap * 2) * taxRate[2]
    elif nci <= taxGap * 4: # income <= 160,000
        tax = taxGap * taxRate[0] + taxGap * taxRate[1] + taxGap * taxRate[2] + (nci - taxGap * 3) * taxRate[3]
    elif nci <= taxGap * 5: # income <= 200, 000
        tax = taxGap * taxRate[0] + taxGap * taxRate[1] + taxGap * taxRate[2] + taxGap * taxRate[3] + (nci - taxGap * 4) * taxRate[4]
    else: # income > 200,000
        tax = taxGap * taxRate[0] + taxGap * taxRate[1] + taxGap * taxRate[2] + taxGap * taxRate[3] + taxGap * taxRate[4] + (nci - taxGap * 5) * taxRate[4]
    return tax

def cal_tax():
    try:
        self_income = float(val_01.get())
        spouse_income = float(val_02.get())
        print("Self MPF: ")
        fmpf = mpf(self_income)
        print(fmpf)
        print("Spouse MPF: ")
        empf = mpf(spouse_income)
        print(empf)
        print ("Self Tax - Separate Tax:")
        if cal_progressive_rate_tax(self_income, fmpf, True) > cal_standard_rate_tax(self_income, fmpf):
            sftax = cal_standard_rate_tax(self_income, fmpf)
        else:
            sftax = cal_progressive_rate_tax(self_income, fmpf, True)

        print (sftax);
        print("Spouse Tax - Separate Tax:")
        if cal_progressive_rate_tax(spouse_income, empf, True) > cal_standard_rate_tax(spouse_income, empf):
            setax = cal_standard_rate_tax(spouse_income, empf)
        else:
            setax = cal_progressive_rate_tax(spouse_income, empf, True)
        print (setax)

        print("Joint Tax:")
        if cal_progressive_rate_tax(self_income + spouse_income, fmpf + empf, False) > cal_standard_rate_tax(self_income + spouse_income, fmpf + empf):
            jtax = cal_standard_rate_tax(self_income + spouse_income, fmpf + empf)
        else:
            jtax = cal_progressive_rate_tax(self_income + spouse_income, fmpf + empf, False)
        print (jtax)

        if sftax + setax > jtax:
            print ("recommend using Joint Tax")

    except ValueError:
        print("value error")

def centre_window(window):
    window.update_idletasks()
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    y = h / 2 - size[1] / 2
    window.geometry("%dx%d+%d+%d" % (size + (x, y)))


"""Main Program"""
window_00 = Tk()
window_00.geometry('400x100')
window_00.title('Pair programming')

centre_window(window_00)
Label(window_00, text="Self Income").grid(row=0)
Label(window_00, text="Spouse Income").grid(row=1)

val_01 = Entry(window_00)
val_02 = Entry(window_00)

val_01.grid(row=0, column=1)
val_02.grid(row=1, column=1)

Button(window_00, text='Calculate', command=cal_tax).grid(row=2, column=1)

mainloop()
