# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=',', skip_header=1)
print(data, data.shape)

census = np.concatenate((data, np.array(new_record)), axis=0)
print(census, census.shape)


# --------------
#Code starts here
age = census[:,0]
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = age.std()

print('Max age = {} \n Min age = {} \n mean age = {} \n std deviation = {}'.format(max_age, min_age, age_mean, age_std))


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
len_0 = len(race_0)

race_1 = census[census[:,2]==1]
len_1 = len(race_1)

race_2 = census[census[:,2]==2]
len_2 = len(race_2)

race_3 = census[census[:,2]==3]
len_3 = len(race_3)

race_4 = census[census[:,2]==4]
len_4 = len(race_4)

minority = min(len_0, len_1, len_2, len_3, len_4)
if minority==len_0:
    minority_race = 0
elif minority==len_1:
    minority_race = 1
elif minority==len_2:
    minority_race = 2
elif minority==len_3:
    minority_race = 3
elif minority==len_4:
    minority_race = 4

print(minority_race)




# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
working_hours_sum = senior_citizens[:,6].sum()
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours, avg_working_hours<=25)


# --------------
#Code starts here
high = census[census[:, 1]>10]
low = census[census[:, 1]<=10]

avg_pay_high = high.mean(axis=0)[7]
avg_pay_low = low.mean(axis=0)[7]

print(avg_pay_high, avg_pay_low)


