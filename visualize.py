import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import config

def plot_core_distribution():
    # 1. Read the system metrics log file
    if not os.path.exists(config.LOG_FILE_PATH):
        print("Error: Metrics file not found! Please run main.py to generate data first.")
        return

    df = pd.read_csv(config.LOG_FILE_PATH)

    # 2. Configure graph aesthetics
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # 3. Bar Chart: Task distribution across CPU cores
    core_counts = df['Assigned_Core'].value_counts().sort_index()
    
    ax = sns.barplot(x=core_counts.index, y=core_counts.values, palette="viridis")
    
    # Labeling and titles
    plt.title("Intra-Node Load Balancing: Task Distribution Across CPU Cores", fontsize=14, fontweight='bold')
    plt.xlabel("CPU Core ID", fontsize=12)
    plt.ylabel("Number of Sensor Tasks Processed", fontsize=12)
    plt.xticks(fontsize=10)
    
    # Annotate bar heights
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.tight_layout()
    print("Visualization Ready! Rendering the graph...")
    plt.show()

if __name__ == "__main__":
    plot_core_distribution()