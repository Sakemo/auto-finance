from datetime import datetime

def GET_DATE(verify_time, searched_time):
    if searched_time[0] != 0:
        if searched_time[1] != 0:
            if searched_time[2] !=0:
                return verify_time.day == searched_time[0] and verify_time.month == searched_time[1] and verify_time.year == searched_time[2]
    else:
        if searched_time[1] != 0:
            if searched_time[2] !=0:
                return verify_time.month == searched_time[1] and verify_time.year == searched_time[2]            
        else:
            if searched_time[2] !=0:
                return verify_time.year == searched_time[2]         
            else:
                return None