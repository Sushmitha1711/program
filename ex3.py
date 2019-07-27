try:
    with open("data1.txt") as f:
        lines=f.readlines()
        for line in lines:
            print(line,end="")

except Exception as e:
    print(f"file not found please check path {e}")