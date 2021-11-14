import pandas
#import plotly.express as px

pandas.set_option('display.max_rows', None)
data = pandas.read_csv("data.csv", low_memory=False)
#print(list(data))
#gglclck = data[data["type"].str.contains("Google Click")]
#print(gglclck)
clicktype = ["Dunkin Click", "Skyward Click"]
#uatype = ["NaN"]
dedupe = data.drop_duplicates(subset = ['email', 'ip'], keep=False)
declicked = dedupe[dedupe.type.isin(clicktype)]
#final = declicked[~declicked.useragent.isin(uatype)]
#final = declicked[declicked.useragent.str.startswith("Mozilla")]
final = declicked[~declicked['useragent'].isnull()]

print(final)
final.to_csv("out.csv")
