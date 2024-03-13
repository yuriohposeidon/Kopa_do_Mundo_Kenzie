from exceptions import  *

def  data_processing(data):
    if data["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    year_initial = int(data["first_cup"].split("-")[0])

    if year_initial not in range(1930, 2023, 4):
        raise InvalidYearCupError("there was no world cup this year")

    possible_years = range(year_initial, 2023, 4)
    print(len(possible_years))

    if data["titles"] > len(possible_years):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")

