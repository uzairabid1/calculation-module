from instructions import *
import json 

old_intake_data = {
"Child_April_1_2020_through_December_31_2020": "10",
"Email": "paulfabbri@yahoo.com",
"Child_January_1_2021_through_March_31_2021": "10",
"Gov_April_1_2021_through_September_30_2021": 10,
"Gov_January_1_2021_through_March_31_2021": 10,
"Gov_April_1_2020_through_December_31_2020": 10,
"Family_January_1_2021_through_March_31_2021": 0,
"Family_April_1_2020_through_December_31_2020": 0,
"Child_April_1_2021_through_September_30_2021": 10,
"Family_April_1_2021_through_September_30_2021": 0,
"First_Name": "Paul",
"Last_Name": "Fabbri",
"ClientId": "",
"Status": "Pending Calculations"
}


instructions_variables_21 = {
    "F8995 QUALIFIED BUSINESS INCOME DEDUCTION COMPUTER": 9279,
    "SELF EMPLOYMENT TAX DEDUCTION PER COMPUTER": 3615,
    "ADJUSTED GROSS INCOME": 63800,
    "ADJUSTED GROSS INCOME PER COMPUTER": 63800,
    "STANDARD DEDUCTION PER COMPUTER": 12550,
    "TENTATIVE TAX": 4447,
    "TOTAL CREDITS": 16,
    "SE TAX": 7229,
    "FEDERAL INCOME TAX WITHHELD": 0,
    "ESTIMATED TAX PAYMENTS": 0,
    "OTHER PAYMENT CREDIT": 0,
    "EARNED INCOME CREDIT": 0,
    "TOTAL PAYMENTS": 0,
    "BAL DUE/OVER PYMT USING TP FIG PER COMPUTER": 12310,
    "TOTAL QUALIFIED BUSINESS INCOME OR LOSS": 47546,
    "FILING STATUS": "MARRIED FILING SEPARATE",
    "SE INCOME PER COMPUTER": 47247,
    "Credit to your account": 0,
    "ACCOUNT BALANCE": 0,
    "ACCRUED INTEREST": 0,
    "TAXABLE INCOME": 41671,
    "TAX PER RETURN": 12310,
    "SCHEDULE 8812 ADDITIONAL CHILD TAX CREDIT": 0,
    "FORM 2439 REGULATED INVESTMENT COMPANY CREDIT1": 0,
    "FORM 4136 CREDIT FOR FEDERAL TAX ON FUELS PER COMPUTER1": 0,
    "TOTAL EDUCATION CREDIT AMOUNT PER COMPUTER": 0,
    "HEALTH COVERAGE TX CR": 0,
    "AMOUNT YOU OWE": 12310,
    "REFUND AMOUNT": 0,
    "SICK FAMILY LEAVE CREDIT AFTER 3-31-21": 0,
    "SICK FAMILY LEAVE CREDIT": 0,
    "PREMIUM TAX CREDIT AMOUNT": 0,
    "REFUNDABLE CREDITS PER COMPUTER": 0,
    "SCHEDULE 8812 ADDITIONAL CHILD TAX CREDIT PER COMPUTER1": 0,
    "RECOVERY REBATE CREDIT PER COMPUTER": 0,
    "WAGES, SALARIES, TIPS, ETC": 0,
    "TAX-EXEMPT INTEREST": 0,
    "QUALIFIED DIVIDENDS": 380,
    "TOTAL IRA DISTRIBUTIONS": 0,
    "TOTAL PENSIONS AND ANNUITIES": 0,
    "TOTAL SOCIAL SECURITY BENEFITS": 0,
    "TAXABLE INTEREST INCOME": 0,
    "ORDINARY DIVIDEND INCOME": 769,
    "TAXABLE IRA DISTRIBUTIONS": 0,
    "TAXABLE PENSION/ANNUITY AMOUNT": 0,
    "TAXABLE SOCIAL SECURITY BENEFITS PER COMPUTER": 0,
    "CAPITAL GAIN OR LOSS": 15485,
    "OTHER INCOME": 0,
    "TOTAL ADJUSTMENTS PER COMPUTER": 3615,
    "NON ITEMIZED CHARITABLE CONTRIBUTION PER COMPUTER": 300,
    "BUSINESS INCOME OR LOSS (SCHEDULE C)": 51161,
    "CHILD AND OTHER DEPENDENT CREDIT PER COMPUTER": 0,
    "EXCESS ADVANCE PREMIUM TAX CREDIT REPAYMENT AMOUNT1": 0,
    "SEC 965 TAX INSTALLMENT": 0,
    "CHILD & DEPENDENT CARE CREDIT": 0,
    "ESTIMATED TAX PENALTY": 0,
    "APPLIED TO NEXT YEAR'S ESTIMATED TAX": 0,
    "EARNED INCOME CREDIT NONTAXABLE COMBAT PAY": 0,
    "MAX DEFERRED TAX PER COMPUTER": 0,
    "EIC PRIOR YEAR EARNED INCOME": 0,
    "FOREIGN TAX CREDIT PER COMPUTER": 16,
    "EDUCATION CREDIT PER COMPUTER": 0,
    "RETIREMENT SAVINGS CNTRB CREDIT PER COMPUTER": 0,
    "RESIDENTIAL CLEAN ENERGY CREDIT PER COMPUTER": 0,
    "F3800, F8801 AND OTHER CREDIT AMOUNT": 0,
    "AMOUNT PAID WITH FORM 4868": 0,
    "EXCESS SOCIAL SECURITY & RRTA TAX WITHHELD": 0,
    "ADDITIONAL INCOME PER COMPUTER": 51161,
    "TOTAL INCOME PER COMPUTER": 67415,
    "ADDITIONAL STANDARD DEDUCTION PER COMPUTER": 0,
    "TAXABLE INCOME PER COMPUTER": 41671,
    "FORM 6251 ALTERNATIVE MINIMUM TAX PER COMPUTER": 0,
    "EXCESS ADVANCE PREMIUM TAX CREDIT REPAYMENT AMOUNT": 650,
    "TOTAL OTHER TAXES PER COMPUTER": 7229,
    "TAXABLE INTEREST INCOME": 0,
    "ORDINARY DIVIDEND INCOME": 0,
    "CAPITAL GAINS OR LOSS": 0,
    "TENTATIVE TAX PER COMPUTER": 4447,
    "EARNED INCOME CREDIT PER COMPUTER": 0,
    "SCHEDULE 8812 NONTAXABLE COMBAT PAY": 0,
    "SCHEDULE 8812 ADDITIONAL CHILD TAX CREDIT PER COMPUTER": 0,
    "REFUNDABLE EDUCATION CREDIT PER COMPUTER": 0,
    "TOTAL NET EARNINGS PER COMPUTER": 47247,
    "TOTAL ITEMIZED DEDUCTIONS PER COMPUTER": 0,
    "FORM 3800 GENERAL BUSINESS CREDITS PER COMPUTER": 0,
    "PRIOR YR MIN TAX CREDIT": 0,
    "ADOPTION CREDIT PER COMPUTER": 0,
    "CREDIT FOR ELDERLY AND DISABLED PER COMPUTER": 0,
    "F8910 ALTERNATIVE MOTOR VEHICLE CREDIT PER COMPUTER": 0,
    "F8936 ELECTRIC MOTOR VEHICLE CREDIT PER COMPUTER": 0,
    "FORM 8396 MORTGAGE CERTIFICATE CREDIT PER COMPUTER": 0,
    "FORM 4136 CREDIT FOR FEDERAL TAX ON FUELS PER COMPUTER": 0,
    "FORM 2439 REGULATED INVESTMENT COMPANY CREDIT": 0,
    "REFUNDABLE CHILD CARE CREDIT": 0
}


instructions_variables_20 = {
    "SE INCOME PER COMPUTER": 18680,
    "TOTAL NET EARNINGS PER COMPUTER": 18680
}

instructions_result_21 = get_tax_variables_2021(instructions_variables_21)
instructions_result_20 = get_tax_variables_2020(instructions_variables_20)
intake_data = get_intake_data(old_intake_data)
