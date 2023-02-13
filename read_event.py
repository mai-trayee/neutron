# Read Text Files with Pandas using read_csv()
  
# importing pandas
import pandas as pd
  
# read text file into pandas DataFrame
column_names = ('rows', 'nscndprt','iprntprt','iprtscnd','lmecscnd','iorgprt','tscnd','pscnd','pprnt','pprntinit') 
df = pd.read_table("event.txt", 
			sep="*", engine='python', 
			skiprows=2,
			header=None) 
			#names=column_names)
df = df.drop(columns=[0, 1, 12])  
df.columns = column_names 
df = df.sort_values(
		by=['tscnd', 'pscnd'],
		ascending=[True, False]
		)

dict_particle = {11 : 'e-',	-11 : 'e+',
	13 : 'mu-',	-13 : 'mu+',
	15 : 'tau-',	-15 : 'tau+', 
	22 : 'gamma',
	12 : 'nu_e',	-12 : 'anti-nu_e',
	14 : 'nu_mu',   -14 : 'anti-nu_mu',
	16 : 'nu_tau',  -16 : 'anti-nu_tau',
	2112: 'n',
	2212: 'p+',    -2212: 'p-',
	111: 'pi0',
	211: 'pi+',     -211: 'pi-',
	221: 'eta',
	311: 'K0',
	321: 'K+',	-321: 'K-'}

dict_process = { 1: 'boundary',
		 5: 'decay',
		18: 'ncapture',
		 6: 'pair production',
		20: 'hadronic inelastic'}


df=df.replace({'iprntprt': dict_particle})
df=df.replace({'iprtscnd': dict_particle})
df=df.replace({'iorgprt': dict_particle})

df=df.replace({'lmecscnd': dict_process})

print('Look for value:')
choice = [input()]
print('in column:')
df = df[df[input()].isin(choice)]


# display DataFrame
print(df.to_markdown())
