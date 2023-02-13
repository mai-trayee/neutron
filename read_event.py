# Read Text Files with Pandas using read_csv()
  
# importing pandas
import pandas as pd
  
# read text file into pandas DataFrame
column_names = ('rows', 'nscndprt','iprntprt','iprtscnd','lmecscnd','iorgprt','tscnd','pscnd') 
df = pd.read_table("event.txt", 
			sep="*", engine='python', 
			skiprows=2,
			header=None) 
			#names=column_names)
df = df.drop(columns=[0, 1, 10, 11])  
df.columns = column_names 
df = df.sort_values(
		by=['tscnd', 'pscnd'],
		ascending=[True, False]
		)

# display DataFrame
print(df.to_markdown())
