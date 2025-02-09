import send_message as sm
from datetime import date

def get_current_date():
    
    today_date = date.today()
    
    day = today_date.day
    month = today_date.month
    year = today_date.year
    weekday = today_date.weekday()
    month_name = ""
    date_suffix = ""
    
    match weekday:
        case 0:
            weekday = 'Monday'
        case 1:
            weekday = 'Tuesday'
        case 2:
            weekday = 'Wednesday'
        case 3:
            weekday = 'Thursday'
        case 4:
            weekday = 'Friday'
        case 5:
            weekday = 'Saturday'
        case 6:
            weekday = 'Sunday'
            
    match month:
        case 1:
            month_name = "January"
        case 2:
            month_name = "February"
        case 3:
            month_name = "March"
        case 4:
            month_name = "April"
        case 5:
            month_name = "May"
        case 6:
            month_name = "June"
        case 7:
            month_name = "July"
        case 8:
            month_name = "August"
        case 9:
            month_name = "September"
        case 10:
            month_name = "October"
        case 11:
            month_name = "November"
        case 12:
            month_name = "December"
            
    match str(day):
        case 1:
            date_suffix = "st"
        case 2:
            date_suffix = "nd"
        case 3:
            date_suffix = "rd"
        case _:
            date_suffix = "th"
            
        
    
    return day, month, year, weekday, month_name, date_suffix

def create_message():
    '''
    Function to create messages before sending them to Whatapp client
    
    Set blank lines to the ~ character
    '''
    
    day, month, year, weekday, month_name, date_suffix = get_current_date()
    
    template = """
    {3}, {0}{4} {1} {2}
    __________________
    """.format(day, month_name, year, weekday, date_suffix)
    
    
    message = """
    This is a headless test message!
    This is line 2 of the headless message!!
    ~
    This is a third line
    """
    
    return template+"~"+message
    

def main():
    
    message = create_message()
    
    # print(message)
    
    client = sm.whatsapp_client(headless=True)
    client.send_message(message=message)

if __name__ == "__main__":
    main()