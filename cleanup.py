import pandas
pandas.set_option('display.max_rows', None)
data = pandas.read_csv("data.csv", low_memory=False)
print(list(data))
gglclck = data[data["type"].str.contains("Google Click")]
print(gglclck)