from instructions import *
from form_7202_21 import *
from form_sch3_21 import *
from test import instructions_variables_20, instructions_variables_21, old_intake_data
from datetime import datetime, timedelta
import json


data_sch_3_21 = get_sch3_data()

def get_1040_data():    
    AB35 = instructions_21["N72"]
    M36 = instructions_21["N73"]
    M37 = instructions_21["N74"]
    M38 = instructions_21["N75"]
    M39 = instructions_21["N76"]
    M40= instructions_21["N77"]
    AB36 = instructions_21["N78"]
    AB37 = instructions_21["N112"]
    AB38 = instructions_21["N80"]
    AB39 = instructions_21["N81"]
    AB40 = instructions_21["N82"]
    AB41 = instructions_21["N113"]
    AB42 = instructions_21["N104"]
    AB43 = instructions_21["N105"]
    AB44 = instructions_21["N85"]
    AB45 = instructions_21["N40"]
    X46 = instructions_21["N120"] if instructions_21["N120"] > 0 else instructions_21["N106"] + instructions_21["N41"]
    X47 = instructions_21["N86"]
    AB48 = X46+X47
    AB49 = instructions_21["N37"]
    AB50 = AB48+AB49
    AB51 = instructions_21["N107"]
    AB54 = instructions_21["N114"]
    AB55 = instructions_21["N108"]+instructions_21["N109"]
    AB56 = AB54+AB55
    AB57 = instructions_21["N88"]
    AB58 = data_sch_3_21["data_sch_3_21_8"]
    AB59 = AB57+AB58
    AB60 = 0 if AB56 - AB59 < 0 else AB56 - AB59
    AB61 = instructions_21["N110"]
    AB62 = AB60+AB61
    X64 = 0
    X65 = 0
    X66 = 0
    AB67 = instructions_21["N45"]
    AB68 = instructions_21["N46"]
    X69 = instructions_21["N115"]
    S73 = instructions_21["N116"]
    S74 = 0
    X75 = instructions_21["N117"]
    X76 = instructions_21["N118"]
    X77 = instructions_21["N71"]
    X78 = data_sch_3_21["data_sch_3_21_15"]
    AB79 = X69+X75+X76+X77+X78
    AB80 = AB67+AB68+AB79
    AB81 = AB80 - AB62 if AB80 > AB62 else 0
    AB82 = AB81
    AB86 = AB62 - AB80 if AB81 == 0 else 0
    U85 = 0
    U87 = instructions_21["N92"]

    data_1040_21 = {
        "data_1040_21_1": AB35,
        "data_1040_21_2a": M36,
        "data_1040_21_2b": AB36,
        "data_1040_21_3a": M37,
        "data_1040_21_3b": AB37,
        "data_1040_21_4a": M38,
        "data_1040_21_4b": AB38,
        "data_1040_21_5a": M39,
        "data_1040_21_5b": AB39,
        "data_1040_21_6a": M40,
        "data_1040_21_6b": AB40,
        "data_1040_21_7": AB41,
        "data_1040_21_8": AB42,
        "data_1040_21_9": AB43,
        "data_1040_21_10": AB44,
        "data_1040_21_11": AB45,
        "data_1040_21_12a": X46,
        "data_1040_21_12b": X47,
        "data_1040_21_12c": AB48,
        "data_1040_21_13": AB49,
        "data_1040_21_14": AB50,
        "data_1040_21_15": AB51,
        "data_1040_21_16": AB54,
        "data_1040_21_17": AB55,
        "data_1040_21_18": AB56,
        "data_1040_21_19": AB57,
        "data_1040_21_20": AB58,
        "data_1040_21_21": AB59,
        "data_1040_21_22": AB60,
        "data_1040_21_23": AB61,
        "data_1040_21_24": AB62,
        "data_1040_21_25a": X64,
        "data_1040_21_25b": X65,
        "data_1040_21_25c": X66,
        "data_1040_21_25d": AB67,
        "data_1040_21_26": AB68,
        "data_1040_21_27a": X69,
        "data_1040_21_27b": S73,
        "data_1040_21_27c": S74,
        "data_1040_21_28": X75,
        "data_1040_21_29": X76,
        "data_1040_21_30": X77,
        "data_1040_21_31": X78,
        "data_1040_21_32": AB79,
        "data_1040_21_33": AB80,
        "data_1040_21_34": AB81,
        "data_1040_21_35a": AB82,
        "data_1040_21_36": U85,
        "data_1040_21_37": AB86,
        "data_1040_21_38": U87
    }

    print(json.dumps(data_1040_21,indent=3))
    return data_1040_21

get_1040_data()
