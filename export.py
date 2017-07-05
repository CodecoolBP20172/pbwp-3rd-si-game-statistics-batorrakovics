import reports
export_data = []
# Export function
def count_games(file_name):
    count = reports.count_games(file_name)
    export_data.append(count)
    return count

def decide(file_name, year):
    yes = reports.decide(file_name, year)
    if yes == True:
        export_data.append("Yes")
        return "Yes."

def get_latest(file_name):
    year = reports.get_latest(file_name)
    export_data.append(year)
    return year

def count_by_genre(file_name, genre):
    num = reports.count_by_genre(file_name, genre)
    export_data.append(num)
    return num

def get_line_number_by_title(file_name, title):
    line_num = reports.get_line_number_by_title(file_name, title)
    export_data.append(line_num)
    return line_num

def export(filename="export.txt"):
    export_file = open(filename, "w")
    for i in export_data:
        export_file.write(str(i))
        export_file.write("\n")
    export_file.close()

def main():
    file_name = "game_stat.txt"
    year = "2004"
    title = "Minecraft"
    genre = "RPG"
    count_games(file_name)
    decide(file_name, year)
    get_latest(file_name)
    count_by_genre(file_name, genre)
    get_line_number_by_title(file_name, title)
    export()

main()