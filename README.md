# TRMNL Todoist Plugin

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/github/license/Nynir/trmnl-todoist)
![Issues](https://img.shields.io/github/issues/Nynir/trmnl-todoist)
![Stars](https://img.shields.io/github/stars/Nynir/trmnl-todoist)

<img src="https://www.svgrepo.com/download/306859/todoist.svg" alt="Todoist Logo" width="10%">

Unofficial Todoist plugin for TRMNL.

<img src="https://pbs.twimg.com/media/GbuhujzXEBQucP5?format=jpg&name=large" alt="Desk picture" width="50%">

## Details
This plugin operates using Todoist filters, which may require Todoist pro. 
You can edit the query run by changing the ``user_filter_query`` variable in `main.py`.

Tasks are sorted in order of Priority, from highest to lowest.

## Requirements
This code operates with the Todoist REST API and the TRMNL webhook API. You will have to run this code yourself in some capacity to push updated Todoist task queries to TRMNL at regular intervals.

## Setup
1. In TRMNL go to Plugins -> Private Plugin -> Add New. Give it a name, and select "Webhook" for the Strategy. Hit save.
2. Collect the Plugin UUID as well as your TRMNL API key.
3. Download the code and in the same folder as it, create a ``.env`` file, and populate like so:
```
TRMNL_API_KEY="<your api key>"
TODOIST_API="<your api key>"
TRMNL_PLUGIN_ID="<your plugin UUID>"
```
4. Take the code in ``template.html.j2`` and add it as the markup for your TRMNL plugin
5. Run ``main.py`` and if it successfully posts to TRMNL you should be set. You can force a refresh in TRMNL to see if the data populates.

From there, you can schedule the code to run at regular intervals to post to TRMNL based on your desired frequency.

# Disclaimer

This plugin is an unofficial project and is not affiliated with, endorsed by, or supported by Doist

<a href="https://www.buymeacoffee.com/nynir" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
