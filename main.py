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

    # use first two columns
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]

    # generate line chart
    plt.figure()
    if chart_type == "line":
        plt.plot(x, y, marker="o")
        plt.xlabel(df.columns[0])
        plt.ylabel(df.columns[1])
        plt.title("Line Chart")

    elif chart_type == "pie":
        plt.pie(y, labels=x, autopct="%1.1f%%")
        plt.title("Pie Chart")

    else:
        print("Invalid chart type. Use 'line' or 'pie'")
        return

    plt.tight_layout()

    # save output
    plt.savefig(output_path)
    plt.close()
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()