def dobaDana(h):
    if(h>=6 and h<=9):
        return "jutro"
    elif(h<=11):
        return "prijepodne"
    elif(h<=16):
        return "poslijepodne"
    elif(h<=20):
        return "vecer"
    else:
        return "noc"