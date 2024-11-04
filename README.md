# TRMNL Todoist Plugin
Unofficial Todoist plugin for TRMNL.
## Requirements
This code operates with the Todoist REST API and the TRMNL webhook API. You will have to run this code yourself in some capacity to push updated Todoist task queries to TRMNL at regular intervals.

You need:
1. To have this code running on a schedule to push updates
2. A TRMNL API key and a Todoist API key

## Setup
1. In TRMNL go to Plugins -> Private Plugin -> Add New. Give it a name, and select "Webhook" for the Strategy. Hit save.
2. Collect the Plugin UUID as well as your TRMNL API key
3. Download the code and in the same folder as it, create a ``.env`` file, and populate like so:
```
TRMNL_API_KEY="<your api key>"
TODOIST_API="<your api key>"
TRMNL_PLUGIN_ID="<your plugin UUID>"
```
4. Take the code in ``template.html.j2`` and add it as the markup for your TRMNL plugin
5. Run ``main.py`` and if it successfully posts to TRMNL you should be set. You can force a refresh in TRMNL to see if the data populates.

From there, you can schedule the code to run at regular intervals to post to TRMNL based on your desired frequency.

### Editing the Todoist query
This plugin operates using Todoist filters, which may require Todoist pro. You can edit the query run by changing the ``user_filter_query`` variable.

If you do so, you might also want to update the markup in TRMNL to reflect  the new filter being used.