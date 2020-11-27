def extract_idf(filename):
    idf = []
    with open(filename,"r") as f:
        lines = f.readlines()
        for line in lines:
            idf.append(line.split()[1])
    return idf

if __name__ == "__main__":
    idf_lst = extract_idf("small_idf.txt")