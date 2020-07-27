"""
.. module:: working_with_excel.read_from_file
   :synopsis: Get the information from excel file and write computing results to another file.
"""

from openpyxl import load_workbook


def load_census_file():
    return load_workbook("excel_files/censuspopdata.xlsx")["Population by Census Tract"]


def compute_population_of_each_country(sheet: load_workbook):
    new_dict: dict = {}
    for state, county, pop in zip(sheet["B"], sheet["C"], sheet["D"]):
        pop = int(pop.value) if str(pop.value).isdigit() else 0
        if state.value in new_dict:
            if county.value in new_dict[state.value]:
                new_dict[state.value][county.value]["pop"] += pop
            else:
                new_dict[state.value].update({county.value: {"pop": pop}})
        else:
            new_dict[state.value] = {county.value: {"pop": pop}}


def handle():
    sheet = load_workbook()
    compute_population_of_each_country(sheet)


if __name__ == "__main__":
    handle()
