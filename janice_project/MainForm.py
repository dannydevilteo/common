from ApartmentFile import *
from StudentFile import *
from ConfirmFile import PrintFile
import datetime

class Mainform:
    #View Student's particular when Student ID is found
    def viewParticular(stdParticular):
        print("Student ID         : ",end=""),color.write(stdParticular[0],"STRING")
        print("\nName               : ",end=""),color.write(stdParticular[1],"STRING")
        print("\nNRID               : ",end=""),color.write(stdParticular[2],"STRING")
        print("\nAddress            : ",end=""),color.write(stdParticular[3],"STRING")
        if(stdParticular[4] !=""):
            color.write("\n            "+(" ")*9+stdParticular[4],"STRING") #Address Line 2
        print("\n           "+(" ")*10,end=""),color.write(stdParticular[5],"STRING"),color.write(" "+stdParticular[6],"STRING") #Postcode & State under same like
        print("\n           "+(" ")*10,end=""),color.write(stdParticular[7],"STRING")
        print("\n\nCourse Code & Name : ",end=""),color.write(stdParticular[8]+" - "+stdParticular[9],"STRING")
        course_end_date = datetime.datetime.strptime(stdParticular[10],"%Y%m%d")
        print("\nCourse End Date    : ",end=""),color.write(course_end_date.strftime("%d %B %Y"),"STRING")
        
    def startForm():
        avai_unit = getAvailUnit()
        book_unit = 0
        for i in range(len(getAvailUnit())):
            if avai_unit[i][3] < 3:
                book_unit += 1
                
        print("Hello Student.\nThere are total of " + str(len(avai_unit)) + " apartments in this University with " + str(book_unit) + " unit(s) available for your booking")
        print("\nHere are the available Apartment with total of occupants for you to select :")
        print("\nUnit No.         Total           Unit Name      Unit Address")
        print("                 Occupants(s)")
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
        
        Mainform.getStudentID(avai_unit)

    def getStudentID(avaiUnit):
        #input student's id
        student_id = inputStdId("\nPlease enter your Student ID (15 char max) : ")
    
        #Get Student info based on student id
        student_profile=getStudentInfo(student_id)
        if student_profile == None:
            color.write("Student Id not found, please seek help from Student's Administrator to obtain your student id","COMMENT")
            Mainform.getStudentID(avaiUnit)
        else:
            course_end = ((datetime.datetime.strptime(student_profile [10],"%Y%m%d") - datetime.datetime.strptime(datetime.datetime.today().strftime("%Y%m%d"),"%Y%m%d")).days < getRentalRate()[3])
            if(student_profile[11] != ""):
                #Display student particular
                print ("\n" * 100)
                Mainform.viewParticular(student_profile)
                Mainform.getRentedUnit(avaiUnit,student_profile)
            elif (course_end):
                Mainform.viewParticular(student_profile)
                color.write("\n\nYou are not eligible to rent because your course will be ending soon","COMMENT")
                redo = input("\n\n\nPlease press Enter")
                print ("\n" * 100)
                Mainform.startForm()
            else:
                #Display student particular
                Mainform.viewParticular(student_profile)
                Mainform.getUnitNo(avaiUnit,student_profile)

    def getRentedUnit(avaiUnit,stdProfile):
        checkout_date = datetime.datetime.strptime(stdProfile[10],"%Y%m%d")
        color.write("\n\nYou are currently renting a unit.","COMMENT")
        for r in range(len(avaiUnit)):
            if(stdProfile[11] == avaiUnit[r][0]):
                color.write("\nUnit Info    : "+stdProfile[11]+", "+avaiUnit[r][1],"COMMENT")
                color.write("\nUnit Address : "+avaiUnit[r][2],"COMMENT")
                color.write("\nCheck Out By : "+checkout_date.strftime("%d %B %Y"),"COMMENT")
        redo = input("\n\n\nPlease press Enter")
        print ("\n" * 100)
        Mainform.startForm()
        
    def getUnitNo(avaiUnit,studentProfile):
        #input unit no
        unit_no, unit_detail = inputUnit("\nPlease select the Unit No. from the available unit above : ",avaiUnit)
        print("Your selected Unit No. : " ,end="")
        color.write(unit_detail[0]+", "+unit_detail[1],"STRING")
        print("\nApartment Address : " ,end="")
        color.write(unit_detail[2],"STRING")
        print("\nWith total occupants including you : " ,end="")
        color.write(str(unit_detail[3]+1),"STRING")
        confirmation = input("\n\n\nPlease Confirm on your selected unit. (Y = Yes, N = No, Others = Exit) : ")

        if(confirmation.upper() == 'Y'):
            PrintFile(unit_no,unit_detail,studentProfile)
            print("Registration completed. Please check the Booking Confirmation in the output folder")
        elif(confirmation.upper() == 'N'):
            color.write("\nPlease select your Unit No. again","COMMENT")
            input("\nPress Enter")
            Mainform.getUnitNo(avaiUnit,studentProfile)
        else:
            print('Program will Exit')
            exit(0)

if __name__ == "__main__":
    Mainform.startForm()





