import matplotlib.pyplot as plt  # type: ignore
import matplotlib
matplotlib.use('TkAgg')
from log_bash_history import HistoryAnalyzer

def plot_cmd():
    cmd = HistoryAnalyzer()
    cmd._get_()

    git_count = cmd.git_counter
    cmd_count = cmd.cd_counter 

    values_for_git = git_count
    values_for_cmd = cmd_count

    plt.bar(['Git', 'CMD'], [values_for_git, values_for_cmd], color='blue')
    plt.xlabel('Command Type')
    plt.ylabel('Count')
    plt.title('Comparison of Git and CMD Commands')
    plt.show()

if __name__ == "__main__":
    plot_cmd()