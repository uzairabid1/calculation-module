from instructions import *
from form_7202_21 import *
from test import instructions_variables_20, instructions_variables_21, old_intake_data
from datetime import datetime, timedelta
import json

instructions_21 = get_tax_variables_2021(instructions_variables_21)
instructions_20 = get_tax_variables_2020(instructions_variables_20)
intake_data = get_intake_data(old_intake_data)


data_7202_21 = get_7202_data(instructions_20, instructions_21, intake_data)


def get_sch3_data():
    
    AB10 = instructions_21["N97"]
    AB12 = instructions_21["N91"]
    AB13 = instructions_21["N98"]
    AB14 = instructions_21["N99"]
    AB15 = instructions_21["N100"]

    V17 = instructions_21["N121"]
    V18 = instructions_21["N122"]
    V19 = instructions_21["N123"]
    V20 = instructions_21["N124"]
    V21 = instructions_21["N125"]
    V22 = instructions_21["N126"]
    V23 = instructions_21["N127"]

    AB31 = V17+V18+V19+V20+V21+V22+V23
    AB33 = AB10+AB12+AB13+AB14+AB15+AB31

    AB38 = instructions_21["N68"]
    AB39 = instructions_21["N102"]
    AB40 = instructions_21["N103"]
    AB41 = instructions_21["N128"]
    AB42 = instructions_21["N128"]

    V43 = instructions_21["N129"]
    V46 = instructions_21["N63"]
    V48 = 0
    V49 = 0
    V50 = instructions_21["N90"]
    V52 = instructions_21["N130"]


    V45 = data_7202_21["data_7202_21_sch_3_13b"]
    V54 = data_7202_21["data_7202_21_sch_3_13h"]

    AB57 = V43+V45+V46+V48+V49+V50+V52+V54
    AB59 = AB38+AB39+AB40+AB41+AB42+AB57

    data_sch_3_21 = {
        "data_sch_3_21_1": AB10,
        "data_sch_3_21_2": AB12,
        "data_sch_3_21_3": AB13,
        "data_sch_3_21_4": AB14,
        "data_sch_3_21_5": AB15,
        "data_sch_3_21_6a": V17,
        "data_sch_3_21_6b": V18,
        "data_sch_3_21_6c": V19,
        "data_sch_3_21_6d": V20,
        "data_sch_3_21_6e": V21,
        "data_sch_3_21_6f": V22,
        "data_sch_3_21_6g": V23,
        "data_sch_3_21_6h": 0,
        "data_sch_3_21_6i": 0,
        "data_sch_3_21_6j": 0,
        "data_sch_3_21_6k": 0,
        "data_sch_3_21_6l": 0,
        "data_sch_3_21_6z": 0,
        "data_sch_3_21_7": AB31,
        "data_sch_3_21_8": AB33,
        "data_sch_3_21_9": AB38,
        "data_sch_3_21_10": AB39,
        "data_sch_3_21_11": AB40,
        "data_sch_3_21_12": AB41,
        "data_sch_3_21_13a": V43,
        "data_sch_3_21_13b": V45,
        "data_sch_3_21_13c": V46,
        "data_sch_3_21_13d": 0,
        "data_sch_3_21_13e": 0,
        "data_sch_3_21_13f": V50,
        "data_sch_3_21_13g": V52,
        "data_sch_3_21_13h": V54,
        "data_sch_3_21_13z": 0,
        "data_sch_3_21_14": AB57,
        "data_sch_3_21_15": AB59
    }

    print(json.dumps(data_sch_3_21,indent=3))

    return data_sch_3_21

get_sch3_data()