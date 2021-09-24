
def check_season(user_month):
    value = ''
    seasons = {
    'autumn':['September', 'October','November'],
    'winter':['December','January','February'],
    'spring':['March','April','May'],
    'summer':['June','July','August']
    }
    for season in seasons:
        for month in seasons[season]:
            if (user_month.lower() == month.lower()) or (user_month.lower() == month.lower()[:3]):
                value = season
                break
    return value

print(check_season('October'))
print(check_season('December'))
print(check_season('April'))
print(check_season('June'))
print(check_season('juNe'))
print(check_season('DEC'))