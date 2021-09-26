import pandas as pd
import statistics
import csv
#change the things into MSM MSD AND MSE 
df = pd.read_csv("StudentsPerformance.csv")
PLOE = df["parental_level_of_education"].to_list()
MS = df["math score"].to_list()
#Mean for height and Weight
StudentPerformance_mean = statistics.mean(PLOE)
MathMean = statistics.mean(MS)
#Median for height and weight
StudentPerformance_median = statistics.median(PLOE)
MathMedian = statistics.median(MS)
#Mode for height and weight
StudentPerformance_mode  = statistics.mode(PLOE)
MathMode = statistics.mode(MS)
#Printing mean, median and mode to validate
print("Mean, Median and Mode of Parental level of education is {}, {} and {}".format(PLOE, PLOE, PLOE))
print("Mean, Median and Mode of Math score {}, {} and {} respectively".format(MS, MS, MS))

StudentPerformance_deviation = statistics.stdev(PLOE)
MathScore_deviation = statistics.stdev(MS)
#1, 2 and 3 Standard Deviations for height
PLOE_first_std_deviation_start, PLOE_first_std_deviation_end = PLOE-StudentPerformance_deviation, PLOE+StudentPerformance_deviation
PLOE_second_std_deviation_start, PLOE_second_std_deviation_end = PLOE-(2*StudentPerformance_deviation), PLOE+(2*StudentPerformance_deviation)
PLOE_third_std_deviation_start, PLOE_third_std_deviation_end = PLOE-(3*StudentPerformance_deviation), PLOE+(3*StudentPerformance_deviation)
#1, 2 and 3 Standard Deviations for weight
MS_first_std_deviation_start, MS_first_std_deviation_end = MS-MathScore_deviation, MS+MathScore_deviation
MS_second_std_deviation_start, MS_second_std_deviation_end = MS-(2*MathScore_deviation), MS+(2*MathScore_deviation)
MS_third_std_deviation_start, MS_third_std_deviation_end = MS-(3*MathScore_deviation), MS+(3*MathScore_deviation)
#Percentage of data within 1, 2 and 3 Standard Deviations for Height
PLOE_list_of_data_within_1_std_deviation = [result for result in PLOE if result > PLOE_first_std_deviation_start and result < PLOE_first_std_deviation_end]
PLOE_list_of_data_within_2_std_deviation = [result for result in PLOE if result > PLOE_second_std_deviation_start and result < PLOE_second_std_deviation_end]
PLOE_list_of_data_within_3_std_deviation = [result for result in PLOE if result > PLOE_third_std_deviation_start and result < PLOE_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for Weight
MS_list_of_data_within_1_std_deviation = [result for result in MS if result > MS_first_std_deviation_start and result < MS_first_std_deviation_end]
MS_list_of_data_within_2_std_deviation = [result for result in MS if result > MS_second_std_deviation_start and result < MS_second_std_deviation_end]
MS_list_of_data_within_3_std_deviation = [result for result in MS if result > MS_third_std_deviation_start and result < MS_third_std_deviation_end]
#Printing data for height and weight (Standard Deviation)
print("{}% of data for Parental level of education lies within 1 standard deviation".format(len(PLOE_list_of_data_within_1_std_deviation)*100.0/len(PLOE)))
print("{}% of data for Parental level of education lies within 2 standard deviations".format(len(PLOE_list_of_data_within_2_std_deviation)*100.0/len(PLOE)))
print("{}% of data for Parental level of education lies within 3 standard deviations".format(len(PLOE_list_of_data_within_3_std_deviation)*100.0/len(PLOE)))
print("{}% of data for Math Score lies within 1 standard deviation".format(len(MS_list_of_data_within_1_std_deviation)*100.0/len(MS)))
print("{}% of data for MAth Score lies within 2 standard deviations".format(len(MS_list_of_data_within_2_std_deviation)*100.0/len(MS)))
print("{}% of data for Math Score lies within 3 standard deviations".format(len(MS_list_of_data_within_3_std_deviation)*100.0/len(MS)))