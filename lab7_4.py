import calendar



def create_calendar_page(m = 11, y = 2016):
    month = calendar.monthcalendar(y, m)
    weeks = []
    result = ["--------------------", "MO TU WE TH FR SA SU", "--------------------"]
    for week in month:
        lst = []
        for date in week:
            if date == 0:
                date = " "
            elif 1 <= date < 10:
                date = "0" +str(date)
            lst.append(str(date))
        weeks.append(lst)

    for i in range(len(weeks[0])):
        if weeks[0][i] == " ":
            weeks[0].remove(weeks[0][i])
            weeks[0].insert(i, "  ")

    for week in weeks:
        week = " ".join(week)
        result.append(week)



    result = "\n".join(result)
    return result










