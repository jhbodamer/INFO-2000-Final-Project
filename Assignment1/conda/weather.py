#John Bodamer
#This program plots precipitation levels in Athens, GA between 2000 and 2010

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read the CSV file into a DataFrame
df = pd.read_csv('data.csv', parse_dates=['DATE'])

#Set the date column as the index
df.set_index('DATE', inplace=True)

#Resample the data to a monthly average
monthly_data= df['HPCP'].resample('M').mean()

#Use seaborn to create a line plot
sns.lineplot(data.monthly_data)
plt.xlabel('Date')
plt.ylabel('Precipitation (inches)')
plt.titile('Athens, GA Rain Gauge')

#save the figure
plt.savefig('athens_rain_guage.png', dpi=300, bbox_inches='tight')
plt.show()
