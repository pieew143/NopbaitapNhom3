# This is a sample Python script.
# Press Shift+
def sorting(a,b,c):
    trunggian = a+b+c - max(a,b,c) - min(a,b,c)
    return max(a,b,c), min(a,b,c), trunggian
def canhtamgiac(a, b ,c):
    kq1 = "0"
    kq2 = "0"
    canhlonnhat ,canhbenhat ,canhtrunggian = sorting(a,b,c)
    if canhlonnhat > (canhbenhat+canhtrunggian):
        kq1 = "a,b,c khong la ba canh cua tam giac"
    else:
        if canhlonnhat**2 == (canhbenhat**2 + canhtrunggian**2):
            kq1 = "tam giac la tam giac vuong"
        elif canhlonnhat**2 > (canhbenhat**2 + canhtrunggian**2):
            kq1 = "tam giac la tam giac tu"
        else:
            kq1 = "tam giac la tam giac nhon"
        if canhbenhat == canhtrunggian or canhtrunggian == canhlonnhat:
            if canhtrunggian == canhlonnhat and canhbenhat == canhtrunggian:
                kq2 = "tam giac la tam giac deu"
            else:
                kq2 = "tam giac la tam giac can"
    if kq2 != "0":
        print(kq1)
        print(kq2)
        return kq1,kq2
    else:
        print(kq1)
        return kq1

# #Press Dou Shift to search everywhere for classes, files, tool windows, actions, and
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

