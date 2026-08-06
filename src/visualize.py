import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA


def plot__average_ratings(matrix, song_ids, save_path="data/peak_average_ratings.png"):
    # This basically computes mean per song across all users
    avg_ratings = np.nanmean(matrix, axis=0)

    # Sort songs by average rating for better storytelling
    sorted_indices = np.argsort(avg_ratings)[::-1]
    sorted_songs = [song_ids[i] for i in sorted_indices]
    sorted_means = avg_ratings[sorted_indices]

    # Styling setup
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(14, 7), dpi=300)

    # Gradient color mapping based on rating height
    colors = sns.color_palette("plasma", len(sorted_means))

    bars = plt.bar(
        sorted_songs,
        sorted_means,
        color=colors,
        edgecolor="black",
        linewidth=0.8,
        alpha=0.9,
    )

    # Formatting details
    plt.title(
        "Average User Rating per Track (Sorted Highest to Lowest)",
        fontsize=15,
        fontweight="bold",
        pad=15,
    )
    plt.xlabel("Song Tracks", fontsize=12, labelpad=10)
    plt.ylabel("Average Rating (1 - 5 Stars)", fontsize=12, labelpad=10)
    plt.ylim(0, 5.5)
    plt.xticks(rotation=45, ha="right", fontsize=10, fontweight="medium")
    plt.axhline(
        y=np.nanmean(avg_ratings),
        color="red",
        linestyle="--",
        linewidth=1.5,
        label=f"Overall Catalog Mean ({np.nanmean(avg_ratings):.2f})",
    )

    # Add numeric labels on top of every bar
    for bar in bars:
        height = bar.get_height()
        if not np.isnan(height):
            plt.text(
                bar.get_x() + bar.get_width() / 2.0,
                height + 0.1,
                f"{height:.2f}",
                ha="center",
                va="bottom",
                fontsize=9,
                fontweight="bold",
            )

    plt.legend(loc="upper right", frameon=True)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()