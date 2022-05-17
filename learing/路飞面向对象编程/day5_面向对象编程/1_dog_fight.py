
attack_vals = {
    "京巴":30,
    "藏獒": 80,
}


def dog(name,d_type): # 模版
    data = {
        "name":name,
        "d_type":d_type,
        "life_val":100,
    }
    if d_type in attack_vals:
        data["attack_val"] = attack_vals[d_type]
    else:
        data["attack_val"] = 15

    def dog_bite(person_obj):
        person_obj["life_val"] -= data["attack_val"]  # 执行咬人动作
        print("狗[%s]咬了人[%s]一口，人掉血[%s],还有血量[%s]..." % (data['name'],
                                                      person_obj["name"],
                                                      data["attack_val"],
                                                      person_obj["life_val"]))
    data["bite"] = dog_bite # 为了从函数外部可以调用 这个dog_bite方法

    return data


def person(name,age):
    data = {
        "name":name,
        "age": age,
        "life_val":100
    }
    if age > 18:
        data["attack_val"] = 50
    else:
        data["attack_val"] = 30

    def beat(dog_obj):
        dog_obj["life_val"] -= data["attack_val"]
        print("人[%s]打了狗[%s]一棒,狗掉血[%s],还有血量[%s]..." % (data["name"], dog_obj["name"],data["attack_val"],dog_obj["life_val"]))

    data["beat"]= beat
    return data


d1 = dog("mjj","京巴") # 实体, 实例化，
d2 = dog("mjj2","藏獒")


p1 = person("Alex",22)

d1["bite"](p1) # 咬人
d1["bite"](p1) # 咬人
d1["bite"](p1) # 咬人

p1["beat"](d1) # 打狗








