import traceback
try:
    validate_max=33000
    train_max=80000
    fp = open("./2024-01/position_names_tags.txt",'r')
    train = open("./2024-01/train.txt","w")
    validate = open("./2024-01/validate.txt","w")
    test = open("./2024-01/test.txt","w")
    for i,l in enumerate(fp):
        print(i,l)
        if i <= validate_max:
            validate.write(l)
        elif i > validate_max and i <= train_max:
            train.write(l)
        else:
            test.write(l)
    fp.close()
    train.close()
    validate.close()
    test.close()

except Exception as e:
    print(e)
    print(traceback.format_exc())


