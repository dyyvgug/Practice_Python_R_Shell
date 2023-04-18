#!/usr/bin/python
# coding: utf-8

import random


def gen_fake():
    candidate = []
    for i in range(0, 50):
        nameSet = "Tom,Aralan,Numus,Jack,Amy,Simon,Kate,Bekky,Schween,Criti,Saruman,Spartz,ikarus,Frank,Manny,White,Karadual,Kare,Arts,Medical,Snow,Noble,Witch,Nafiz,dikkie,Alexl,Blade,Mo,Fata,Pad,Gandalf,Sauranar,Pizza"
        name = nameSet.split(",")
        choName = name[int(random.random() * len(name))]
        # print(choName)

        choAge = random.randint(16, 40)

        country = ["Sweden", "China", "Thailand", "Germany", "UK", "Canada", "France", "Spain", "Singapore", "Russia"]
        choCou = country[int(random.random() * len(country))]

        education = ["senior high school", "Bachelor Degree", "Master Degree", "PhD Degree "]
        choEdu = education[int(random.random() * len(education))]

        person = {"name": choName, "age": choAge, "country": choCou, "education": choEdu, "aim": choCou + "&" + choEdu}
        candidate.append(person)
    print(candidate)

    count = 0
    for i in candidate:
        for j in candidate:
            if i == j:
                continue
            else:
                if i["aim"].split("&")[0] == j["country"] and i["aim"].split("&")[1] == j["education"]:
                    print("{} and {} match successfully".format(i["name"], j["name"]))
                    count += 1
                    break
    print("%d pairs match successfully" % count)


if __name__ == "__main__":
    gen_fake()
