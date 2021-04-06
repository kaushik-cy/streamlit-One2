import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns

YPAD = 10
DAYS = 120
COLORS_AREA = ['#876cdd', '#6fe3d4']
COLORS_LINE = ['#bac7f2', '#e0e0e0']
COLORS_BG = '#414059'
ALPHA = 1.
DIMS = (25, 30)
LW = [1.25, 0.1]
GRID_HT = [7, 4]
GRID_HS = 1.5

ght = GRID_HT[0] + 3 * GRID_HT[1]

def plot_01(data_i, days = DAYS):
	grid_space = 0

	fig = plt.figure(figsize = DIMS)
	plt.subplots_adjust(left = 0.15, right = 0.9, top = 0.92, bottom = 0.08)
	gs = GridSpec(ght, 1, figure = fig, hspace = GRID_HS)
	
	ax = fig.add_subplot(gs[grid_space:grid_space + GRID_HT[0], :])
	ax.set_facecolor(COLORS_BG)
	sns.lineplot(data = data_i['Close'][-days:], color = COLORS_LINE[0], linewidth = LW[0])
	plt.xlabel('')
	plt.ylabel('Close Price', labelpad = YPAD)
	grid_space += GRID_HT[0]
	
	ax = fig.add_subplot(gs[grid_space:grid_space + GRID_HT[1], :])
	ax.set_facecolor(COLORS_BG)
	sns.lineplot(data = data_i['MACD'][-days:], color = COLORS_LINE[1], linewidth = LW[1])
	plt.fill_between(data_i.index[-days:],
	                 data_i['MACD'][-days:],
	                 0,
	                 color = COLORS_AREA[0],
	                 where = data_i['MACD'][-days:] < 0,
	                 interpolate = True,
	                 alpha = ALPHA)
	plt.fill_between(data_i.index[-days:],
	                 data_i['MACD'][-days:],
	                 0,
	                 color = COLORS_AREA[1],
	                 where = data_i['MACD'][-days:] >= 0,
	                 interpolate = True,
	                 alpha = ALPHA)
	plt.xlabel('')
	plt.ylabel('MACD', labelpad = YPAD)
	grid_space += GRID_HT[1]

	ax = fig.add_subplot(gs[grid_space:grid_space + GRID_HT[1], :])
	ax.set_facecolor(COLORS_BG)
	sns.lineplot(data = data_i['CCI'][-days:], color = COLORS_LINE[1], linewidth = LW[1])
	plt.fill_between(data_i.index[-days:],
	                 data_i['CCI'][-days:],
	                 0,
	                 color = COLORS_AREA[0],
	                 where = data_i['CCI'][-days:] < 0,
	                 interpolate = True,
	                 alpha = ALPHA)
	plt.fill_between(data_i.index[-days:],
	                 data_i['CCI'][-days:],
	                 0,
	                 color = COLORS_AREA[1],
	                 where = data_i['CCI'][-days:] >= 0,
	                 interpolate = True,
	                 alpha = ALPHA)
	plt.xlabel('')
	plt.ylabel('CCI', labelpad = YPAD)
	grid_space += GRID_HT[1]

	ax = fig.add_subplot(gs[grid_space:grid_space + GRID_HT[1], :])
	ax.set_facecolor(COLORS_BG)
	sns.lineplot(data = data_i['CMF'][-days:], color = COLORS_LINE[1], linewidth = LW[1])
	plt.fill_between(data_i.index[-days:],
	                 data_i['CMF'][-days:],
	                 0,
	                 color = COLORS_AREA[0],
	                 where = data_i['CMF'][-days:] < 0,
	                 interpolate = True,
	                 alpha = ALPHA)
	plt.fill_between(data_i.index[-days:],
	                 data_i['CMF'][-days:],
	                 0,
	                 color = COLORS_AREA[1],
	                 where = data_i['CMF'][-days:] >= 0,
	                 interpolate = True,
	                 alpha = ALPHA)
	plt.xlabel('')
	plt.ylabel('CMF', labelpad = YPAD)

	fig.align_ylabels()
	plt.close()
	return fig