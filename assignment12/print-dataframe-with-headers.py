import pandas as pd


class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        total_rows = len(self)
        for i in range(0, total_rows, 10):
            print("\n=== Rows {} to {} ===".format(i, min(i + 9, total_rows - 1)))
            print(self.iloc[i : i + 10].to_string(index=False))


if __name__ == "__main__":
    dfp = DFPlus.from_csv("../csv/products.csv")
    dfp.print_with_headers()
