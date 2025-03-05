#!/usr/bin/env python
# coding: utf-8

# Notebook to create new html pages

# In[8]:


from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import json


# In[9]:


TEMPLATE_PATH = Path("templates")
HOSTING_PATH = Path("all_events")
environment = Environment(
    loader=FileSystemLoader(TEMPLATE_PATH),
    extensions=["jinja2.ext.loopcontrols", "jinja2.ext.do"],
)


# In[10]:


with open('event_details.json', 'r') as f:
    details = json.load(f)


# In[11]:


# YYYY/MM/DD format
start_date = details['start_date']
start_time = details['time']
start_date_time_str = f"{start_date} {start_time}"
start_date_datetime = datetime.strptime(start_date_time_str, "%Y/%m/%d %H:%M")

# Parse the end date (only the date is considered)
end_date = details['end_date']
end_date_datetime = datetime.strptime(end_date, "%Y/%m/%d")

# Extract the year from the end_date
event_year = end_date_datetime.year

# Generate the HTML page name using the event year
html_page_name = f"{event_year}.html"


# In[12]:


page_template = environment.get_template("landingpage.html")
template_level = html_page_name.count("/")
page_html_path = html_page_name
page_content = page_template.render(
    TEMPLATE_LEVEL=template_level,
    start_date=start_date_datetime,
    end_date=end_date_datetime,
    event_year=event_year,
    details=details
)
with open(page_html_path, mode="w", encoding="utf-8") as page:
    page.write(page_content)


# In[13]:


# import time
# from datetime import datetime

# # Target date and time
# target_date_str = "2025/03/17 09:00"  # Format: YYYY/MM/DD HH:MM
# target_date = datetime.strptime(target_date_str, "%Y/%m/%d %H:%M")

# # Countdown logic
# while True:
#     # Get the current date and time
#     now = datetime.now()

#     # Calculate the time remaining
#     time_remaining = target_date - now

#     if time_remaining.total_seconds() <= 0:
#         print("Countdown Complete!")
#         break

#     # Extract days, hours, minutes, and seconds
#     days = time_remaining.days
#     hours, remainder = divmod(time_remaining.seconds, 3600)
#     minutes, seconds = divmod(remainder, 60)

#     # Display the countdown
#     print(f"Countdown: {days}d {hours}h {minutes}m {seconds}s", end="\r")

#     # Wait for 1 second before updating
#     time.sleep(1)


# In[14]:


page_template = environment.get_template("index_template.html")
template_level = html_page_name.count("/")
index_html_path = "index.html"
index_page_content = page_template.render(
    TEMPLATE_LEVEL=template_level,
    current_year=event_year
)
with open(index_html_path, mode="w", encoding="utf-8") as index_page:
    index_page.write(index_page_content)

