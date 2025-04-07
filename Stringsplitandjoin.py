def split_and_join(line):
    line=line.split(" ")

    gg=""
    for i in line:
        if(gg==""):
            gg=i
        else:    
            gg+="-"+i
    return gg    

if __name__ == '__main__':
