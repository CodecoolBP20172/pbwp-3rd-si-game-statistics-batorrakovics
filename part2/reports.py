def file_read(file_name):
    games_list = []
    with open(file_name, "r") as f:
        for line in f:
            games_list.append(line.strip().split("\t"))
    return games_list

# Report functions
def get_most_played(file_name):
    games_list = file_read(file_name)
    copies = []
    for sub_list in games_list:
        copies.append(float(sub_list[1]))
    maxcopies = max(copies)
    return(games_list[copies.index(maxcopies)][0])

def sum_sold(file_name):
    games_list = file_read(file_name)
    total = 0
    for sub_list in games_list:
        total += float(sub_list[1])
    return total

def get_selling_avg(file_name):
    games_list = file_read(file_name)
    copies = []
    for sub_list in games_list:
        copies.append(float(sub_list[1]))
    average = sum(copies) / len(games_list)
    return average


def count_longest_title(file_name):
    games_list = file_read(file_name)
    longest = ""
    titles = []
    count = 0
    for sub_list in games_list:
        titles.append(sub_list[0])
    for x in titles:
        if isinstance(x, str) and len(x) > len(longest):
            longest = x
    for letters in longest:
        count += 1
    return count
            

def get_date_avg(file_name):
    games_list = file_read(file_name)
    dates = []
    for sub_list in games_list:
        dates.append(int(sub_list[2]))
    average = sum(dates) / len(games_list)
    return round(average)

def get_game(file_name, title):
    games_list = file_read(file_name)
    number_of_games = -1
    for game in games_list:
        number_of_games += 1
        if game[0] == title:
            game[1] = float(game[1])
            game[2] = int(game[2])
            return games_list[number_of_games]
        


#get_most_played("game_stat.txt")
#sum_sold("game_stat.txt")
#get_selling_avg("game_stat.txt")
#count_longest_title("game_stat.txt")
#get_date_avg("game_stat.txt")
#get_game("game_stat.txt", "Minecraft")