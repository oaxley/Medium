# jupyter_notebook_config.py
# Configuration file for the Jupyter Notebook

# retrieve the configuration
c = get_config()

# set the network config
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888

# does not open a browser upon start
c.NotebookApp.open_browser = False

# notebook working directory
c.NotebookApp.notebook_dir = '/home/jovyan'

# deactivate authentication
c.NotebookApp.password = ''
c.NotebookApp.password_required = False
c.NotebookApp.token = ''