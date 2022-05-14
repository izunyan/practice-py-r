# 
print('hello, world')

# 日付
import datetime
date = datetime.datetime.today()
print(date)


# ライブラリインストールなど





# カレントディレクトリの確認と変更
import os
os.getcwd()

# os.chdir('C:\\name\\name2')


# csv読み込み
import pandas as pd
df = pd.read_csv('data/penguins.csv')
df.head()

# 変数名一覧
df.info()

# summary
df.describe()


# select
df[['species',	'bill_length_mm']].head()
