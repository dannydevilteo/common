import sys,datetime,os
from DataFile import *

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

class PrintFile(object):
    def __init__(self,unit_no,unit_detail,student_profile):
        self.system_date = datetime.datetime.today().strftime("%Y%m%d")
        self.booking_date = datetime.datetime.strptime(self.system_date,"%Y%m%d")
        self.unit_no = unit_no
        self.unit_name = unit_detail[1]
        self.unit_address = unit_detail[2]
        self.unit_occupant = str(unit_detail[3]+1)
        self.unit_checkout = datetime.datetime.strptime(student_profile [10],"%Y%m%d")
        self.student_id = student_profile [0]
        self.student_name = student_profile [1]

        #Rental Fees
        rental_fee = getRates()
        self.rental_currency_fee = rental_fee[0]
        self.rental_rate = rental_fee[1]
        self.rental_tax = rental_fee[2]
        self.rental_max_stay = rental_fee[3]
        self.total_stay = (self.unit_checkout-self.booking_date).days

        #Calculate Rental Fee = (Total days x 300) + tax. If today days in final month is 15 or more it will considered as 1 month. Over stay days can be parameterized.
        overstay = 1 if (self.total_stay%30) >= 15 else 0
        self.total_rental = ((self.total_stay+overstay)//30*self.rental_rate)
        self.total_rental +=  self.total_rental*(self.rental_tax/100)
        self.total_rental = "{:0.2f}".format(self.total_rental)
        
        
        PrintFile.productTxtFile(self)

    def productTxtFile(self):
        if not os.path.exists("output"):
            os.mkdir(os.path.expanduser("output"))
        file = open("output\TAX_INVOICE_"+self.student_id+"_"+self.system_date+"_"+self.unit_no.upper()+".rtf", "w") #TAX_INVOICE_STUDENTID_SYSTEMDATE_UNITNO
        #file.write("Student Id : \\b"+self.student_id)
        file.write("{\\rtf1 \sl0 \\b \\fs40Booking Confirmation \\b0 "+str("")
                   + " \\tab \\tab \\tab \line \margl360\margr720\margt720\margb720 \\fs28 \\b Student ID : \\b0 "+str(self.student_id)
                   +" \line \line Asia Pacific University (APU) \line Jalan Teknologi 5 \line Taman Teknologi Malaysia \line 57000 Wilayah Persekutuan Kuala Lumpur \line Peninsular Malaysia"
                   +"\line \line Dear "+self.student_name
                   +"\line \line This is to inform you know that the University have received your booking to stay at our apartment from " +datetime.datetime.today().strftime('%d %B %Y')+" with the details below :"
                   +"\line \line \\b Unit No. & Name : \\b0 " +self.unit_no.upper()+", "+self.unit_name+ "\line \\b Unit Address : \\b0" +self.unit_address
                   + "\line \\b Number of guest(s) including yourself : \\b0 " +self.unit_occupant
                   +"\line \\b Check Out Date : \\b0 " + self.unit_checkout.strftime('X%d %B %Y').replace('X0','X').replace('X','')
                   +"\line \line A to total of \\b " +self.rental_currency_fee +" "+self.total_rental+" \\b0 (\\b "+self.rental_currency_fee+" "+(str(self.rental_rate))+" \\b0 per month) inclusive of \\b "
                   +str(self.rental_tax)+"% \\b0 Sales and Service Tax will be deducted from your total credit with the University."
                   +"\line \line Kindly obey the house rules which is set by the property management of this University. The property management in collaboration with Student Afair Administration has the right to "
                   +"request the student to vacate the unit if student is found violating the house rules and policy."
                   +"\line We like to thank you and hope you have an enjoyable stay while studying with us."
                   +"\line \line \line \line APU Student Afair Administration"
                   +"\line \line \\fs20 This is a computer generated advice with no signature required"
                   +"}")

        file.close()
