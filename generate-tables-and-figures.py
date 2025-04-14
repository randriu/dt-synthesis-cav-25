import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib

import click

def plot_figure_3(file_path, generate_pgf, add_dtcontrol_depths):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    if generate_pgf:
        matplotlib.use("pgf")
        matplotlib.rcParams.update({
            "pgf.texsystem": "pdflatex",
            'font.family': 'serif',
            'text.usetex': True,
            'pgf.rcfonts': False,
        })

    rename_dict = {
            "maze-7": "maze-7",
            "maze-steps": "maze-steps",
            "3d_navigation": "3d",
            "blackjack": "blackjack",
            "frozenlake_4x4": "lake-4",
            "frozenlake_8x8": "lake-8",
            "frozenlake_12x12": "lake-12",
            "inventory_management": "inventory",
            "system_administrator_1": "sys-1",
            "system_administrator_2": "sys-2",
            "system_administrator_tree": "sys-tree",
            "tictactoe_vs_random": "tictactoe",
            "traffic_intersection": "traffic",
            "consensus-3-32": "consensus",
            "csma-2-4": "csma",
            "firewire-3": "firewire",
            "ij-10": "ij",
            "pacman": "pacman",
            "philosophers-4": "philos",
            "pnueli-zuck-3": "pnueli",
            "rabin-4": "rabin",
            "resource-gathering-5": "resource",
            "wlan-1-2": "wlan",
            "wlan-2-cost": "wlan"
        }
    
    filter_models = []
    # filter_models = ["wlan", "lake-4", "sys-2", "philos", "resource", "3d", "blackjack"]
    filter_models = ["wlan", "lake-4", "philos", "resource", "3d", "blackjack", "pnueli", "sys-1"]
    
    # Replace NaN values in 'best relative' column with 0
    df['best relative'] = df['best relative'].fillna(0)
    
    # Sort the DataFrame by 'model' and 'depth'
    df = df.sort_values(by=['model', 'max_depth'])

    # Filter out rows that have no value for column "dtcontrol nodes"
    df = df.dropna(subset=['dtcontrol nodes'])

    # df = df[df["max_depth"] <= 7]

    df['model'] = df['model'].str.replace('^omdt-|^qcomp-', '', regex=True)

    # Rename models according to the rename_dict
    df['model'] = df['model'].apply(lambda x: rename_dict[x] if x in rename_dict else x)

    # Remove rows from df that contain model names from filter_models
    df = df[~df['model'].isin(filter_models)]
    # df = df[df['model'].isin(filter_models)]

    max_depth = {}

    for model in df['model'].unique():
        model_df = df[df['model'] == model]
        max_depth[model] = model_df['max_depth'].max()
    
    # Create a dictionary to store the maximum depth for each model
    max_depth_reached = {}

    relarive_best_cutoff = 0.95
    
    # Filter the DataFrame to exclude rows where 'best relative' is 1.0 or higher depths after 1.0 is reached
    filtered_rows = []
    for _, row in df.iterrows():
        model = row['model']
        depth = row['max_depth']
        best_relative = row['best relative']
        
        if model not in max_depth_reached:
            max_depth_reached[model] = 0
        
        if max_depth_reached[model] == 0:
            filtered_rows.append(row)
            if best_relative >= relarive_best_cutoff:
                max_depth_reached[model] = depth
            if depth == max_depth[model]:
                max_depth_reached[model] = depth
        
    
    filtered_df = pd.DataFrame(filtered_rows)

    # Sort the DataFrame by 'model' and 'S'
    filtered_df = filtered_df.sort_values(by=['choices'])
    
    # Create a dictionary to store the dtcontrol nodes for each model
    dtcontrol_nodes = df.groupby('model')['dtcontrol nodes'].first().to_dict()
    
    # Create the bar plots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6.5), sharex=True, gridspec_kw={'height_ratios': [1, 1.2]})
    
    # Define colors for different depths
    colors = plt.cm.cividis_r(np.linspace(0.1, 1, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.twilight_shifted(np.linspace(0, 0.9, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.terrain_r(np.linspace(0, 0.9, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.cividis(np.linspace(0.1, 0.9, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.Greens(np.linspace(0.2, 1, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.Wistia(np.linspace(0.2, 1, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.YlGnBu(np.linspace(0.2, 0.9, len(filtered_df['max_depth'].unique())))

    colors = [[0.2, 0.2, 0.2], [0.4, 0.4, 0.4], [0.6, 0.6, 0.6], [0.8, 0.8, 0.8], [0.85, 1, 0.75], [0.65, 0.9, 0.6], [0.4, 0.8, 0.3], [0.25, 0.45, 0.1]]
    
    # Upper plot: Relative values
    bar_width = 0.4
    index = np.arange(len(filtered_df['model'].unique()))

    model_space_width = 1.5
    bar_space_width = 0.0
    
    # Create a mapping from model names to their indices
    model_indices = {model: i for i, model in enumerate(filtered_df['model'].unique())}
    model_bars_offset = {}

    # Compute the first large model
    first_large_model = filtered_df[filtered_df['choices'] >= 3000].iloc[0]['model']

    prev_models = []

    for model in model_indices.keys():
        model_bars_offset[model] = 0
        for prev_model in prev_models:
            model_bars_offset[model] += max_depth_reached[prev_model]
        prev_models.append(model)
    
    # Plot bars for each depth
    for depth, color in zip(sorted(filtered_df['max_depth'].unique()), colors):
        depth_df = filtered_df[filtered_df['max_depth'] == depth]
        ax1.bar(
            [model_indices[model] * model_space_width + (model_bars_offset[model] + depth) * (bar_width+bar_space_width) + bar_space_width for index, model in enumerate(depth_df['model'])],
            depth_df['best relative'],
            bar_width,
            label=f'Depth {depth}',
            color=color
        )
    
    ax1.set_ylabel('Normalised Value', fontsize=14)
    ax1.set_ylim(0, 1)
    # ax1.legend(title='', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.yaxis.grid(True, linestyle='--')
    ax1.set_axisbelow(True)
    ax1.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are off
    
    # Add a vertical line to separate smaller and larger models
    ax1.axvline(x=model_indices[first_large_model] * model_space_width + (model_bars_offset[first_large_model] * bar_width+bar_space_width) - bar_width, color='black', linestyle='--')
    
    # Lower plot: Tree nodes (logarithmic scale)
    for depth, color in zip(sorted(filtered_df['max_depth'].unique()), colors):
        depth_df = filtered_df[filtered_df['max_depth'] == depth]
        ax2.bar(
            [model_indices[model] * model_space_width + (model_bars_offset[model] + depth) * (bar_width+bar_space_width) + bar_space_width for index, model in enumerate(depth_df['model'])],
            depth_df['tree nodes'],
            bar_width,
            label=f'Depth {depth}',
            color=color
        )
    
    # Plot dtcontrol nodes
    for model, idx in model_indices.items():
        ax2.bar(
            model_indices[model] * model_space_width + (model_bars_offset[model] + max_depth_reached[model]+1) * (bar_width+bar_space_width) + bar_space_width,
            dtcontrol_nodes[model],
            bar_width,
            label='DTControl' if idx == 0 else "",
            color='sandybrown'
        )

        if add_dtcontrol_depths:
            # Annotate dtcontrol bars with the value of "dtcontrol depth"
            dtcontrol_depth = df[df['model'] == model]['dtcontrol depth'].values[0]
            if model in ["consensus"]:
                ax2.text(
                model_indices[model] * model_space_width + (model_bars_offset[model] + max_depth_reached[model]+1) * (bar_width+bar_space_width) + bar_space_width + 0.8,
                dtcontrol_nodes[model]-32,
                f'({dtcontrol_depth})',
                ha='center',
                va='bottom',
                fontsize=10,
                color='black'
                )
            elif model in ["rabin"]:
                ax2.text(
                model_indices[model] * model_space_width + (model_bars_offset[model] + max_depth_reached[model]+1) * (bar_width+bar_space_width) + bar_space_width + 0.7,
                dtcontrol_nodes[model]-1,
                f'({dtcontrol_depth})',
                ha='center',
                va='bottom',
                fontsize=10,
                color='black'
                )
            else:
                ax2.text(
                model_indices[model] * model_space_width + (model_bars_offset[model] + max_depth_reached[model]+1) * (bar_width+bar_space_width) + bar_space_width + 0.1,
                dtcontrol_nodes[model],
                f'({dtcontrol_depth})',
                ha='center',
                va='bottom',
                fontsize=10,
                color='black'
                )
        
    
    ax2.set_ylabel('Tree Decision Nodes (log scale)', fontsize=14)
    ax2.set_yscale('log', base=2)
    ax2.set_xticks([model_indices[model] * model_space_width + (model_bars_offset[model]) * (bar_width+bar_space_width) + bar_space_width + ((max_depth_reached[model]+2)/2 * (bar_width+bar_space_width)) for index, model in enumerate(filtered_df['model'].unique())])
    ax2.set_xticklabels(filtered_df['model'].unique(), rotation=45, ha='right')
    ax2.yaxis.grid(True, linestyle='--')
    ax2.set_axisbelow(True)
    ax2.legend(title='', bbox_to_anchor=(0.95, 1.05), loc='upper left', framealpha=1, facecolor='white')

    ax2.axvline(x=model_indices[first_large_model] * model_space_width + (model_bars_offset[first_large_model] * bar_width+bar_space_width) - bar_width, color='black', linestyle='--')
    
    # plt.tight_layout()
    # plt.show()
    if generate_pgf:
        plt.savefig('results/generated-results/figure-3.pgf')
    else:
        fig.savefig('results/generated-results/figure-3.pdf', bbox_inches='tight')



def plot_figure_5(file_path, generate_pgf, add_dtcontrol_depths):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    if generate_pgf:
        matplotlib.use("pgf")
        matplotlib.rcParams.update({
            "pgf.texsystem": "pdflatex",
            'font.family': 'serif',
            'text.usetex': True,
            'pgf.rcfonts': False,
        })

    rename_dict = {
            "maze-7": "maze-7",
            "maze-steps": "maze-steps",
            "3d_navigation": "3d",
            "blackjack": "blackjack",
            "frozenlake_4x4": "lake-4",
            "frozenlake_8x8": "lake-8",
            "frozenlake_12x12": "lake-12",
            "inventory_management": "inventory",
            "system_administrator_1": "sys-1",
            "system_administrator_2": "sys-2",
            "system_administrator_tree": "sys-tree",
            "tictactoe_vs_random": "tictactoe",
            "traffic_intersection": "traffic",
            "consensus-3-32": "consensus",
            "csma-2-4": "csma",
            "firewire-3": "firewire",
            "ij-10": "ij",
            "pacman": "pacman",
            "philosophers-4": "philos",
            "pnueli-zuck-3": "pnueli",
            "rabin-4": "rabin",
            "resource-gathering-5": "resource",
            "wlan-1-2": "wlan",
            "wlan-2-cost": "wlan"
        }
    
    filter_models = []
    # filter_models = ["wlan", "lake-4", "sys-2", "philos", "resource", "3d", "blackjack"]
    # filter_models = ["wlan", "lake-4", "philos", "resource", "3d", "blackjack", "pnueli", "sys-1"]
    
    # Replace NaN values in 'best relative' column with 0
    df['best relative'] = df['best relative'].fillna(0)
    
    # Sort the DataFrame by 'model' and 'depth'
    df = df.sort_values(by=['model', 'max_depth'])

    # Filter out rows that have no value for column "dtcontrol nodes"
    df = df.dropna(subset=['dtcontrol nodes'])

    # df = df[df["max_depth"] <= 7]

    df['model'] = df['model'].str.replace('^omdt-|^qcomp-', '', regex=True)

    # Rename models according to the rename_dict
    df['model'] = df['model'].apply(lambda x: rename_dict[x] if x in rename_dict else x)

    # Remove rows from df that contain model names from filter_models
    df = df[~df['model'].isin(filter_models)]
    # df = df[df['model'].isin(filter_models)]

    max_depth = {}

    for model in df['model'].unique():
        model_df = df[df['model'] == model]
        max_depth[model] = model_df['max_depth'].max()
    
    # Create a dictionary to store the maximum depth for each model
    max_depth_reached = {}

    relarive_best_cutoff = 0.95
    
    # Filter the DataFrame to exclude rows where 'best relative' is 1.0 or higher depths after 1.0 is reached
    filtered_rows = []
    for _, row in df.iterrows():
        model = row['model']
        depth = row['max_depth']
        best_relative = row['best relative']
        
        if model not in max_depth_reached:
            max_depth_reached[model] = 0
        
        if max_depth_reached[model] == 0:
            filtered_rows.append(row)
            if best_relative >= relarive_best_cutoff:
                max_depth_reached[model] = depth
            if depth == max_depth[model]:
                max_depth_reached[model] = depth
        
    
    filtered_df = pd.DataFrame(filtered_rows)

    # Sort the DataFrame by 'model' and 'S'
    filtered_df = filtered_df.sort_values(by=['choices'])
    
    # Create a dictionary to store the dtcontrol nodes for each model
    dtcontrol_nodes = df.groupby('model')['dtcontrol nodes'].first().to_dict()
    
    # Create the bar plots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6.5), sharex=True, gridspec_kw={'height_ratios': [1, 1.2]})
    
    # Define colors for different depths
    colors = plt.cm.cividis_r(np.linspace(0.1, 1, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.twilight_shifted(np.linspace(0, 0.9, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.terrain_r(np.linspace(0, 0.9, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.cividis(np.linspace(0.1, 0.9, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.Greens(np.linspace(0.2, 1, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.Wistia(np.linspace(0.2, 1, len(filtered_df['max_depth'].unique())))
    # colors = plt.cm.YlGnBu(np.linspace(0.2, 0.9, len(filtered_df['max_depth'].unique())))

    colors = [[0.2, 0.2, 0.2], [0.4, 0.4, 0.4], [0.6, 0.6, 0.6], [0.8, 0.8, 0.8], [0.85, 1, 0.75], [0.65, 0.9, 0.6], [0.4, 0.8, 0.3], [0.25, 0.45, 0.1]]
    
    # Upper plot: Relative values
    bar_width = 0.4
    index = np.arange(len(filtered_df['model'].unique()))

    model_space_width = 1.5
    bar_space_width = 0.0
    
    # Create a mapping from model names to their indices
    model_indices = {model: i for i, model in enumerate(filtered_df['model'].unique())}
    model_bars_offset = {}

    # Compute the first large model
    first_large_model = filtered_df[filtered_df['choices'] >= 3000].iloc[0]['model']

    prev_models = []

    for model in model_indices.keys():
        model_bars_offset[model] = 0
        for prev_model in prev_models:
            model_bars_offset[model] += max_depth_reached[prev_model]
        prev_models.append(model)
    
    # Plot bars for each depth
    for depth, color in zip(sorted(filtered_df['max_depth'].unique()), colors):
        depth_df = filtered_df[filtered_df['max_depth'] == depth]
        ax1.bar(
            [model_indices[model] * model_space_width + (model_bars_offset[model] + depth) * (bar_width+bar_space_width) + bar_space_width for index, model in enumerate(depth_df['model'])],
            depth_df['best relative'],
            bar_width,
            label=f'Depth {depth}',
            color=color
        )
    
    ax1.set_ylabel('Normalised Value', fontsize=14)
    ax1.set_ylim(0, 1)
    # ax1.legend(title='', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.yaxis.grid(True, linestyle='--')
    ax1.set_axisbelow(True)
    ax1.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are off
    
    # Add a vertical line to separate smaller and larger models
    ax1.axvline(x=model_indices[first_large_model] * model_space_width + (model_bars_offset[first_large_model] * bar_width+bar_space_width) - bar_width, color='black', linestyle='--')
    
    # Lower plot: Tree nodes (logarithmic scale)
    for depth, color in zip(sorted(filtered_df['max_depth'].unique()), colors):
        depth_df = filtered_df[filtered_df['max_depth'] == depth]
        ax2.bar(
            [model_indices[model] * model_space_width + (model_bars_offset[model] + depth) * (bar_width+bar_space_width) + bar_space_width for index, model in enumerate(depth_df['model'])],
            depth_df['tree nodes'],
            bar_width,
            label=f'Depth {depth}',
            color=color
        )
    
    # Plot dtcontrol nodes
    for model, idx in model_indices.items():
        ax2.bar(
            model_indices[model] * model_space_width + (model_bars_offset[model] + max_depth_reached[model]+1) * (bar_width+bar_space_width) + bar_space_width,
            dtcontrol_nodes[model],
            bar_width,
            label='DTControl' if idx == 0 else "",
            color='sandybrown'
        )

        if add_dtcontrol_depths:
            # Annotate dtcontrol bars with the value of "dtcontrol depth"
            dtcontrol_depth = df[df['model'] == model]['dtcontrol depth'].values[0]
            if model in ["consensus"]:
                ax2.text(
                model_indices[model] * model_space_width + (model_bars_offset[model] + max_depth_reached[model]+1) * (bar_width+bar_space_width) + bar_space_width + 0.8,
                dtcontrol_nodes[model]-32,
                f'({dtcontrol_depth})',
                ha='center',
                va='bottom',
                fontsize=10,
                color='black'
                )
            elif model in ["rabin"]:
                ax2.text(
                model_indices[model] * model_space_width + (model_bars_offset[model] + max_depth_reached[model]+1) * (bar_width+bar_space_width) + bar_space_width + 0.7,
                dtcontrol_nodes[model]-1,
                f'({dtcontrol_depth})',
                ha='center',
                va='bottom',
                fontsize=10,
                color='black'
                )
            else:
                ax2.text(
                model_indices[model] * model_space_width + (model_bars_offset[model] + max_depth_reached[model]+1) * (bar_width+bar_space_width) + bar_space_width + 0.1,
                dtcontrol_nodes[model],
                f'({dtcontrol_depth})',
                ha='center',
                va='bottom',
                fontsize=10,
                color='black'
                )
        
    
    ax2.set_ylabel('Tree Decision Nodes (log scale)', fontsize=14)
    ax2.set_yscale('log', base=2)
    ax2.set_xticks([model_indices[model] * model_space_width + (model_bars_offset[model]) * (bar_width+bar_space_width) + bar_space_width + ((max_depth_reached[model]+2)/2 * (bar_width+bar_space_width)) for index, model in enumerate(filtered_df['model'].unique())])
    ax2.set_xticklabels(filtered_df['model'].unique(), rotation=45, ha='right')
    ax2.yaxis.grid(True, linestyle='--')
    ax2.set_axisbelow(True)
    ax2.legend(title='', bbox_to_anchor=(0.95, 1.05), loc='upper left', framealpha=1, facecolor='white')

    ax2.axvline(x=model_indices[first_large_model] * model_space_width + (model_bars_offset[first_large_model] * bar_width+bar_space_width) - bar_width, color='black', linestyle='--')
    
    # plt.tight_layout()
    # plt.show()
    if generate_pgf:
        plt.savefig('results/generated-results/figure-5.pgf')
    else:
        fig.savefig('results/generated-results/figure-5.pdf', bbox_inches='tight')

def plot_figure_2(file_path, generate_pgf):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    if generate_pgf:
        matplotlib.use("pgf")
        matplotlib.rcParams.update({
            "pgf.texsystem": "pdflatex",
            'font.family': 'serif',
            'text.usetex': True,
            'pgf.rcfonts': False,
        })
    
    # Convert columns to appropriate types
    df['max_depth'] = df['max_depth'].astype(int)
    df['S'] = df['S'].astype(int)
    df['choices'] = df['choices'].astype(int)
    df['Act'] = df['Act'].astype(int)
    df['omdt best'] = df['omdt best'].astype(float)
    df['best'] = df['best'].astype(float)
    df['random'] = df['random'].astype(float)
    df['*-opt'] = df['*-opt'].astype(float)
    
    # Separate the DataFrame into two based on the 'depth' column
    df_smaller = df[df['choices'] <= 3000]
    df_larger = df[df['choices'] > 3000]

    # Function to compute relative value
    def compute_relative_value(value, min_value, max_value, row):
        relative_value = (value - min_value) / (max_value - min_value)
        if relative_value > 1.05:
            relative_value = 0 # OMDT can give wrong values sometimes...
        return min(max(relative_value, 0.005), 0.995)
    
    # Function to classify points
    def classify_point(row):
        base_color = 'orange' if row['max_depth'] <= 4 else 'green'
        return base_color
    
    # Introduce jitter to the scatter plot
    def add_jitter(values, jitter_amount=0.0075):
        jittered_values = values + np.random.uniform(-jitter_amount, jitter_amount, size=values.shape)
        return np.clip(jittered_values, 0.005, 0.995)
    
    # Create scatter plot for depth <= 3
    fig1 = plt.figure()
    # Scatter plot for points classified as 'orange'
    plt.scatter(
        add_jitter(df_smaller[df_smaller.apply(lambda row: classify_point(row) == 'orange', axis=1)].apply(lambda row: compute_relative_value(row['best'], row['random'], row['*-opt'], row), axis=1)),
        add_jitter(df_smaller[df_smaller.apply(lambda row: classify_point(row) == 'orange', axis=1)].apply(lambda row: compute_relative_value(row['omdt best'], row['random'], row['*-opt'], row), axis=1)),
        c='orange',
        marker='^',
        s=60,  # Set marker size
        label='depths 1-4',
        alpha=0.5
    )
    
    # Scatter plot for points classified as 'green'
    plt.scatter(
        add_jitter(df_smaller[df_smaller.apply(lambda row: classify_point(row) == 'green', axis=1)].apply(lambda row: compute_relative_value(row['best'], row['random'], row['*-opt'], row), axis=1)),
        add_jitter(df_smaller[df_smaller.apply(lambda row: classify_point(row) == 'green', axis=1)].apply(lambda row: compute_relative_value(row['omdt best'], row['random'], row['*-opt'], row), axis=1)),
        c='green',
        marker='o',
        s=60,  # Set marker size
        label='depths 5-8',
        alpha=0.5
    )

    # for index, row in df_smaller.iterrows():
    #     plt.annotate(row['model'], (compute_relative_value(row['best'], row['random'], row['*-opt'], row), compute_relative_value(row['omdt best'], row['random'], row['*-opt'], row)))
    
    plt.legend(fontsize=12, bbox_to_anchor=(0, 1), loc='upper left', framealpha=1, facecolor='white')

    plt.plot([0, 1], [0, 1], 'grey', linewidth=0.5)  # Add thinner grey diagonal line

    plt.ylabel('Relative OMDT best', fontsize=14)
    plt.xlabel('Relative DTPAYNT best', fontsize=14)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.title('DTPAYNT vs OMDT (Smaller models)', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    # plt.show()
    
    # Create scatter plot for depth > 3
    fig2 = plt.figure()
    # Scatter plot for points classified as 'orange'

    # Scatter plot for points classified as 'orange' with jitter
    plt.scatter(
        add_jitter(df_larger[df_larger.apply(lambda row: classify_point(row) == 'orange', axis=1)].apply(lambda row: compute_relative_value(row['best'], row['random'], row['*-opt'], row), axis=1)),
        add_jitter(df_larger[df_larger.apply(lambda row: classify_point(row) == 'orange', axis=1)].apply(lambda row: compute_relative_value(row['omdt best'], row['random'], row['*-opt'], row), axis=1)),
        c='orange',
        marker='^',
        s=60,  # Set marker size
        label='depths 1-4',
        alpha=0.5
    )

    # Scatter plot for points classified as 'green' with jitter
    plt.scatter(
        add_jitter(df_larger[df_larger.apply(lambda row: classify_point(row) == 'green', axis=1)].apply(lambda row: compute_relative_value(row['best'], row['random'], row['*-opt'], row), axis=1)),
        add_jitter(df_larger[df_larger.apply(lambda row: classify_point(row) == 'green', axis=1)].apply(lambda row: compute_relative_value(row['omdt best'], row['random'], row['*-opt'], row), axis=1)),
        c='green',
        marker='o',
        s=60,  # Set marker size
        label='depths 5-8',
        alpha=0.5
    )

    

    # for index, row in df_larger.iterrows():
    #     plt.annotate(row['model'], (compute_relative_value(row['best'], row['random'], row['*-opt'], row), compute_relative_value(row['omdt best'], row['random'], row['*-opt'], row)))
    
    plt.legend(fontsize=12, bbox_to_anchor=(0, 1), loc='upper left', framealpha=1, facecolor='white')
    
    plt.plot([0, 1], [0, 1], 'grey', linewidth=0.5)  # Add thinner grey diagonal line

    plt.ylabel('Relative OMDT best', fontsize=14)
    plt.xlabel('Relative DTPAYNT best', fontsize=14)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.title('DTPAYNT vs OMDT (Larger models)', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    # plt.show()

    if generate_pgf:
        plt.savefig('results/generated-results/figure-2.pgf')
    else:
        fig1.savefig('results/generated-results/figure-2-smaller.pdf', bbox_inches='tight')
        fig2.savefig('results/generated-results/figure-2-larger.pdf', bbox_inches='tight')

def plot_figure_4(file_path, generate_pgf):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    if generate_pgf:
        matplotlib.use("pgf")
        matplotlib.rcParams.update({
            "pgf.texsystem": "pdflatex",
            'font.family': 'serif',
            'text.usetex': True,
            'pgf.rcfonts': False,
        })

    # Function to compute relative value
    def compute_relative_value(value, min_value, max_value):
        relative_value = (value - min_value) / (max_value - min_value)
        if relative_value > 1.05: # OMDT can give wrong values sometimes...
            relative_value = 0
        return min(max(relative_value, 0.005), 0.995)
    
    # Convert columns to appropriate types
    df['max_depth'] = df['max_depth'].astype(int)
    df['S'] = df['S'].astype(int)
    df['choices'] = df['choices'].astype(int)
    df['Act'] = df['Act'].astype(int)
    df['omdt best'] = df['omdt best'].astype(float)
    df['best'] = df['best'].astype(float)
    df['random'] = df['random'].astype(float)
    df['*-opt'] = df['*-opt'].astype(float)

    # Filter rows where the difference in relative values between "best" and "omdt best" is less than 10%
    df = df[df.apply(lambda row: abs(compute_relative_value(row['best'], row['random'], row['*-opt']) - compute_relative_value(row['omdt best'], row['random'], row['*-opt'])) < 0.1, axis=1)]

    # for row in df.iterrows():
    #     print(row)
    #     print(compute_relative_value(row['best'], row['random'], row['*-opt']), compute_relative_value(row['omdt best'], row['random'], row['*-opt']))
    
    # Separate the DataFrame into two based on the 'depth' column
    df_smaller = df[df['choices'] <= 3000]
    df_larger = df[df['choices'] > 3000]

    # Function to classify points
    def classify_point(row):
        base_color = 'orange' if row['choices'] <= 3000 else 'green'
        return base_color
    
    # Introduce jitter to the scatter plot
    def add_jitter(values, jitter_amount=0.0075):
        jittered_values = values + np.random.uniform(-jitter_amount, jitter_amount, size=values.shape)
        return np.clip(jittered_values, 0.005, 0.995)
    
    # Create scatter plot for depth <= 3
    fig = plt.figure()
    # Scatter plot for points classified as 'orange'
    plt.scatter(
        df[df.apply(lambda row: classify_point(row) == 'orange', axis=1)].apply(lambda row: row['time (best)'], axis=1),
        df[df.apply(lambda row: classify_point(row) == 'orange', axis=1)].apply(lambda row: row['omdt time (best)'], axis=1),
        c='orange',
        marker='^',
        s=60,  # Set marker size
        label='smaller models',
        alpha=0.5
    )
    
    # Scatter plot for points classified as 'green'
    plt.scatter(
        df[df.apply(lambda row: classify_point(row) == 'green', axis=1)].apply(lambda row: row['time (best)'], axis=1),
        df[df.apply(lambda row: classify_point(row) == 'green', axis=1)].apply(lambda row: row['omdt time (best)'], axis=1),
        c='green',
        marker='o',
        s=60,  # Set marker size
        label='larger models',
        alpha=0.5
    )

    # for index, row in df_smaller.iterrows():
    #     plt.annotate(row['model'], (compute_relative_value(row['best'], row['random'], row['*-opt'], row), compute_relative_value(row['omdt best'], row['random'], row['*-opt'], row)))
    
    plt.legend(fontsize=12, bbox_to_anchor=(0.59, 0.6), loc='upper left', framealpha=1, facecolor='white')

    plt.plot([0, 1200], [0, 1200], 'grey', linewidth=0.5)  # Add thinner grey diagonal line

    plt.ylabel('OMDT runtime (s)', fontsize=14)
    plt.xlabel('PAYNT runtime (s)', fontsize=14)
    plt.xlim(0, 1200)
    plt.ylim(0, 1200)
    plt.title('DTPAYNT vs OMDT runtimes', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    # plt.show()

    if generate_pgf:
        plt.savefig('results/generated-results/figure-4.pgf')
    else:
        fig.savefig('results/generated-results/figure-4.pdf', bbox_inches='tight')

def generate_model_info_table(file_path):
    with open(file_path, mode='r') as file:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Define the order of columns for the LaTeX table
        column_order = ["model", "vars", "S", "Act", "choices"]

        rename_dict = {
            "maze-7": "maze-7",
            "maze-steps": "maze-steps",
            "3d_navigation": "3d",
            "blackjack": "blackjack",
            "frozenlake_4x4": "lake-4",
            "frozenlake_8x8": "lake-8",
            "frozenlake_12x12": "lake-12",
            "inventory_management": "inventory",
            "system_administrator_1": "sys-1",
            "system_administrator_2": "sys-2",
            "system_administrator_tree": "sys-tree",
            "tictactoe_vs_random": "tictactoe",
            "traffic_intersection": "traffic",
            "consensus-3-32": "consensus",
            "csma-2-4": "csma",
            "firewire-3": "firewire",
            "ij-10": "ij",
            "pacman": "pacman",
            "philosophers-4": "philos",
            "pnueli-zuck-3": "pnueli",
            "rabin-4": "rabin",
            "resource-gathering-5": "resource",
            "wlan-1-2": "wlan",
            "wlan-2-cost": "wlan"
        }

        # Remove duplicates based on the 'model' column
        df = df.drop_duplicates(subset=['model'])

        # Rename models according to the rename_dict
        df['model'] = df['model'].str.replace('^omdt-|^qcomp-', '', regex=True)
        df['model'] = df['model'].apply(lambda x: rename_dict[x] if x in rename_dict else x)



        # Open the file in write mode
        with open("results/generated-results/model-info-table.tex", "w") as f:
            # Start LaTeX table
            f.write(r"\begin{tabular}{l rrrr@{\hskip 32pt}l rrrr}" + "\n")
            f.write(r"\toprule" + "\n")
            f.write(r"\multirow{1}{*}{model} & vars & $|S|$ & $|Act|$ & choices & \multirow{1}{*}{model} & vars & $|S|$ & $|Act|$ & choices \\" + "\n")
            f.write(r"\midrule" + "\n")

            # Iterate through rows in pairs
            for i in range(0, len(df), 2):
                row1 = df.iloc[i]
                ordered_row1 = [
                    f"{float(row1[col]):.2f}" if col == "*-opt" else str(row1[col]).replace('_', r'\_') if isinstance(row1[col], str) else row1[col]
                    for col in column_order
                ]
                ordered_row1 = [str(x) for x in ordered_row1]
                if i + 1 < len(df):
                    row2 = df.iloc[i + 1]
                    ordered_row2 = [
                    f"{float(row2[col]):.2f}" if col == "*-opt" else str(row2[col]).replace('_', r'\_') if isinstance(row2[col], str) else row2[col]
                    for col in column_order
                    ]
                    ordered_row2 = [str(x) for x in ordered_row2]
                else:
                    ordered_row2 = [""] * len(column_order)
                f.write(" & ".join(ordered_row1) + " & " + " & ".join(ordered_row2) + r" \\" + "\n")
            
            # End LaTeX table
            f.write(r"\bottomrule" + "\n")
            f.write(r"\end{tabular}" + "\n")

@click.command()
@click.option('--file-path', type=str, default='./results/logs/final-merge.csv', help='Path to the CSV file.')
@click.option('--generate-pgf', is_flag=True, default=False, help='Generate PGF output.')
@click.option('--add-dtcontrol-depths', is_flag=True, default=False, help='Adds dtcontrol depths to figures 3 and 5. Can only be used with original log files.')
def main(file_path, generate_pgf, add_dtcontrol_depths):
    # Use the function with the provided file path
    plot_figure_2(file_path, generate_pgf)
    plot_figure_3(file_path, generate_pgf, add_dtcontrol_depths)
    plot_figure_4(file_path, generate_pgf)
    plot_figure_5(file_path, generate_pgf, add_dtcontrol_depths)

    generate_model_info_table(file_path)

if __name__ == '__main__':
    main()