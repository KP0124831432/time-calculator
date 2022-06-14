def add_time(s, d, day_of_the_week=None):
    # s = start ... d = duration
    dw = ('monday', 'tuesday',
          'wednesday', 'thursday',
          'friday', 'saturday', 'sunday')
    # Treating input
    check_start = 'Full' \
        if 'AM' not in s and 'PM' not in s else f"{'AM' if 'AM' in s else 'PM'}"
    # Converting time to 24H clock and then to minutes:
    time = s.split(':')
    hour, minute = time[0], time[1][0:2]
    h = hour if check_start == 'AM' else f'{int(hour) + 12}'
    converted_s_to_minutes = (int(h) * 60) + int(minute)
    # Converting second input to minutes
    duration = d.split(':')
    converted_d_to_minutes = (int(duration[0]) * 60) + int(duration[1])
    total = converted_s_to_minutes + converted_d_to_minutes
    day_duration = 24
    r_hours = (day_duration * 60) - converted_s_to_minutes
    # Number of days :
    numb_days = int(((converted_d_to_minutes - r_hours) / 60) / 24) + 1 \
        if converted_d_to_minutes >= r_hours else 0
    # Converting Back :
    converted_total = total / 60
    new_hour_system = converted_total - (numb_days * 24)
    pack_converted = str(new_hour_system).split('.')
    treated_hour = pack_converted[0]
    period = 'PM' if int(treated_hour) >= 12 else 'AM'
    converted_hour = str(int(treated_hour) - 12).lstrip()\
        if period == 'PM' else treated_hour.lstrip()
    converted_minute = str(round(60 * float('0.' + pack_converted[1]))).rstrip()
    # Creating String
    if day_of_the_week:
        input_cd = day_of_the_week.lower()
        current = int((numb_days + dw.index(input_cd)) % 7)
        current_day = dw[current]
        day_of_the_w = f' {current_day.title()}'

    # Main string
    # pre_fixed_hour = converted_hour.strip() if int(converted_hour) >= 10 else '0' + converted_hour.strip()

    fixed_hour = converted_hour if converted_hour != '0' else str(int(converted_hour) + 12)
    fixed_minute = converted_minute.strip() if int(converted_minute)\
        >= 10 else '0' + converted_minute.strip()
    fixed_period = f' {period.strip()},' if day_of_the_week else f' {period.strip()}'
    main_string = fixed_hour + ":" + fixed_minute + fixed_period
    # Complement
    complement = ' (next day)' if numb_days == 1 else f' ({numb_days} days later)'
    if not day_of_the_week:
        return main_string + complement if numb_days >= 1 else main_string
    elif numb_days == 0:
        return main_string + day_of_the_w.title()
    else:
        return main_string + day_of_the_w.title() + complement


