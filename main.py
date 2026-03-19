import argparse
import pandas as pd
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    # read csv
    df = pd.read_csv(args.input)

    # use first two columns
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]

    # generate chart
    if args.type == "line":
        plt.plot(x, y)
    elif args.type == "bar":
        plt.bar(x, y)
    elif args.type == "pie":
        plt.pie(y, labels=x)
    else:
        print("Invalid chart type")
        return

    # save output
    plt.savefig(args.output)
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()