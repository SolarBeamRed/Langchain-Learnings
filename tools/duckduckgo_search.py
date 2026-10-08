import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

print('Tool description: ', search_tool.description)
print('Tool args: ', search_tool.args)

results = search_tool.invoke('Elder Scrolls VI News')
print('\nSearch query results for Elder Scrolls VI News:/n', results)
