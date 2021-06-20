import os
import inspect
import tts_diet
import unittest

def _this_directory() :
    return os.path.dirname(os.path.realpath(os.path.abspath(inspect.getsourcefile(_this_directory))))

def get_test_data(data_set_name):
    path = os.path.join(_this_directory(), "data", data_set_name)
    assert os.path.exists(path), f"bad path {path}"
    # right now assumes data is archived as either a directory of csv files or a single json file for each data set
    if os.path.isfile(path):
        return tts_diet.input_schema.json.create_tic_dat(path)

def _nearly_same(x, y, epsilon=1e-5):
    if x == y or max(abs(x), abs(y)) < epsilon:
        return True
    if min(abs(x), abs(y)) > epsilon:
        return abs(x-y) /  min(abs(x), abs(y)) < epsilon

def _smaller(x, y, epsilon=1e-5):
    return x < y and not _nearly_same(x, y, epsilon)

class TestDiet(unittest.TestCase):
    # This is a pretty simple test suite - just two data sets. But the template should be clear for how you could
    # archive many useful data sets for validating your optimization engine.
    def test_standard_data_set(self):
        dat = get_test_data("standard_data_set.json")
        sln = tts_diet.solve(dat)
        self.assertTrue(_nearly_same(11.82886, sln.parameters["Total Cost"]["Value"], epsilon=1e-4))
        # The test_ subroutine can stop here and still be a good test. The rest of the subroutine
        # demonstrates how you can validate the objective function is being handled by the optimization
        most_eaten = sorted(sln.buy_food, key= lambda f: sln.buy_food[f]["Quantity"], reverse=True)[0]
        dat.foods[most_eaten]["Cost"] *= 10
        sln2 =  tts_diet.solve(dat)
        self.assertTrue(_smaller(11.82886, sln2.parameters["Total Cost"]["Value"]))
        self.assertTrue(most_eaten not in sln2.buy_food or
                        _smaller(sln2.buy_food[most_eaten]["Quantity"], sln.buy_food[most_eaten]["Quantity"]))

    def test_neos_guide_data_set(self):
        # Reproducing the result from here https://neos-guide.org/content/diet-problem.
        # Note that they have a constraint on servings per foods, which we model using dummy categories.
        dat = get_test_data("neos_data_set.json")
        sln = tts_diet.solve(dat)
        self.assertTrue(all(_nearly_same(qty, sln.buy_food[f]["Quantity"]) for f, qty in
                            [['Corn', 1.94444], ['2% Milk', 10], ['Wheat Bread', 10]]))

# Run the tests via the command line
if __name__ == "__main__":
    unittest.main()