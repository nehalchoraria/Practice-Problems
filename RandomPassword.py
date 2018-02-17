def randompassd(size):
    alphanum = string.ascii_letters + string.digits
    passd = ""
    for i in range(0,size):
        passd = passd + random.choice(alphanum)
    return passd

print(randompassd(13))