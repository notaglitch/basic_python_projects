import argparse
import os
import json

TASK_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASK_FILE)