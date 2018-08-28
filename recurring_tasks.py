def recurringTask(firstDate, k, daysOfTheWeek, n):
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days = {'Sunday': 0, 'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6}
    start = firstDate.split('/')
    day = int(start[0])
    month = int(start[1].lstrip('0'))
    year = int(start[2])
    day_diff = 0
    for m in range(1, month):
        day_diff += months[m]
    diff = abs(2015 - year) * 365.25

    print("year diff:", diff)

    print("days:", day_diff)
    total_diff = round(diff - day_diff)
    print("total diff:", total_diff)

    dates = []

    for i in range(n):
        for elem in daysOfTheWeek:
            if day + days[elem] > months[month]:
                day = days[elem] - (months[month] - day)
                month += 1
            else:
                day = day + days[elem]
            dates.append("{}/{}".format(day, month))
            print("DAY: {}. MONTH: {}".format(str(day), str(month))


    # if total_diff % 7 >= 4:
    #     day_week = total_diff % 7 - 4
    # else:
    #     day_week = 4 - total_diff % 7

    # print("day:", days[day_week])


recurringTask('01/03/2014', 2, ['Monday'], 4)
# print(recurringTask('01/01/2015', 2, ['Monday'], 4))

