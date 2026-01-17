{
    "name": "Run Scheduler Per Second",
    "summary": """Run Scheduler Per Second""",
    "description": """
        Odoo sheduled action cannot be used to schedule a job in seconds interval. 
        i.e You cannot schedule a cron job to run every 5 seconds.

        This module enable running cron to the lowest time fragment. It is advisable to be use for quick and fast action that 
        will take less execution time

    """,
    "author": "PowerOn | Wapsol GmbH",
    "website": "https://simplify-erp.de/apps",
    "license": "OPL-1",
    "price": "10.0",
    "currency": "EUR",
    "images": ["static/description/main_screenshot.png"],
    "category": "Technical",
    "version": "18.0.0.1",
    "depends": ["base_setup"],
}
