from instructions import *
from test import instructions_variables_20, instructions_variables_21, old_intake_data
from datetime import datetime, timedelta

instructions_21 = get_tax_variables_2021(instructions_variables_21)
instructions_20 = get_tax_variables_2020(instructions_variables_20)
intake_data = get_intake_data(old_intake_data)

def generate_dates(input_str, start_date):
   
    if input_str == "":
        return ""
    
    try:
        num_days = int(input_str)
    except ValueError:
        return "Invalid input"
    
    start_date = datetime.strptime(start_date, "%m/%d")
  
    dates = [(start_date + timedelta(days=i)).strftime("%m/%d") for i in range(num_days)]
    
    return " ".join(dates)

def get_7202_data(instructions_20, instructions_21, intake_data):

    data_7202_21_4b = generate_dates(intake_data["T40"], "01/04")
    data_7202_21_6b = generate_dates(intake_data["T38"], "01/14")
    data_7202_21_38b = generate_dates(intake_data["T41"], "04/01")
    data_7202_21_40b = generate_dates(intake_data["T44"], "04/11")

    


get_7202_data(instructions_20, instructions_21, intake_data)



