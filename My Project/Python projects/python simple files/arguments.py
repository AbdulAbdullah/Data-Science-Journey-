def gender_get(sex='Unknown'):
    if sex is 'm':
        sex = "male"
    elif sex is 'f':
        sex = "female"
    print(sex)


gender_get('m')
gender_get('f')
gender_get()
