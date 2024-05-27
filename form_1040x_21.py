from instructions import *
from form_7202_21 import *
from form_sch3_21 import *
from form_1040_21 import *
from test import instructions_variables_20, instructions_variables_21, old_intake_data
from datetime import datetime, timedelta
import json

data_1040_21 = get_1040_data()
data_7202_21 = get_7202_data(instructions_20, instructions_21, intake_data)
data_sch_3_21 = get_sch3_data()



def get_1040x_data():
    K12 = instructions_21["N40"]
    S12 = K12
    K13 = max(instructions_21["N41"], instructions_21["N120"]) if max(instructions_21["N41"], instructions_21["N120"]) > 0 else 0
    S13 = K13
    K14 = K12-K13
    S14 = K14
    K15 = 0
    S15 = 0
    K16 = instructions_21["N37"]
    S16 = K16
    K17 = K14-K16
    S17 = K17
    K18 = instructions_21["N42"]
    S18 = K18
    K19 = instructions_21["N43"]
    S19 = K19
    K20 = K18-K19
    S20 = K20
    K21 = 0
    S21 = 0
    K22 = data_1040_21["data_1040_21_23"]
    S22 = K22
    K23 = data_1040_21["data_1040_21_24"]
    S23 = K23
    K24 = data_1040_21["data_1040_21_25d"]
    S24 = K24
    K25 = data_1040_21["data_1040_21_26"]
    S25 = K25
    K26 = data_1040_21["data_1040_21_27a"]
    S26 = K26

    J39 = data_1040_21["data_1040_21_28"]
    J40 = data_1040_21["data_1040_21_29"]
    J41 = data_1040_21["data_1040_21_30"]
    J42 = data_sch_3_21["data_sch_3_21_15"]

    AI81_1040_21 = 0 if data_1040_21["data_1040_21_34"] - data_7202_21["data_7202_21_sch_3_13b"] - data_7202_21["data_7202_21_sch_3_13h"] <=0 else data_1040_21["data_1040_21_34"] - data_7202_21["data_7202_21_sch_3_13b"] - data_7202_21["data_7202_21_sch_3_13h"]

    if AI81_1040_21 == 0:
        AI86_1040_21 = data_1040_21["data_1040_21_24"] - data_1040_21["data_1040_21_33"] + data_7202_21["data_7202_21_sch_3_13b"] + data_7202_21["data_7202_21_sch_3_13h"] + data_1040_21["data_1040_21_38"]
    else:
        AI86_1040_21 = 0

    print(AI86_1040_21)
    AI87_1040_21 = data_1040_21["data_1040_21_38"]

    J44 = 0 if AI86_1040_21 <= 0 else AI86_1040_21
    J45 = 0 if AI86_1040_21 <= 0 else data_1040_21["data_1040_21_38"]
    J49 = 0

    print(J44, J45, J49)

    K27 = J39+J40+J41
    O27 = data_7202_21["data_7202_21_sch_3_13b"] + data_7202_21["data_7202_21_sch_3_13h"]
    S27 = K27+O27
    S28 = 0 if J44-J45+J49 <= 0 else J44-J45+J49
    S29 = S24+S25+S26+S27+S28
    S30 = 0 if AI81_1040_21 == 0 else AI81_1040_21 - AI87_1040_21
    S31 = S29-S30
    S32 = S23 - S31 if S23 > S31 else 0
    S33 = S31 - S23 if S23 < S31 else 0
    S34 = S33 if S33 > 0 else 0
    M35 = 0

    data_1040x_21 = {
        "data_1040x_21_original_1": K12,
        "data_1040x_21_correct_1": S12,
        "data_1040x_21_original_2": K13,
        "data_1040x_21_correct_2": S13,
        "data_1040x_21_original_3": K14,
        "data_1040x_21_correct_3": S14,
        "data_1040x_21_original_4a": K15,
        "data_1040x_21_correct_4a": S15,
        "data_1040x_21_original_4b": K16,
        "data_1040x_21_correct_4b": S16,
        "data_1040x_21_original_5": K17,
        "data_1040x_21_correct_5": S17,
        "data_1040x_21_original_6": K18,
        "data_1040x_21_correct_6": S18,
        "data_1040x_21_original_7": K19,
        "data_1040x_21_correct_7": S19,
        "data_1040x_21_original_8": K20,
        "data_1040x_21_correct_8": S20,
        "data_1040x_21_original_9": K21,
        "data_1040x_21_correct_9": S21,
        "data_1040x_21_original_10": K22,
        "data_1040x_21_correct_10": S22,
        "data_1040x_21_original_11": K23,
        "data_1040x_21_correct_11": S23,
        "data_1040x_21_original_12": K24,
        "data_1040x_21_correct_12": S24,
        "data_1040x_21_original_13": K25,
        "data_1040x_21_correct_13": S25,
        "data_1040x_21_original_14": K26,
        "data_1040x_21_correct_14": S26,
        "data_1040x_21_original_15": K27,
        "data_1040x_21_correct_15": S27,
        "data_1040x_21_change_15": O27,
        "data_1040x_21_correct_16": S28,
        "data_1040x_21_correct_17": S29,
        "data_1040x_21_correct_18": S30,
        "data_1040x_21_correct_19": S31,
        "data_1040x_21_correct_20": S32,
        "data_1040x_21_correct_21": S33,
        "data_1040x_21_correct_22": S34,
        "data_1040x_21_23": M35,
        "data_1040x_21_28": J39,
        "data_1040x_21_29": J40,
        "data_1040x_21_30": J41,
        "data_1040x_21_31": J42,
        "data_1040x_21_37": J44,
        "data_1040x_21_38": J45,
        "data_1040x_21_org_sch_3_10": J49
    }

    print(json.dumps(data_1040x_21,indent=3))

get_1040x_data()


