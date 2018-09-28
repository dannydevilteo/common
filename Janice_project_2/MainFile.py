import sys,datetime,re,os

from DataFile import DataFileClass

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

class MainForm(object):
    def __init__(self):
        #input student's name START
        self.student_name = MainForm.inputStdName("\nPlease enter your name according to your NRIC or passport (40 char max) : ")
        self.student_name_2 = MainForm.inputExtName("\nPlease enter your extended name if any(40 char max) : ")
        print("Your Name : " ,end=""),color.write(self.student_name.strip()+ " " +self.student_name_2,"STRING")

        #input nationality
        self.student_nationality = MainForm.inputNationality("\nNationality (40 char max) : ")
        print("Nationality : " ,end=""),color.write(self.student_nationality,"STRING")

        #input student's age START
        self.student_age = MainForm.inputStudentAge("\nPlease enter your age as of this year, "+datetime.datetime.today().strftime('%Y')+" : ")
        print("Your Age : " ,end=""),color.write(str(self.student_age),"STRING")

        #input Home address line 1
        self.student_address1 = MainForm.inputStdAddr1("\nHome Address (40 char max) : ")
        print("Home Address : " ,end=""),color.write(self.student_address1,"STRING")
        
        #input Home address line 2
        self.student_address2 = MainForm.inputStdAddr2("\nHome Address (con't...) (40 char max) : ")
        if self.student_address2 != "":
            print("Home Address (con't...) :  " ,end=""),color.write(self.student_address2,"STRING")
        
        #input Postcode
        self.student_poscode = MainForm.inputPostCode("\nPostcode (10 char max) : ")
        print("Postcode : " ,end=""),color.write(self.student_poscode,"STRING")

        #input State
        self.student_state = MainForm.inputState("\nState (40 char max) : ")
        print("State : " ,end=""),color.write(self.student_state,"STRING")

        #input country
        self.student_country = MainForm.inputCountry("\nCountry (40 char max) : ")
        print("Country : " ,end=""),color.write(self.student_country,"STRING")

        #input email
        self.student_email = MainForm.inputEmail("\nEmail Address (40 char max) :")
        print("Email Address  : " ,end=""),color.write(self.student_email,"STRING")
        
        #Course Name
        self.student_course = MainForm.inputCourse("\nCourse Name (40 char max) : ")
        print("Course Name : " ,end=""),color.write(self.student_course,"STRING")

        #Semester End
        self.course_end_date = MainForm.inputCourseEndDate("\nCourse End Date (01/01/2001) : ")
        print("Course End Date : " ,end=""),color.write(self.course_end_date,"STRING")

        #Get the list of apartment
        avai_unit = MainForm.getApartment(self)

        #Input Unit No.
        MainForm.getUnitNo(avai_unit,self)

    """********Section for Input file validation*********"""

    #Input validate (NAME)
    def inputStdName(inName):
        try:
            student_name = input(inName)
            if student_name.strip() == "":
                color.write("Name must not be empty\n","COMMENT")
                return MainForm.inputStdName(inName)
            elif len(student_name) > 40:
                color.write("Name too long. Continue to last name if above 40 max\n","COMMENT")
                return MainForm.inputStdName(inName)
            else:
                return student_name
        except ValueError:
            color.write("Exception in inputStdName(inName)\n","COMMENT")
            return MainForm.inputStdName(inName)

    def inputExtName(inName2):
        try:
            student_name_2 = input(inName2)
            if len(student_name_2) > 40:
                color.write("Extended Name too long. Max length is 40\n","COMMENT")
                return MainForm.inputExtName(inName2)
            else:
                return student_name_2
        except ValueError:
            color.write("Exception in inputStdName(inName)\n","COMMENT")
            return MainForm.inputExtName(inName2)

        #Input validate (NATIONALITY)
    def inputNationality(nationality):
        try:
            student_nationality = input(nationality)
            if student_nationality.strip() == "":
                color.write("Nationality must not be empty\n","COMMENT")
                return MainForm.inputNationality(nationality)
            elif len(student_nationality) > 40:
                color.write("Nationality too long. 40 max\n","COMMENT")
                return MainForm.inputNationality(nationality)
            else:
                return student_nationality
        except ValueError:
            color.write("Exception in inputNationality(postCode)\n","COMMENT")
            return MainForm.inputNationality(nationality)

    #Input Validate (AGE)
    def inputStudentAge(inAge):
        try:
            student_age = int(input(inAge))
            if student_age < 18:
                color.write("Age must not be below 18\n","COMMENT")
                return MainForm.inputStudentAge(inAge)
            elif student_age > 120:
                color.write("Invalid age\n","COMMENT")
                return MainForm.inputStudentAge(inAge)
            else:
                return student_age
        except ValueError:
            color.write("Please enter Numbers only without decimal\n","COMMENT")
            return MainForm.inputStudentAge(inAge)

    #Input Validate (ADDRESS 1)
    def inputStdAddr1(address1):
        try:
            student_address1 = input(address1)
            if student_address1.strip() == "":
                color.write("Address must not be empty\n","COMMENT")
                return MainForm.inputStdAddr1(address1)
            elif len(student_address1) > 40:
                color.write("Address too long. Continue to next address field if above 40 max\n","COMMENT")
                return MainForm.inputStdAddr1(address1)
            else:
                return student_address1
        except ValueError:
            color.write("Exception in inputStdAddr1(address1)\n","COMMENT")
            return MainForm.inputStdAddr1(address1)

    #Input Validate (ADDRESS 2)
    def inputStdAddr2(address2):
        try:
            student_address2 = input(address2)
            if len(student_address2) > 40:
                color.write("Address too long. max is 40 char\n","COMMENT")
                return MainForm.inputStdAddr2(address2)
            else:
                return student_address2
        except ValueError:
            color.write("Exception in inputStdAddr1(address2)\n","COMMENT")
            return MainForm.inputStdAddr2(address2)

    #Input validate (POSTCODE)
    def inputPostCode(postCode):
        try:
            addr_postcode = input(postCode)
            if addr_postcode.strip() == "":
                color.write("Postcode must not be empty\n","COMMENT")
                return MainForm.inputPostCode(postCode)
            elif len(addr_postcode) > 10:
                color.write("Postcode too long. Continue to last name if above 10 max\n","COMMENT")
                return MainForm.inputPostCode(postCode)
            else:
                return addr_postcode
        except ValueError:
            color.write("Exception in inputPostCode(postCode)\n","COMMENT")
            return MainForm.inputPostCode(postCode)

    #Input validate (STATE)
    def inputState(state):
        try:
            addr_state = input(state)
            if addr_state.strip() == "":
                color.write("State must not be empty\n","COMMENT")
                return MainForm.inputState(state)
            elif len(addr_state) > 40:
                color.write("State too long. 40 max\n","COMMENT")
                return MainForm.inputState(state)
            else:
                return addr_state
        except ValueError:
            color.write("Exception in inputState(state)\n","COMMENT")
            return MainForm.inputState(state)
        
    #Input validate (COUNTRY)
    def inputCountry(country):
        try:
            addr_country = input(country)
            if addr_country.strip() == "":
                color.write("Country must not be empty\n","COMMENT")
                return MainForm.inputCountry(country)
            elif len(addr_country) > 40:
                color.write("Country too long. 40 max\n","COMMENT")
                return MainForm.inputCountry(country)
            else:
                return addr_country
        except ValueError:
            color.write("Exception in inputCountry(country)\n","COMMENT")
            return MainForm.inputCountry(country)

    #Input validate (EMAIL)
    def inputEmail(email):
        try:
            email_addr = input(email)
            if len(email_addr) > 7:
                if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email_addr):
                    return email_addr
            color.write("Invalid Email format\n","COMMENT")
            return MainForm.inputEmail(email)
        except ValueError:
            color.write("Exception in inputEmail(email)\n","COMMENT")
            return MainForm.inputEmail(email)

    #Input validate (COURSE)
    def inputCourse(course):
        try:
            courseName = input(course)
            if courseName.strip() == "":
                color.write("Course Name must not be empty\n","COMMENT")
                return MainForm.inputCourse(course)
            elif len(courseName) > 40:
                color.write("Course Name too long. 40 max\n","COMMENT")
                return MainForm.inputCourse(course)
            else:
                return courseName
        except ValueError:
            color.write("Exception in inputCourse(course)\n","COMMENT")
            return MainForm.inputCourse(course)

    #Input validate (COURSE_END_DATE)
    def inputCourseEndDate(date):
        course_end_date = input(date)

        try:
            datetime.datetime.strptime(course_end_date, '%d/%m/%Y')
        except ValueError:
            color.write("Incorrect Date Format, 01/01/2001","COMMENT")
            return MainForm.inputCourseEndDate(date)
        course_end = ((datetime.datetime.strptime(course_end_date,"%d/%m/%Y") - datetime.datetime.strptime(datetime.datetime.today().strftime("%d/%m/%Y"),"%d/%m/%Y")).days < 30)
        if (course_end):
            color.write("Invalid course duration","COMMENT")
            return MainForm.inputCourseEndDate(date)
        else:
            return course_end_date

    #Input validate (UNIT_NO)
    def inputUnit(inUnit,avaiUnit):
        try:
            unit_no = input(inUnit)
            unit_isFound,selected_unit = MainForm.compareInput(unit_no,avaiUnit)
            if unit_no == "":
                color.write("Sorry, Unit No. must not be empty\n","COMMENT")
                return MainForm.inputUnit(inUnit,avaiUnit)
            elif not unit_isFound:
                color.write("Unit No. not found. Please key in according to the available unit above.\n","COMMENT")
                return MainForm.inputUnit(inUnit,avaiUnit)
            elif selected_unit[3] >= 3 :
                color.write("Unit No. is full, please select another unit\n","COMMENT")
                return MainForm.inputUnit(inUnit,avaiUnit)
            else:
                return unit_no,selected_unit
        except ValueError:
            unit_no = input("Exception in inputUnit(inUnit,avaiUnit)\n","COMMENT")
            return MainForm.inputUnit(inUnit,avaiUnit)

    #Function to compare input unit no against available unit no
    def compareInput(inUnit,avaiUnit):
        for i in range(len(avaiUnit)):
            if inUnit.lower() == avaiUnit[i][0].lower():
                return True,avaiUnit[i]
        return False,avaiUnit[i]

    """*******Get the Apartment info****** """

    def getApartment(self):
        avai_unit = DataFileClass.getApartmentList()
        book_unit = 0
        for i in range(len(avai_unit)):
            if avai_unit[i][3] < 3:
                book_unit += 1
                
        print("\n\nHello", end = " "),color.write(self.student_name.strip()+ " " +self.student_name_2,"STRING")
        print("\nThere are total of " + str(len(avai_unit)) + " apartments in this University with " + str(book_unit) + " unit(s) available for your booking")
        print("\nHere are the available Apartment with total of occupants for you to select :")
        print("\nUnit No.       No. of            Unit Name      Unit Address")
        print("               Occupants(s)")
        print("               per Unit")
        print("=========================================================================================")
        for unit in range(len(avai_unit)):
            insert_blank_space=" "
            insert_blank_space += insert_blank_space * (14-len(avai_unit[unit][1])) #Formula to add blank space depending on the length of the unit name.
            print(" ")
            print(avai_unit[unit][0], end = "            ")
            color.write(str(avai_unit[unit][3]),"COMMENT") if (avai_unit[unit][3]) >= 3 else print (str(avai_unit[unit][3]), end = "")
            print ("               "+str(avai_unit[unit][1])+insert_blank_space+avai_unit[unit][2],end = "")
    
        print("\n\n=========================================================================================")
        print("")
        return avai_unit

    def getUnitNo(avaiUnit,self):
        #input unit no
        unit_no, unit_detail = MainForm.inputUnit("\nPlease select the Unit No. from the available unit above : ",avaiUnit)
        print("Your selected Unit No. : " ,end="")
        color.write(unit_detail[0]+", "+unit_detail[1],"STRING")
        print("\nApartment Address : " ,end="")
        color.write(unit_detail[2],"STRING")
        print("\nWith total occupants including you : " ,end="")
        color.write(str(unit_detail[3]+1),"STRING")
        confirmation = input("\n\n\nPlease Confirm on your selected unit. (Y = Yes, N = No, Others = Exit) : ")

        if(confirmation.upper() == 'Y'):
            MainForm.printFile(unit_no,unit_detail,self)
            print("Registration completed. Please check the Booking Confirmation in the output folder")
        elif(confirmation.upper() == 'N'):
            color.write("\nPlease select your Unit No. again","COMMENT")
            input("\nPress Enter")
            MainForm.getUnitNo(avaiUnit,self)
        else:
            print('Program will Exit')
            exit(0)


    """*******Produce confirmation file******"""
    def printFile(unit_no,unit_detail,self):
        self.system_date = datetime.datetime.today().strftime("%Y%m%d")
        self.booking_date = datetime.datetime.strptime(self.system_date,"%Y%m%d")
        self.unit_no = unit_no
        self.unit_name = unit_detail[1]
        self.unit_address = unit_detail[2]
        self.unit_occupant = str(unit_detail[3]+1)
        self.unit_checkout = datetime.datetime.strptime(self.course_end_date,"%d/%m/%Y")
        self.student_name = self.student_name.strip()+ " " +self.student_name_2
        self.student_id = datetime.datetime.today().strftime("C%Y%m%d%H%M%S") #generate student id with timestamp

        #Rental Fees
        rental_fee = DataFileClass.getRates()
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
        
        
        MainForm.productTxtFile(self)

    def productTxtFile(self):
        if not os.path.exists("output"):
            os.mkdir(os.path.expanduser("output"))
        displayAddress2 = " \line "+self.student_address2 if self.student_address2!="" else ""
        file = open("output\TAX_INVOICE_"+self.student_id+"_"+self.system_date+"_"+self.unit_no.upper()+".rtf", "w") #TAX_INVOICE_STUDENTID_SYSTEMDATE_UNITNO
        #file.write("Student Id : \\b"+self.student_id)
        file.write("{\\rtf1 \sl0 \\b \\fs40Booking Confirmation \\b0 "+str("")
                   + " \\tab \\tab \\tab \line \margl360\margr720\margt720\margb720 \\fs28 \\b Student ID : \\b0 "+str(self.student_id)
                   +" \line \\b Course Name : \\b0 "+self.student_course
                   +" \line \line "+self.student_name+" \line "+self.student_address1+displayAddress2+" \line "+self.student_poscode+" "+self.student_state+" \line self.country"
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

if __name__ == "__main__":
    MainForm()
