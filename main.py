# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


def check_bmi(bmi):
    if bmi <= 18.4:
        return [bmi, "Underweight", "Malnutrition risk"]
    elif 18.5 <= bmi <= 24.9:
        return [bmi, "Normal weight", "Normal weight"]
    elif 24.9 < bmi <= 29.9:
        return [bmi, "Overweight", "Enhanced risk"]
    elif 29.9 < bmi <= 34.9:
        return [bmi, "Moderately obese", "Medium risk"]
    elif 34.9 < bmi <= 39.9:
        return [bmi, "Severely obese", "High risk"]
    elif bmi >= 40:
        return [bmi, "Very severely obese", "Very high risk"]


def compute_bmi(df: pd.Series) -> pd.Series:
    height_in_ms = df['HeightCm'] / 100
    bmi = df['WeightKg'] / (height_in_ms ** 2)
    return check_bmi(bmi)


def read_json_return_csv(name: str) -> pd.DataFrame:
    return pd.read_json(name)  # Press ⌘F8 to toggle the breakpoint.


def count_overweight(df: pd.DataFrame) -> int:
    return len(df[df['BMI Category'] == 'Overweight'])


def include_bmi_data(df: pd.DataFrame) -> pd.DataFrame:
    df[['bmi', 'BMI Category', 'Health risk']] = df.apply(compute_bmi, axis=1, result_type='expand')
    return df


def handler(df: pd.DataFrame):
    include_bmi_data(df)
    df.to_json('result.json', orient='records')
    print(f"number of overweight: {count_overweight(df)}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name_of_the_json_file = 'input.json'
    df = read_json_return_csv(name_of_the_json_file)
    handler(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
