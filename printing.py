import reports
# Printing functions
def file_read(file_name):
    games_list = []
    with open(file_name, "r") as f:
        for line in f:
            games_list.append(line.strip().split("\t"))
    return games_list

def count_games(file_name):
    count = reports.count_games(file_name)
    print(count)

def decide(file_name, year):
    yes = reports.decide(file_name, year)
    if yes == True:
        print("Yes.")

def get_latest(file_name):
    year = reports.get_latest(file_name)
    print(year)

def count_by_genre(file_name, genre):
    num = reports.count_by_genre(file_name, genre)
    print(num)

def get_line_number_by_title(file_name, title):
    line_num = reports.get_line_number_by_title(file_name, title)
    print(line_num)

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

main()