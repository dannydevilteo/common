"""For this assignment the total of apartment is hard coded because we are not directly taking the information from database or any other provided eg: webservices, batch files, etc.
The value app_tenant[x][0] can be changed to any aprtment names that you desire. In real application, it is best to define a function just to retrieve the live record of the apartments
[UNIT_NO][UNIT_NAME][UNIT_ADDR][TOTAL_OCCUPANT]
"""
class DataFileClass:
    def getApartmentList():
        return [["1A-01","Anggerik","Block A, 1 Taman Teknologi Malaysia, 33/561 Jalan Kulat",2],
            ["1A-02","Anggerik","Block A, 1 Taman Teknologi Malaysia, 33/561 Jalan Kulat",3],
            ["1A-11","Anggerik","Block A, 1 Taman Teknologi Malaysia, 33/561 Jalan Kulat",2],
            ["1D-02","Dahlia","Block D, 1 Taman Teknologi Malaysia, 33/566 Jalan Cendawan",3],
            ["1D-05","Dahlia","Block D, 1 Taman Teknologi Malaysia, 33/566 Jalan Cendawan",0],
            ["1D-10","Dahlia","Block D, 1 Taman Teknologi Malaysia, 33/566 Jalan Cendawan",1],
            ["1E-03","Enggang","Block E, 1 Taman Teknologi Malaysia, 33/564 Jalan Mendung",2],
            ["1E-11","Enggang","Block E, 1 Taman Teknologi Malaysia, 33/564 Jalan Mendung",2]]



#Currency Type, Room Rate, Tax,Exceed Term of stay
    def getRates():
        return ["MYR",300,5,15]
