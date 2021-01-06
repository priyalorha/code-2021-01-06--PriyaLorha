import unittest

from main import read_json_return_csv, handler, include_bmi_data, check_bmi, count_overweight
import pandas as pd


class MyTestCase(unittest.TestCase):
    def test_compute_bmi(self):
        df = pd.DataFrame([{"HeightCm": 161, "WeightKg": 85}])
        data = include_bmi_data(df).to_dict(orient='records')[0]
        self.assertEqual(data['BMI Category'], 'Moderately obese')
        self.assertEqual(data['Health risk'], 'Medium risk')
        self.assertEqual(check_bmi(25), [25, "Overweight", "Enhanced risk"])

    def test_count_overweight(self):
        df = pd.DataFrame([{"HeightCm": 161, "WeightKg": 85}])
        include_bmi_data(df)
        self.assertNotEqual(count_overweight(df), 5)
        self.assertEqual(count_overweight(df), 0)


if __name__ == '__main__':
    unittest.main()
