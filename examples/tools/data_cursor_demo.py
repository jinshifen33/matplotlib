import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backend_tools import ToolDataCursor
from matplotlib.backend_managers import ToolManager

matplotlib.rcParams['toolbar'] = 'toolmanager'

fig = plt.figure()
manager = ToolManager(fig)

fig.canvas.manager.toolmanager.add_tool('ToolDataCursor', ToolDataCursor)
fig.canvas.manager.toolbar.add_tool('ToolDataCursor', 'zoompan')

ax = fig.add_subplot(111)
x = np.arange(5)
y = np.array([1,9,3,6,2])
y2 = np.array([3,2,5,1,4])
line, = ax.plot(x, y, label='l1', picker=5)
line, = ax.plot(x, y2, label='l2', picker=5)

plt.show()
