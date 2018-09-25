import sys
from DataFile import *

try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")

#Function to filter out only the available apartment.
def getAvailUnit():
        return getApartmentList()
        """avai_unit = []
        for u in range(total_apt):
                if(app_tenant[u][3] < 3):
                        avai_unit.append([app_tenant[u][0],app_tenant[u][1],app_tenant[u][2],app_tenant[u][3]])
        return avai_unit"""

#Function to validate input for unit no
def inputUnit(inUnit,avaiUnit):
    try:
        unit_no = input(inUnit)
        unit_isFound,selected_unit = compareInput(unit_no,avaiUnit)
        if unit_no == "":
                color.write("Sorry, Unit No. must not be empty\n","COMMENT")
                return inputUnit(inUnit,avaiUnit)
        elif not unit_isFound:
                color.write("Unit No. not found. Please key in according to the available unit above.\n","COMMENT")
                return inputUnit(inUnit,avaiUnit)
        elif selected_unit[3] >= 3 :
                color.write("Unit No. is full, please select another unit\n","COMMENT")
                return inputUnit(inUnit,avaiUnit)
        else:
                return unit_no,selected_unit
    except ValueError:
        unit_no = input("Exception in inputUnit(inUnit,avaiUnit)\n","COMMENT")
        return inputUnit(inUnit,avaiUnit)

#Function to compare input unit no against available unit no
def compareInput(inUnit,avaiUnit):
        for i in range(len(avaiUnit)):
                if inUnit.lower() == avaiUnit[i][0].lower():
                        return True,avaiUnit[i]
        return False,avaiUnit[i]

def getRentalRate():
        return getRates()
