import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--stacked", action="store_true", help="Stack bars when drawing multiple bar series")
    parser.add_argument("--colors", help="Comma-separated colors for each series")

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    chart_type = args.type
    stacked = args.stacked
    colors = [c.strip() for c in args.colors.split(",")] if args.colors else None

    os.makedirs("output", exist_ok=True)

    # read excel
    df = pd.read_excel(input_path)

    # use first column as x and the rest as y series for line charts
    x = df.iloc[:, 0]
    y_series = df.iloc[:, 1:]

    # generate chart
    plt.figure()
    if chart_type == "line":
        if y_series.shape[1] == 0:
            print("Line chart needs at least one y-series column after the first column.")
            return
        for idx, column in enumerate(y_series.columns):
            plot_kwargs = {"marker": "o", "label": column}
            if colors and idx < len(colors):
                plot_kwargs["color"] = colors[idx]
            plt.plot(x, y_series[column], **plot_kwargs)
        plt.xlabel(df.columns[0])
        plt.ylabel(" / ".join(y_series.columns))
        plt.title("Line Chart")
        plt.legend()

    elif chart_type == "bar":
        if y_series.shape[1] == 0:
            print("Bar chart needs at least one y-column after the first column.")
            return
        x_positions = np.arange(len(x))
        if stacked:
            bottoms = np.zeros(len(x))
            for idx, column in enumerate(y_series.columns):
                bar_kwargs = {"bottom": bottoms, "label": column}
                if colors and idx < len(colors):
                    bar_kwargs["color"] = colors[idx]
                plt.bar(x_positions, y_series[column], width=0.8, **bar_kwargs)
                bottoms += y_series[column].values
            title = "Stacked Bar Chart"
        else:
            total_series = y_series.shape[1]
            bar_width = 0.8 / total_series
            for idx, column in enumerate(y_series.columns):
                offsets = x_positions + idx * bar_width - (total_series - 1) * bar_width / 2
                bar_kwargs = {"width": bar_width, "label": column}
                if colors and idx < len(colors):
                    bar_kwargs["color"] = colors[idx]
                plt.bar(offsets, y_series[column], **bar_kwargs)
            title = "Bar Chart"
        plt.xticks(x_positions, x)
        plt.xlabel(df.columns[0])
        plt.ylabel(" / ".join(y_series.columns))
        plt.title(title)
        plt.legend()

    elif chart_type == "pie":
        if y_series.shape[1] != 1:
            print("Pie chart currently supports only one y-column.")
            return
        y = y_series.iloc[:, 0]
        pie_kwargs = {"labels": x, "autopct": "%1.1f%%"}
        if colors and len(colors) >= 1:
            pie_kwargs["colors"] = colors
        plt.pie(y, **pie_kwargs)
        plt.title("Pie Chart")

    else:
        print("Invalid chart type. Use 'line', 'bar' or 'pie'")
        return

    plt.tight_layout()

    # save output
    plt.savefig(output_path)
    plt.close()
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()