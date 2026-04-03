import os
import pandas as pd
import matplotlib.pyplot as plt
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output
    chart_type = args.type

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
        for column in y_series.columns:
            plt.plot(x, y_series[column], marker="o", label=column)
        plt.xlabel(df.columns[0])
        plt.ylabel(" / ".join(y_series.columns))
        plt.title("Line Chart")
        plt.legend()

    elif chart_type == "bar":
        if y_series.shape[1] != 1:
            print("Bar chart currently supports only one y-column.")
            return
        y = y_series.iloc[:, 0]
        plt.bar(x, y)
        plt.xlabel(df.columns[0])
        plt.ylabel(y_series.columns[0])
        plt.title("Bar Chart")

    elif chart_type == "pie":
        if y_series.shape[1] != 1:
            print("Pie chart currently supports only one y-column.")
            return
        y = y_series.iloc[:, 0]
        plt.pie(y, labels=x, autopct="%1.1f%%")
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