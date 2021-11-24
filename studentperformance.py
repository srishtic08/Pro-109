import csv
import pandas as pd
import random 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data)/len(data) 
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_sd_start,first_sd_end = mean - std_deviation, mean + std_deviation
second_sd_start,second_sd_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_sd_start,third_sd_end = mean - (3*std_deviation), mean + (3*std_deviation)

fig = ff.create_distplot([data],["result"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [first_sd_start, first_sd_start],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [first_sd_end, first_sd_end],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x = [second_sd_start, second_sd_start],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x = [second_sd_end, second_sd_end],y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 2"))

fig.show()
list_of_data_within_1_std_deviation = [result for result in data if result > first_sd_start and result < first_sd_end]
list_of_data_within_2_std_deviation = [result for result in data if result > second_sd_start and result < second_sd_end]
list_of_data_within_3_std_deviation = [result for result in data if result > third_sd_start and result < third_sd_end]

print("Mean of this data is {}".format(mean))
print("Standard deviation of this data is {}".format(std_deviation))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))

