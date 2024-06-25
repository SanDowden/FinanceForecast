def getMonthYearLabel(month, year):
    tmp = str(month)
    if month < 10:
        tmp = "0" + tmp
    return f"{tmp}/{year}"