def dayOfProgrammer(year):

    if 1700 <= year <= 2700:
        if year == 1918:
           
            return f"26.09.{year}"
        elif year < 1918:  
       
            is_leap = (year % 4 == 0)
        else:
            is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

     
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if is_leap:
            days_in_month[2] = 29

        days_passed = 0
        month = 0
        for i in range(1, 13):
            if days_passed + days_in_month[i] >= 256:
                month = i
                day = 256 - days_passed
                break
            days_passed += days_in_month[i]

        return f"{day:02d}.{month:02d}.{year}"
    else:
        return "Año fuera del rango permitido (1700-2700)."

