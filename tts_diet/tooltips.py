# To minimize distraction from the logical code in tts_diet.py, I'm putting the tooltips in this file.
# The tooltips are completely optional but they make the schemas more comprehensible.
input_schema_tooltips = {
    ("categories", ""): "Define the nutrition categories.",
    ("categories", "Name"): "The name of the category.",
    ("categories", "Min Nutrition"): "The minimum amount of this category that must be consumed.",
    ("categories", "Max Nutrition"): "The maximum amount of this category that must be consumed.",
    ("foods", ""): "Define the foods.",
    ("foods", "Name"): "The name of the food.",
    ("foods", "Cost"): "The price of the food.",
    ("nutrition_quantities", ""): "Define the amount of nutrition in each food.",
    ("nutrition_quantities", "Food"): "The name of the food.",
    ("nutrition_quantities", "Category"): "The name of the nutrition category.",
    ("nutrition_quantities", "Quantity"): "The quantity of nutrition of this category supplied by this food.",
}

solution_schema_tooltips = {
    ("buy_food", ""): "This report defines the foods to purchase.",
    ("buy_food", "Food"): "The name of the food to purchase.",
    ("buy_food", "Quantity"): "The amount of this food that should be purchased.",
    ("consume_nutrition", ""): "This report defines the nutrition that is consumed.",
    ("consume_nutrition", "Category"): "The name of the nutrition category.",
    ("consume_nutrition", "Quantity"): "The amount of this category that will be consumed.",
    ("parameters", ""): "This report lists the Key Performance Indicators for the solution.",
    ("parameters", "Parameter"): "This name of the Key Performance Indicator.",
    ("parameters", "Value"): "The value of the Key Performance Indicator.",
}