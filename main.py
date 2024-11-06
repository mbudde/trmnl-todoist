import os
from dotenv import load_dotenv
import requests
from jinja2 import Environment, FileSystemLoader
from todoist_api_python.api import TodoistAPI
import datetime

DEBUG = False
user_filter_query = "today | overdue"

#===#
load_dotenv()

env_todoist_api_key = os.getenv('TODOIST_API')
todoist_api_key = TodoistAPI(env_todoist_api_key)
trmnl_api_key = os.getenv('TRMNL_API_KEY')
#trmnl_mac_address = os.getenv('TRMNL_DEVICE_MAC')
webhook_id = os.getenv('TRMNL_PLUGIN_ID')
trmnl_webhook_url = f"https://usetrmnl.com/api/custom_plugins/{webhook_id}"
#===#

# GET TODOIST DATA
try:
    filter_query = f'{user_filter_query}'
    tasks = todoist_api_key.get_tasks(filter=filter_query)
    if DEBUG: print(tasks)
except Exception as error:
    print(error)

# PARSE DATA
parsed_tasks = []
for index, task in enumerate(tasks, start=1):
    description = task.description if task.description else 'No description'
    content = task.content
    parsed_task = {
        'index': index,
        'content': content,
        'description': description,
        'due_date': task.due.date if task.due else None,
        'priority': task.priority
    }
    parsed_tasks.append(parsed_task)

# Sort by priority (p4 = highest in Todoist)
parsed_tasks.sort(key=lambda x: x['priority'], reverse=True)

tasks = parsed_tasks
if DEBUG: print(tasks)

# SEND DATA TO WEBHOOK
try:
    response = requests.post(
        trmnl_webhook_url,
        json={'merge_variables': {'tasks': tasks, 'todoist_query': user_filter_query}},
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {trmnl_api_key}'
        }
    )
    response.raise_for_status()
    current_timestamp = datetime.datetime.now().isoformat()
    print(f"Tasks sent successfully to TRMNL at {current_timestamp}")
except Exception as error:
    print(error)
    