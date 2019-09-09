# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print('='*50)
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID', axis=1)
null_values = banks.isnull().sum()
print(null_values)
bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True)
banks.isnull().sum()
#code ends here


# --------------
# Code starts here
avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount')



# code ends here



# --------------
# code starts here




loan_approved_se = banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].shape[0]
loan_approved_nse = banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].shape[0]
Loan_Status = 614
percentage_se = loan_approved_se*100/Loan_Status
percentage_nse = loan_approved_nse*100/Loan_Status
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)

big_loan_term = banks.loc[loan_term>=25, 'Loan_Amount_Term'].count()

print(big_loan_term)


# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()



# code ends here


