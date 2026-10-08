import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=UserWarning)

from langchain_community.tools import ShellTool

shell_tool = ShellTool()

print(shell_tool.invoke('echo "Hi from shell tool"'))