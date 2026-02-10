from programs import check_user as check
import datetime
import json

def create_account(*, userid, username):
    if check.check_user(userid):
        return "400"
    
    acc_json = {
        userid : {
            "username" : None,
            "points": 1000,
            "next_work_time": 0,
            "win_time" : 0,
            "lose_time" : 0,
            "played_time" : 0,
            "win_rate": 0
        },
    }

    acc_json[userid]["next_work_time"] = int(datetime.datetime.now().timestamp())
    acc_json[userid]["username"] = username

    try:
        with open("src/programs/user_data.json", "r") as f:
            user_data = json.load(f)
    except:
        user_data = {}


    user_data[userid] = acc_json[userid]

    with open("src/programs/user_data.json", "w") as f:
        json.dump(user_data, f, indent=4)

    return "success"
