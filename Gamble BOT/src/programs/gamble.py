import random
import datetime
import math
from programs import points
import json
from programs import check_user as check

def play(*, bet, userid):
    with open("src/programs/user_data.json", "r") as f:
        data = json.load(f)

    if not check.check_user(userid):
        return "404"
    
    if bet < 1 or data[userid]["points"] < bet or data[userid]["points"] - bet < 0:
        return "403"
    
    x = random.randint(1, 85)
    y = random.randint(1, x)
    
    result = {
        "title" : None,
        "txt" : None,
        "probability" : None,
        "imgs" : None
        }

    result_copy = result.copy()

    if x == y:
        result_copy["title"] = "I Can't Stop Winning!!"
        result_copy["txt"] = "You won!"
        result_copy["probability"] = f"{math.floor(1/85 * 1/x * 10000) /100}%"
        result_copy["imgs"] = f"src/imgs/i_cant_stop_winning_{random.randint(1,5)}.png"
        win = True

    else:
        result_copy["title"] = "Aw Dang It!!"
        result_copy["txt"] = "You Lost!"
        result_copy["probability"] = f"{math.floor(1/85 * 1/x * 10000) /100}%"
        result_copy["imgs"] = "src/imgs/aw_dang_it.png"
        win = False

    point = points.play_update(bet=bet, userid=userid, win=win, probability=result_copy["probability"])
    result_copy["txt"] = f"{result_copy["txt"]}\nYour Point : {point}"

    return result_copy

def work(*, userid):
    with open("src/programs/user_data.json", "r") as f:
        data = json.load(f)
    
    if not check.check_user(userid):
        return "404"
    
    if int(datetime.datetime.now().timestamp()) > data[userid]['next_work_time']:
        return points.work_update(userid=userid)
    else:
        return "405"