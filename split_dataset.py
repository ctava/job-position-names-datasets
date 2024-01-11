import traceback
try:
    train_max=400
    t = open("./2024-01/position_names_tags.txt",'r')
    train = open("./2024-01/train.txt","w")
    test = open("./2024-01/test.txt","w")
    for i,l in enumerate(t):
        if i <= train_max:
            train.write(l)
        else:
            test.write(l)
    t.close()
    train.close()
    test.close()

except Exception as e:
    print(e)
    print(traceback.format_exc())


