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
trmnl_mac_address = os.getenv('TRMNL_DEVICE_MAC')
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

MAX_TASKS = 5  # throttling otherwise it will extend into infinity

# PARSE DATA
parsed_tasks = []
for task in tasks:
    description = task.description if task.description else 'No description'
    if len(description) > 60:
        description = description[:60] + '...'
    content = task.content
    if len(content) > 60:
        content = content[:60] + '...'
    parsed_task = {
        'content': content,
        'description': description,
        'due_date': task.due.date if task.due else None,
        'priority': task.priority
    }
    parsed_tasks.append(parsed_task)

# Sort by priority (p4 = highest in Todoist)
parsed_tasks.sort(key=lambda x: x['priority'], reverse=True)

# Actual throttling
if len(parsed_tasks) > MAX_TASKS:
    additional_tasks_count = len(parsed_tasks) - (MAX_TASKS - 1) # Replacing the 4th task with an appending task
    parsed_tasks = parsed_tasks[:MAX_TASKS - 1]
    parsed_tasks.append({
        'content': f'...and {additional_tasks_count} more tasks',
        'description': '',
        'due_date': None,
        'priority': None 
    })

tasks = parsed_tasks
if DEBUG: print(tasks)

'''
# RENDER HTML
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html.j2')
html_output = template.render(tasks=tasks)
if DEBUG: print(html_output)
'''

# SEND DATA TO WEBHOOK
try:
    response = requests.post(
        trmnl_webhook_url,
        json={'merge_variables': {'tasks': tasks}},
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