import os 

class HistoryAnalyzer:
    def __init__(self):
        self.git_counter = 0
        self.cd_counter = 0 
    def _get_(self):
        # File path where bash history is located 
        bash_history = os.path.join(os.path.expanduser("~"), '.bash_history')

        with open(bash_history, 'r') as history_file:
            for cmd_line in history_file:
                if cmd_line.startswith("git"):
                    self.git_counter += 1 
                elif cmd_line.startswith("cd"):
                    self.cd_counter += 1 
        


