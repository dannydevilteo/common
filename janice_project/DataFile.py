"""For this assignment the total of apartment is hard coded because we are not directly taking the information from database or any other provided eg: webservices, batch files, etc.
The value app_tenant[x][0] can be changed to any aprtment names that you desire. In real application, it is best to define a function just to retrieve the live record of the apartments
[UNIT_NO][UNIT_NAME][UNIT_ADDR][TOTAL_OCCUPANT]
"""
def getApartmentList():
    return [["1A-01","Anggerik","Block A, 1 Taman Teknologi Malaysia, 33/561 Jalan Kulat",2],
            ["1A-02","Anggerik","Block A, 1 Taman Teknologi Malaysia, 33/561 Jalan Kulat",3],
            ["1A-11","Anggerik","Block A, 1 Taman Teknologi Malaysia, 33/561 Jalan Kulat",2],
            ["1D-02","Dahlia","Block D, 1 Taman Teknologi Malaysia, 33/566 Jalan Cendawan",3],
            ["1D-05","Dahlia","Block D, 1 Taman Teknologi Malaysia, 33/566 Jalan Cendawan",0],
            ["1D-10","Dahlia","Block D, 1 Taman Teknologi Malaysia, 33/566 Jalan Cendawan",1],
            ["1E-03","Enggang","Block E, 1 Taman Teknologi Malaysia, 33/564 Jalan Mendung",2],
            ["1E-11","Enggang","Block E, 1 Taman Teknologi Malaysia, 33/564 Jalan Mendung",2]]


"""Student's record is hardcoded because we are not connecting to DB or any host server to fetch the student's particular. In this project we assume that student is already onboarded with the
university and student's particular is already registered to existing system in the uni. Here are the sequence in the list:
[[STUDENTID][STUDENTNAME][NRID][MAILING_ADDR1][MAILING_ADDR2][POSTCODE][STATE][COUNTRY][COURSEID][COURSE_NAME][SEMESTER_END_DATE][UNIT_NO][LAST_CHECK_IN]]
"""
def getStudentList():
    return [["C11223344","Joe Bob Sam Ray","880418-13-5555","1 street road","No.3 main street","336600","Minowa","US and A","BSC01","BSC in Information Technology","20181031","1E","20180701"],
                    ["C11223344","Joe Bob Sam Ray","880418-13-5555","1 street road","No.3 main street","336600","Minowa","US and A","BSC01","BSC in Information Technology","20181031","1E","20180701"],
                    ["C11999344","Prakash Kumar","7777885-34-01","101 cape street","ZZZAAAPPP AAAA","555664","New Delhi","India","MSC022","MSC in Data Analytic","20190308","",""],
                    ["C0000012","Xin Hao","CC-01-6667755","18 Harmony Street","Some province in China","00008762","Shenzhen","China","BAC08","Bachelor of Business in FInance","20181007","",""],
                    ["C30888877","Amir Khan","A090443-03","12 pain road","XXX PPP XXXX","66600","Some state","Armenia","BAC07","Bachelor of Arts & Socialogy","20181108","1H","20180801"]]

#Currency Type, Room Rate, Tax,Exceed Term of stay
def getRates():
    return ["MYR",300,5,15]
