# When run from the command line, will read/write json/xls/csv/db/sql/mdb files
# For example, typing
#   python -m tts_diet -i diet_sample_data -o diet_solution_data
# will read from a model stored in the directory diet_sample_data and write the solution
# to a directory called diet_solution_data. These data directories contain .csv files.
# This all assumes the tts_diet package has been installed from a .whl file, or is otherwise
# in the Python path.
from ticdat import standard_main
from tts_diet import input_schema, solution_schema, solve
if __name__ == "__main__":
    standard_main(input_schema, solution_schema, solve)
