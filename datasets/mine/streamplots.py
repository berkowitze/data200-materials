import matplotlib.pyplot as plt
import math
import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.cm as cm

odf = pd.read_csv('stream-data.csv')
df = odf.dropna(subset=['STREAM TEMP'])
df.DATE = pd.to_datetime(df.DATE)
df.year = df.DATE.apply(lambda r: r.year)
df.crd = df['DISCHARGE'].apply(lambda x: x**(1./3))
numb_year_bins = 7
start, stop = float(df.year.min()), float(df.year.max())
df.year_bin = ((df.year - start) / (stop - start) * (numb_year_bins - 1)).apply(math.floor)



def rgb(r, g, b):
    return (r/255., g/255., b/255.)

ys = mdates.YearLocator()
ys_fmt = mdates.DateFormatter('%Y')
ms_fmt = mdates.MonthLocator()
fig, ax = plt.subplots(figsize=(10, 5))


ax.plot('DATE', 'STREAM TEMP', data=df, linewidth=1)

ax.xaxis.set_major_locator(ys)
ax.xaxis.set_major_formatter(ys_fmt)
# ax.xaxis.set_minor_locator(ms_fmt)

plt.ylabel('Stream Temperature ($^oC$)', fontsize=14)
plt.title('Plot C', fontsize=16)
dates = df.DATE
ax.set_xlim(dates.iloc[0], dates.iloc[-1])

ax.format_xdata = mdates.DateFormatter('%m/%d/%y')
ax.grid(True)

ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
_, labels = plt.xticks()
plt.setp(labels, rotation=90)
# fig.autofmt_xdate()
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)
plt.savefig('temp-timeseries', bbox_inches='tight')
plt.show()

ax = plt.gca()
# ax.scatter(df['STREAM HEIGHT'], df['DISCHARGE'], s=1, c=(0., 107./255, 164./255))
ax.scatter(df['STREAM HEIGHT'], df['DISCHARGE'], s=1,
           c=df.year_bin,
           cmap=cm.get_cmap('hsv'))
plt.legend()
ax.grid(True, c=rgb(230, 230, 230))
ax.set_axisbelow(True)
plt.xlabel('Stream height (cm)', fontsize=14)
plt.ylabel('Stream discharge [volume per second] $(m^3/s)$', fontsize=12)
plt.title('Plot B', fontsize=16)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
plt.tick_params(axis="both", which="both", bottom="off", top="off",
                labelbottom="on", left="off", right="off", labelleft="on")
# plt.savefig('height-vs-discharge.png', bbox_inches='tight')

plt.show()

fig, ax = plt.subplots()
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# plt.xticks(fontsize=14)
# plt.yticks(range(5000, 30001, 5000), fontsize=14)
plt.xlabel('Stream Temperature ($^oC$)', fontsize=14)
plt.ylabel('Count (# days)', fontsize=14)
plt.title('Plot A', fontsize=16)
ax.set_xticks(list(range(-6, 33, 3)))
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
plt.tick_params(axis='y', which='both', left=False, right=False, labelleft=True)
ax.yaxis.grid(True, c=rgb(210, 210, 210), alpha=0.5)
ax.hist(df['STREAM TEMP'], edgecolor='black',
        bins=range(-6, 33, 3), color='#3F5D7D')
plt.savefig('temp-hist.png', bbox_inches='tight')
plt.show()
