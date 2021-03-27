import requests
from bs4 import BeautifulSoup
import pandas as pd


def read_file():
    f = open("urls.txt", "r")
    all_urls = f.readlines()
    f.close()
    return all_urls


def run_code(tables, raw_game_details):
    loc_index = 2
    if "Spartanburg, SC" in raw_game_details:
        loc_index = 5

    counter = 0
    for table in tables:
        counter += 1
        if counter == loc_index:
            tab_data = [[cell.text for cell in row.find_all(["th", "td"])]
                        for row in table.find_all("tr")]
            df = pd.DataFrame(tab_data)
            df.columns = df.iloc[0, :]
            df.drop(index=0, inplace=True)
            return df


# I can build functions like these to get info about player
def get_highest_score_across_season(all_tables):
    playerDict = {}
    for each_table in all_tables:
        top_scorer = str(each_table["Player"][1][0:2].strip())
        num_of_points = int(each_table["PTS"][1])
        if top_scorer not in playerDict:
            playerDict[top_scorer] = num_of_points
        else:
            playerDict[top_scorer] += num_of_points
    dict(sorted(list(playerDict.items()), key=lambda item: item[1]))
    print("Highest Scorers: ")
    print(playerDict)

def get_highest_score_across_season_per_minute(all_tables):
    playerDict = {}
    minuteDict = {}
    for each_table in all_tables:
        top_scorer = str(each_table["Player"][1][0:2].strip())
        num_of_points = int(each_table["PTS"][1])
        num_of_minutes = int(each_table["MIN"][1])
        if top_scorer not in playerDict:
            playerDict[top_scorer] = num_of_points
            minuteDict[top_scorer] = num_of_minutes
        else:
            playerDict[top_scorer] += num_of_points
            minuteDict[top_scorer] += num_of_minutes
    for each_player in playerDict:
        playerDict[each_player] = playerDict[each_player]/minuteDict[each_player]
    dict(sorted(playerDict.items(), key=lambda item: item[1]))
    print("Highest Scorers Per Minute: ")
    print(playerDict)

def export_to_csv(all_tables):
    pd.concat(all_tables).to_csv('WBB_Data.csv')

def main():
    all_tables = []
    all_urls = read_file()
    for each_url in all_urls:
        page = requests.get(each_url.strip())
        print(page)
        soup = BeautifulSoup(page.content, 'html.parser')
        tables = soup.find_all("table")
        raw_game_details = str(soup.find_all("dd"))
        df = run_code(tables, raw_game_details)
        # print(df)
        all_tables.append(df)

    get_highest_score_across_season(all_tables)
    get_highest_score_across_season_per_minute(all_tables)
    export_to_csv(all_tables)
    print(all_tables)


if __name__ == "__main__":
    main()
