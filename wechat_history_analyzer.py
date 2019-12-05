import pandas as pd
import matplotlib.pyplot as plt

WECHAT_HISTORY_FILE_PATH = './wechat_history_for_python_2019.12.05.csv'
WECHAT_HISTORY_PERSON_COLUMN = '微信帐号'
WECHAT_HISTORY_DATETIME_COLUMN = '日期'
WECHAR_HISTORY_PERSON1 = 'wechat_id_1'  # Configure your own WeChat ID here
WECHAR_HISTORY_PERSON2 = 'wechat_id_2'

root_dataframe = pd.read_csv(WECHAT_HISTORY_FILE_PATH)
person1_list = []
person2_list = []
for i in range(0, len(root_dataframe)):
    # format datetime to date
    root_dataframe[WECHAT_HISTORY_DATETIME_COLUMN][i] = root_dataframe[WECHAT_HISTORY_DATETIME_COLUMN][i][0:10]
    if root_dataframe[WECHAT_HISTORY_PERSON_COLUMN][i] == WECHAR_HISTORY_PERSON1:
        person1_list.append(root_dataframe[WECHAT_HISTORY_DATETIME_COLUMN][i])
    elif root_dataframe[WECHAT_HISTORY_PERSON_COLUMN][i] == WECHAR_HISTORY_PERSON2:
        person2_list.append(root_dataframe[WECHAT_HISTORY_DATETIME_COLUMN][i])
    else:
        print('unknown person, i=%d, name=%s' % (i, root_dataframe[WECHAT_HISTORY_PERSON_COLUMN][i]))

person1_dataframe = pd.DataFrame({'date': person1_list, 'sum': 1})
person2_dataframe = pd.DataFrame({'date': person2_list, 'sum': 1})

person1_date_grouped_dataframe = person1_dataframe.groupby('date', as_index=False).sum()
person2_date_grouped_dataframe = person2_dataframe.groupby('date', as_index=False).sum()

plt.figure(0, figsize=[14, 8])  # set figure size, 100 times
plt.title('title')
plt.xlabel('x')
plt.ylabel('y')
# set figure surrounding margin
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.15, top=0.9)
plt.xticks(rotation=60)
plt.bar(person1_date_grouped_dataframe['date'], person1_date_grouped_dataframe['sum'], color='red',)
plt.bar(person2_date_grouped_dataframe['date'], person2_date_grouped_dataframe['sum'], color='blue')
plt.show()
