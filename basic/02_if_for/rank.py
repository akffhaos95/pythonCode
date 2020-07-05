import json

rank_file_path = './basic/02_if_for/rank.json'

def insertRank(name, point):
    with open(rank_file_path, "rt") as json_file:
        json_data = json.load(json_file)
    json_data['rank'].append({
        "name": name,
        "point": point
    })
    with open(rank_file_path, 'wt') as outfile:
        json.dump(json_data, outfile, indent=4)

def loadRank():
    with open(rank_file_path, "rt") as json_file:
        json_data = json.load(json_file)
    json_data = json_data['rank']
    json_data = sorted(json_data, key=lambda k: k['point'], reverse=True)
    for i in range(0, 5):
        print(i+1,"위 : ", json_data[i]['name'], " 점수 : ", json_data[i]['point'])
    print("")
