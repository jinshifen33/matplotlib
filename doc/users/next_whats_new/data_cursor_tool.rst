Added Data Cursor Tool for ToolManager
--------------------------------------

A new tool has been added for use by the ToolManager that allows for data
selection with annotations. For the moment, the Data Cursor tool only
supports scatter(), bar() and plot(). Extending the Data Cursor tool is
coming soon.

To add this tool to `ToolManager`

 >>> fig.canvas.manager.toolmanager.add_tool('DataCursor', ToolDataCursor)

To add it to the toolbar inside the group 'foo'

 >>> fig.canvas.manager.toolbar.add_tool('DataCursor', 'foo')

An example of this feature is provided at
`~matplotlib/examples/user_interfaces/data_cursor_demo.py`