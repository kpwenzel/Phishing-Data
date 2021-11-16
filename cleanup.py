import pandas
#import plotly.express as px

pandas.set_option('display.max_rows', None) # This might crash your computer if you don't have at least 4 gb of memory
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

#serialclick = declicked.drop_duplicates(keep='last', subset='email')
#serialclick = declicked.duplicated(keep='last', subset='email').sum()
#amount = declicked.shape[0]
#serialclickactual = amount - serialclick

#print(final)
print()
#final.to_csv("out.csv")

totalpeople = 1743

finalskyward = final[final.type.str.startswith("Skyward")]
print("Amount of unique Skyward IP's: {0}".format(len(finalskyward)))
mobiledevices = ["iPhone", "Android"]
skywardsafari = finalskyward[finalskyward.useragent.str.contains("iPhone")]
print("Amount of safari skyward clicks: {0}".format(len(skywardsafari)))
skywardandroid = finalskyward[finalskyward.useragent.str.contains("Android")]
print("Amount of Android skyward clicks: {0}".format(len(skywardandroid)))
print("Amount of Mobile Skyward clicks: {0}".format(len(skywardandroid + skywardsafari)))
print()
skywardwindows = finalskyward[finalskyward.useragent.str.contains("Windows")]
print("Amount of Windows clicks: {0}".format(len(skywardwindows)))
skywardlinux = finalskyward[finalskyward.useragent.str.contains("Linux")]
print("Amount of Linux clicks: {0}".format(len(skywardlinux)))
print("Amount of Desktop and Laptop clicks: {0}".format(len(skywardwindows + skywardlinux)))
print()

clickrateperskyward = len(finalskyward) / totalpeople
print(clickrateperskyward * 100)
print()

finaldunkin = final[final.type.str.startswith("Dunkin")]
print("Amount of unique Dunkin IP's: {0}".format(len(finaldunkin)))
mobiledevices = ["iPhone", "Android"]
dunkinsafari = finaldunkin[finaldunkin.useragent.str.contains("iPhone")]
print("Amount of safari Dunkin clicks: {0}".format(len(dunkinsafari)))
dunkinandroid = finaldunkin[finaldunkin.useragent.str.contains("Android")]
print("Amount of Android Dunkin clicks: {0}".format(len(dunkinandroid)))
print("Amount of Mobile Dunkin clicks: {0}".format(len(dunkinandroid + dunkinsafari)))
print()
dunkinwindows = finaldunkin[finaldunkin.useragent.str.contains("Windows")]
print("Amount of Windows clicks: {0}".format(len(dunkinwindows)))
dunkinlinux = finaldunkin[finaldunkin.useragent.str.contains("Linux")]
print("Amount of Linux clicks: {0}".format(len(dunkinlinux)))
print("Amount of Desktop and Laptop clicks: {0}".format(len(dunkinwindows + dunkinlinux)))
print()

clickrateperdunkin = len(finaldunkin) / totalpeople
print(clickrateperdunkin * 100)
print()

serialclick = declicked.duplicated(keep='last', subset='email').sum()
amount = declicked.shape[0]
serialclickactual = amount - serialclick

print(serialclickactual)

skywardserialclick = finalskyward.duplicated(keep='last', subset='email').sum()
amount = finalskyward.shape[0]
skywardserialclickactual = amount - skywardserialclick

print(skywardserialclickactual)

dunkinserialclick = finaldunkin.duplicated(keep='last', subset='email').sum()
amount = finaldunkin.shape[0]
dunkinserialclickactual = amount - dunkinserialclick

print(dunkinserialclickactual)

print(skywardserialclickactual / 1743 * 100)

print(dunkinserialclickactual / 1743 * 100)