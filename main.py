import os
import pandas as pd
import matplotlib.pyplot as plt


def main():
    input_path = "input/input_data.xlsx"
    output_path = "output/latency_chart.png"

    os.makedirs("output", exist_ok=True)

    # read excel
    df = pd.read_excel(input_path)

    # use first two columns
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]

    # generate line chart
    plt.figure()
    plt.plot(x, y, marker="o")
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.title("Latency vs Node Numbers")

    # save output
    plt.savefig(output_path)
    plt.close()
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()