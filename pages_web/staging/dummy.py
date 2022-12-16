from datetime import datetime


def date_picker(date, weekday, day_to):
    date_increasing = {"Tuesday": {"Monday": 1, "Tuesday": 7, "Wednesday": 6, "Thursday": 5,
                                   "Friday": 4, "Saturday": 3, "Sunday": 2},
                       "Wednesday": {"Monday": 2, "Tuesday": 1, "Wednesday": 7, "Thursday": 6,
                                     "Friday": 5, "Saturday": 4, "Sunday": 3},
                       "Thursday": {"Monday": 3, "Tuesday": 2, "Wednesday": 1, "Thursday": 7,
                                    "Friday": 6, "Saturday": 5, "Sunday": 4}
                       }
    if date.month in [1, 3, 5, 7, 8, 10, 12]:
        if (date.day + date_increasing[day_to][weekday]) > 31:
            if date.month == 12:
                return "{}/{}/{}".format(date.month - 11, date.day + date_increasing[day_to][weekday] - 31, date.year + 1)
            else:
                return "{}/{}/{}".format(date.month + 1, date.day + date_increasing[day_to][weekday] - 31, date.year)
        else:
            return "{}/{}/{}".format(date.month, date.day + date_increasing[day_to][weekday], date.year)
    elif date.month in [4, 6, 9, 11]:
        if (date.day + date_increasing[day_to][weekday]) > 30:
            return "{}/{}/{}".format(date.month + 1, date.day + date_increasing[day_to][weekday] - 30, date.year)
        else:
            return "{}/{}/{}".format(date.month, date.day + date_increasing[day_to][weekday], date.year)
    else:
        if (date.day + date_increasing[day_to][weekday]) > 28:
            return "{}/{}/{}".format(date.month + 1, date.day + date_increasing[day_to][weekday] - 28, date.year)
        else:
            return "{}/{}/{}".format(date.month, date.day + date_increasing[day_to][weekday], date.year)


def tickets_calendar(ticket):
    if ticket == "new_m_ticket":  # Tuesdays
        date_input = datetime.now()
        weekday = date_input.strftime('%A')
        date_output = date_picker(date=date_input, weekday=weekday, day_to="Tuesday")
        return date_output
    elif ticket == "cancel_m_ticket":  # Wednesdays
        date_input = datetime.now()
        weekday = date_input.strftime('%A')
        date_output = date_picker(date=date_input, weekday=weekday, day_to="Wednesday")
        return date_output
    elif ticket == "new_m_chat_ticket":  # Thursdays
        date_input = datetime.now()
        weekday = date_input.strftime('%A')
        date_output = date_picker(date=date_input, weekday=weekday, day_to="Thursday")
        return date_output
    else:
        date_input = datetime.now()
        return "{}/{}/{}".format(date_input.month + 1, date_input.day, date_input.year)


def date_incrementer(date_to_increase):
    date = datetime.strptime(date_to_increase, "%m/%d/%Y")
    if date.month in [1, 3, 5, 7, 8, 10, 12]:
        if (date.day + 7) > 31:
            if date.month == 12:
                return "{}/{}/{}".format(date.month - 11, date.day + 7 - 31, date.year + 1)
            else:
                return "{}/{}/{}".format(date.month + 1, date.day + 7 - 31, date.year)
        else:
            return "{}/{}/{}".format(date.month, date.day + 7, date.year)
    elif date.month in [4, 6, 9, 11]:
        if (date.day + 7) > 30:
            return "{}/{}/{}".format(date.month + 1, date.day + 7 - 30, date.year)
        else:
            return "{}/{}/{}".format(date.month, date.day + 7, date.year)
    else:
        if (date.day + 7) > 28:
            return "{}/{}/{}".format(date.month + 1, date.day + 7 - 28, date.year)
        else:
            return "{}/{}/{}".format(date.month, date.day + 7, date.year)



selected_date = tickets_calendar("new_m_ticket")
selected_date_2 = tickets_calendar("cancel_m_ticket")
selected_date_3 = tickets_calendar("new_m_chat_ticket")
print(selected_date, selected_date_2, selected_date_3)

mod_date = date_incrementer(selected_date)
mod_date_2 = date_incrementer(selected_date_2)
mod_date_3 = date_incrementer(selected_date_3)
print("New modified date 1: --> ", mod_date)
print("New modified date 2: --> ", mod_date_2)
print("New modified date 3: --> ", mod_date_3)
