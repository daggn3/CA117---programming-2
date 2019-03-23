def read(filename):

    infile = open(filename, "r")
    profile_list = infile.readlines()
    for i in range(len(profile_list)):
        profile_list[i] = profile_list[i].rstrip('\n')
    infile.close()
    return profile_list