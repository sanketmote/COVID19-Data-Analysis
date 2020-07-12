
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
## dataset = corona_dataset_csv file
dataset = pd.read_csv("Data/covid19_confirmed_dataset.csv")

                        ## to print first 10 line of data from data19_confirmed_dataset.csv
                        ##print(dataset.head(10))
                        ##to print rows and column from data
                        ##print(dataset.shape)
##to drop useless columns
dataset.drop(["Lat","Long"],axis = 1,inplace=True)
##print(dataset)

##to aggregatting the rows by country
dataset_aggregrate = dataset.groupby("Country/Region").sum()
#*
##print(dataset_aggregrate)
#x = "India"
#dataset_aggregrate.loc["India"].plot()          ##to print specifis country name example india
#print(dataset_aggregrate.loc["Itely"])
#dataset_aggregrate.loc["China"].plot()
#plt.legend()
#plt.show()
#dataset_aggregrate.loc["China"][:3].plot()
#plt.show()

#################### calculating and plotting the 1st derivative of the curve

#dataset_aggregrate.loc["China"].diff().plot()
#plt.show()
##find max infection rate
#res = dataset_aggregrate.loc["China"].diff().max()
#print(res)

##find max infection in all country
countries = list(dataset_aggregrate.index)
#print(countries)
max_infetction_list = []
max_infetction_dict = {}
for c in countries:
    max =  dataset_aggregrate.loc[c].diff().max()
    max_infetction_list.append(max)
    max_infetction_dict.update({c:max})
    #print(c, ' : ', max_infetction_dict[c])
#print((key,':', max_infetction_dict[key]) for key in max_infetction_dict.items())
##print(max_infetction_dict)

               #to add max infected data in framedata
dataset_aggregrate["Max_infected_rate"] = max_infetction_list

#create a new dataset with needed  column

corona_data = pd.DataFrame(dataset_aggregrate['Max_infected_rate'])

#print(corona_data)

## happiness_data = corona_happiness_data_csv file
happiness_data = pd.read_csv("Data/worldwide_happiness_report.csv")

                        ## to print first 10 line of data from data19_confirmed_happiness_data.csv
                        ##print(happiness_data.head(10))
                        ##to print rows and column from data
                        ##print(happiness_data.shape)
##to drop useless columns
useless_list = ["Overall rank","Score","Generosity","Perceptions of corruption"]
happiness_data.drop(useless_list,axis = 1,inplace=True)
##print(happiness_data)

happiness_data.set_index(['Country or region'],inplace=True)
######print(happiness_data)

#to join Covid19 Data with happiness Data
data = happiness_data.join(corona_data).copy()
#print(data)

##yo correlation matrix

data.corr()

##to read data

print(data)
lst = open("data.txt","a")
for word in data:
    lst.write(word)
lst.close()
x = data['GDP per capita']
y = data['Max_infected_rate']
#####Various Graph with various data

#  1.

sns.scatterplot(x,np.log(y))
plt.show()

#2.

#sns.regplot(x,np.log(y))
#plt.show()

#3.

#x = data['Healthy life expectancy']
#y = data['Max_infected_rate']
#sns.scatterplot(x,np.log(y))
#plt.show()

#4.

#sns.regplot(x,np.log(y))
#plt.show()

#5.

#x = data['Freedom to make life choices']
#y = data['Max_infected_rate']
#sns.scatterplot(x,np.log(y))
#plt.show()

#6.

#sns.regplot(x,np.log(y))
#plt.show()

#7.

data.loc["India"].plot()
plt.legend()
plt.show()
