


# 人狗大战，多条狗，多个人
#
# 狗能咬人，人能打狗
#
# 咬了或被打了都掉血
dog_attack_level = {
    "京巴":20,
    "藏獒":80,
    "平头哥":60
}


def dog(name,d_type):
    if d_type in dog_attack_level:
        d = {
            "name":name,
            "type":d_type,
            "life_val" :100
        }
    else:
        print("未知物种，不易接近")
        return None
    return d


def person(name,age,sex):
    d = {
        "name": name,
        "age": age,
        "sex":sex,
        "life_val": 100
    }
    if age > 18:
        d["attack_level"] = 50
    else:
        d["attack_level"] = 30
    return d


def bite(dog_obj,person_obj):
    person_obj["life_val"] -= dog_attack_level[dog_obj["type"]]
    print("疯狗[%s]咬了[%s],掉血[%s]..." %(dog_obj["name"], person_obj['name'], dog_attack_level[dog_obj["type"]]) )


def beat(person_obj,dog_obj):
    dog_obj["life_val"] -= person_obj['attack_level']
    print("[%s] 打了 疯狗[%s],狗掉血[%s]..." %(person_obj["name"], dog_obj["name"], person_obj["attack_level"]))


dog1 = dog("majj","平头哥")
dog2 = dog("二哈","京巴")

p1 = person("alex",22,"male")

bite(p1,dog1)

bite(dog1,p1)
beat(p1,dog2)

print(dog1,dog2)