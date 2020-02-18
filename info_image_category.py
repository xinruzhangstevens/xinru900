import json
with open("../data/annotations/instances_train2017.json","r") as f:
    temp = json.loads(f.read())
    image_id =[]
    image_category={}
    count = 0
    for dict in temp["annotations"]:
        count=count+1
        if(dict["image_id"] not in image_id):
            image_id.append(dict["image_id"])
            image_category.setdefault(dict["image_id"],[])
            image_category[dict["image_id"]].append(dict["category_id"])
        else:
            if(dict["category_id"] not in image_category[dict["image_id"]]):
                image_category[dict["image_id"]].append(dict["category_id"])
with open("./image_category_number.json","w") as ff:
    json.dump(image_category,ff)
