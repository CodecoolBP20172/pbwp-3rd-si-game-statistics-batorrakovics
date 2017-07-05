# Opening and storing the file
def file_read(file_name):
    games_list = []
    with open(file_name, "r") as f:
        for line in f:
            games_list.append(line.strip().split("\t"))
    return games_list

# Report functions
def count_games(file_name):
    games_list = file_read(file_name)
    count = len(games_list)
    return count

def decide(file_name, year):
    games_list = file_read(file_name)
    search = year
    any(e[1] == search for e in games_list)
    return True

def get_latest(file_name):
    games_list = file_read(file_name)
    years = []
    for sub_list in games_list:
        years.append(sub_list[2])
    maxyears = max(years)
    return (games_list[years.index(maxyears)])
    
        
        
def count_by_genre(file_name, genre):
    games_list = file_read(file_name)
    genre_list = []
    for sub_list in games_list:
        genre_list.append(sub_list[3])

def get_line_number_by_title(file_name, title):
    pass

#file_read("game_stat.txt")
#count_games("game_stat.txt")
#decide("game_stat.txt", "2009")
get_latest("game_stat.txt")