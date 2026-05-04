def readPulse(fname):
    dataFile = open(fname, 'r')
    dataFile.readline()
    time = []
    absorption = []
    for line in dataFile.readlines():
        line = line.split(",")
        time.append(float(line[0]))
        absorption.append(float(line[1]))
    return time, absorption
