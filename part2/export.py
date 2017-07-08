import reports
export_data = []
# Export function
def get_most_played(file_name):
    most_played = reports.get_most_played(file_name)
    export_data.append(most_played)
    return most_played

def sum_sold(file_name):
    total = reports.sum_sold(file_name)
    export_data.append(total)
    return total

def get_selling_avg(file_name):
    avg = reports.get_selling_avg(file_name)
    export_data.append(avg)
    return avg

def count_longest_title(file_name):
    longest = reports.count_longest_title(file_name)
    export_data.append(longest)
    return longest

def get_date_avg(file_name):
    average = reports.get_date_avg(file_name)
    export_data.append(average)
    return average

def get_game(file_name, title):
    game = reports.get_game(file_name, title)
    export_data.append(game)
    return game

def export(filename="export.txt"):
    export_file = open(filename, "w")
    for i in export_data:
        export_file.write(str(i))
        export_file.write("\n")
    export_file.close()

def main():
    file_name = "game_stat.txt"
    title = "Minecraft"
    get_most_played(file_name)
    sum_sold(file_name)
    get_selling_avg(file_name)
    count_longest_title(file_name)
    get_date_avg(file_name)
    get_game(file_name, title)
    export()

main()