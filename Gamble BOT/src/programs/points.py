import json
import datetime
import math
from programs import check_user as check

def play_update(*, bet, userid, win, probability):
    with open("src/programs/user_data.json", "r") as f:
        data = json.load(f)

    user_data = data[str(userid)]
    probability = float(probability.replace("%", ""))
    
    if win == True:
        if probability <= 0.03:
            points = bet * 10
        
        elif probability <= 0.25:
            points = bet * 5
            
        elif probability <= 0.50:
            points = bet * 3
            
        elif probability <= 1.17:
            points = bet * 2

        user_data["points"] += points
        user_data["win_time"] += 1
        user_data["played_time"] += 1
        user_data["win_rate"] = math.floor(user_data["win_time"] / user_data["played_time"] * 100) / 100

    else:
        user_data["points"] -= bet
        user_data["lose_time"] += 1
        user_data["played_time"] += 1
        user_data["win_rate"] = math.floor(user_data["win_time"] / user_data["played_time"] * 100) / 100

    data[str(userid)] = user_data
    with open("src/programs/user_data.json", "w") as f:
        json.dump(data,f, indent=4)

    return user_data["points"]

def work_update(*, userid):
    with open("src/programs/user_data.json", "r") as f:
        data = json.load(f)

    point_data = data[str(userid)]
    point_data["points"] += 1000
    nexttime = datetime.datetime.now() + datetime.timedelta(hours=2)
    point_data["next_work_time"] = int(nexttime.timestamp())

    data[str(userid)] = point_data

    with open("src/programs/user_data.json", "w") as f:
        json.dump(data, f, indent=4)

    return point_data["next_work_time"]

def get_user_info(*, userid):

    with open("src/programs/user_data.json", "r") as f:
        data = json.load(f)

    if check.check_user(userid):
        return data[userid]
    return "404"


                
