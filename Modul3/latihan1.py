data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

outputData = []

def convertToMinutes(weeks,days,hours,minutes):
    return ( weeks * 7 * 24 * 60 ) + ( days * 24 * 60 ) + ( hours * 60 + minutes )

def curriedCoverter(weeks):
    def dayInner(days):
        def hourInner(hours):
            def minuteInner(minutes):
                return convertToMinutes(weeks,days,hours,minutes)
            return minuteInner
        return hourInner
    return dayInner

for item in data:
    parser = item.split()
    weeks = int(parser[0])
    days = int(parser[2])
    hours = int(parser[4])
    minutes = int(parser[6])

    convertedValues = curriedCoverter(weeks)(days)(hours)(minutes)
    outputData.append(convertedValues)

print("OutputData = " ,outputData)