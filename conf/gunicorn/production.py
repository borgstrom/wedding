"""
Wedding RSVP gunicorn config file
"""

import multiprocessing

proc_name = "weddingrsvp"
bind = "127.0.0.1:6100"
workers = 2
daemon = False
timeout = 300
