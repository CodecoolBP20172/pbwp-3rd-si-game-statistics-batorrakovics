import reports
# Printing functions
def file_read(file_name):
    games_list = []
    with open(file_name, "r") as f:
        for line in f:
            games_list.append(line.strip().split("\t"))
    return games_list

def get_most_played(file_name):
    most_played = reports.get_most_played(file_name)
    print(most_played)

def sum_sold(file_name):
    total = reports.sum_sold(file_name)
    print(total)

def get_selling_avg(file_name):
    avg = reports.get_selling_avg(file_name)
    print(avg)

def count_longest_title(file_name):
    longest = reports.count_longest_title(file_name)
    print(longest)

def get_date_avg(file_name):
    average = reports.get_date_avg(file_name)
    print(average)

def get_game(file_name, title):
    game = reports.get_game(file_name, title)
    print(game)

def main():
    file_name = "game_stat.txt"
    title = "Minecraft"
    get_most_played(file_name)
    sum_sold(file_name)
    get_selling_avg(file_name)
    count_longest_title(file_name)
    get_date_avg(file_name)
    get_game(file_name, title)

main()