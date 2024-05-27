from instructions import *
from test import instructions_variables_20, instructions_variables_21, old_intake_data
from datetime import datetime, timedelta
import json

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

    G5 = intake_data["T40"]
    G6 = intake_data["T38"]
    G7 = 0
    G8 = 0
    G9 = 0
    G10 = 10 - G9
    G11 = min(G5, G10)
    G12 = G10-G11
    G14 = min(G6, G12)
    G15 = max(instructions_20['M119'], instructions_21['N119'])
    G17 = round(G15/260)
    G19 = min(G17, 511)
    G20 = G11*G19
    G21 = round(G17*0.67)
    G22 = min(G21,200)
    G23 = G14*G22
    G24 = G23+G20
    G25 = 0
    G26 = 0
    G27 = G25+G26
    G28 = 0
    G29 = 0
    G30 = G28+G29
    G31 = G23+G30
    G33 = 0
    G34 = G31+G33
    G35 = min(G34,2000)
    G36 = G34-G35
    G37 = G20+G27+G35
    G38 = 0
    G39 = G37+G38
    G40 = min(G39,5110)
    G41 = G39-G40
    G42 = G36+G41
    G43 = G24 if G30 + G27 == 0 else max(G24 - G42, 0)
    G46 = min(intake_data["T42"]-G6, 50)
    G47 = 0
    G48 = 0 if G46 == 0 else 50 - G47
    G49 = min(G48,G46)
    G50 = max(instructions_20['M119'], instructions_21['N119'])
    G51 = round(G50/260)
    G53 = round(G51*0.67)
    G54 = min(G53,200)
    G55 = round(G54*G49)
    G56 = 0
    G57 = 0
    G58 = G56+G57
    G59 = G58+G55
    G61 = 0 
    G62 = G59+G61
    G63 = min(G62, 10000)
    G64 = G62-G63
    G65 = max(G55-G64,0)
    G67 = intake_data["T39"]
    G68 = 0 if G67 > 9 else min(10 - G67, intake_data["T44"])
    G69 = min(10,G67)
    G70 = 0 if G67 == 0 else 10 - G69
    G72 = min(G68, G70)
    G73 = max(instructions_20['M119'], instructions_21['N119'])
    G75 = round(G73/260)
    G77 = min(G75,511)
    G78 = G69*G77
    G79 = round(G75*0.67)
    G80 = min(G79,200)
    G81 = G80*G72
    G82 = G78+G81
    G83 = 0
    G84 = 0
    G85 = G81+G84
    G87 = min(G85, 2000)
    G88 = G85-G87
    G89 = G78+G83+G87
    G90 = min(G89,5110)
    G91 = G89-G90
    G92 = G88+G91
    G93 = max(G82-G92,0)
    G96 = min(intake_data["T45"], 60)
    G97 = max(instructions_20['M119'], instructions_21['N119'])
    G98 = round(G97/260)
    G100 = round(G98*0.67)
    G101 = min(G100,200)
    G102 = G96*G101
    G103 = 0
    G104 = G102+G103
    G106 = min(G104,12000)
    G107 = G104-G106
    G108 = max(G102-G107,0)
    H111 = G43+G65
    H112 = G93+G108

    if instructions_20["M53"] > instructions_21["N53"]:
        greater_variable = "20 SE INCOME PER COMPUTER"
        greater_variable_value = instructions_20["M53"] 
    elif instructions_20["M53"] < instructions_21["N53"]:
        greater_variable = "21 SE INCOME PER COMPUTER"
        greater_variable_value = instructions_21["N53"]
    
    if instructions_20["M119"] > instructions_21["N119"]:
        greater_variable = "20 TOTAL NET EARNINGS PER COMPUTER"
        greater_variable_value = instructions_20["M119"]
    elif instructions_20["M119"] < instructions_21["N119"]:
        greater_variable = "21 TOTAL NET EARNINGS PER COMPUTER"
        greater_variable_value = instructions_21["N119"]

    if greater_variable == "21 TOTAL NET EARNINGS PER COMPUTER" or greater_variable == "20 TOTAL NET EARNINGS PER COMPUTER":
        pdf_flag = "FALSE"
    else:
        pdf_flag = "TRUE"

    data_7202_21 = {
        "data_7202_21_1": G5,
        "data_7202_21_2": G6,
        "data_7202_21_3a": G7,
        "data_7202_21_3b": G8,
        "data_7202_21_3c": G9,
        "data_7202_21_3d": G10,
        "data_7202_21_4a": G11,
        "data_7202_21_4b": data_7202_21_4b,
        "data_7202_21_5": G12,
        "data_7202_21_6a": G14,
        "data_7202_21_6b": data_7202_21_6b,
        "data_7202_21_7a": G15,
        "data_7202_21_8": G17,
        "data_7202_21_9": G19,
        "data_7202_21_10": G20,
        "data_7202_21_11": G21,
        "data_7202_21_12": G22,
        "data_7202_21_13": G23,
        "data_7202_21_14": G24,
        "data_7202_21_15a": G25,
        "data_7202_21_15b": G26,
        "data_7202_21_15c": G27,
        "data_7202_21_16a": G28,
        "data_7202_21_16b": G29,
        "data_7202_21_16c": G30,
        "data_7202_21_17a": G31,
        "data_7202_21_17b": G33,
        "data_7202_21_17c": G34,
        "data_7202_21_18": G35,
        "data_7202_21_19": G36,
        "data_7202_21_20a": G37,
        "data_7202_21_20b": G38,
        "data_7202_21_20c": G39,
        "data_7202_21_21": G40,
        "data_7202_21_22": G41,
        "data_7202_21_23": G42,
        "data_7202_21_24": G43,
        "data_7202_21_25a": G46,
        "data_7202_21_25b": G47,
        "data_7202_21_25c": G48,
        "data_7202_21_25d": G49,
        "data_7202_21_26a": G50,
        "data_7202_21_27": G51,
        "data_7202_21_28": G53,
        "data_7202_21_29": G54,
        "data_7202_21_30": G55,
        "data_7202_21_31a": G56,
        "data_7202_21_31b": G57,
        "data_7202_21_31c": G58,
        "data_7202_21_32a": G59,
        "data_7202_21_32b": G61,
        "data_7202_21_32c": G62,
        "data_7202_21_33": G63,
        "data_7202_21_34": G64,
        "data_7202_21_35": G65,
        "data_7202_21_36": G67,
        "data_7202_21_37": G68,
        "data_7202_21_38a": G69,
        "data_7202_21_38b": data_7202_21_38b,
        "data_7202_21_39": G70,
        "data_7202_21_40a": G72,
        "data_7202_21_40b": data_7202_21_40b,
        "data_7202_21_41a": G73,
        "data_7202_21_42": G75,
        "data_7202_21_43": G77,
        "data_7202_21_44": G78,
        "data_7202_21_45": G79,
        "data_7202_21_46": G80,
        "data_7202_21_47": G81,
        "data_7202_21_48": G82,
        "data_7202_21_49": G83,
        "data_7202_21_50": G84,
        "data_7202_21_51": G85,
        "data_7202_21_52": G87,
        "data_7202_21_53": G88,
        "data_7202_21_54": G89,
        "data_7202_21_55": G90,
        "data_7202_21_56": G91,
        "data_7202_21_57": G92,
        "data_7202_21_58": G93,
        "data_7202_21_59": G96,
        "data_7202_21_60a": G97,
        "data_7202_21_61": G98,
        "data_7202_21_62": G100,
        "data_7202_21_63": G101,
        "data_7202_21_64": G102,
        "data_7202_21_65": G103,
        "data_7202_21_66": G104,
        "data_7202_21_67": G106,
        "data_7202_21_68": G107,
        "data_7202_21_69": G108,
        "data_7202_21_sch_3_13b": H111,
        "data_7202_21_sch_3_13h": H112,
        f"{greater_variable}": greater_variable_value,
        "data_pdf_flag": pdf_flag        
    }

    print(json.dumps(data_7202_21,indent=3))

    return data_7202_21
   

get_7202_data(instructions_20, instructions_21, intake_data)
