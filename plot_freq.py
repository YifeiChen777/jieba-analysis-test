import matplotlib.pyplot as plt
def extract_idf(filename):
    idf = []
    with open(filename,"r") as f:
        lines = f.readlines()
        for line in lines:
            idf.append(line.split()[1])
    return idf

def plot_idf(idf_lst):
    plt.plot(idf_lst)
    plt.ylabel('freq')
    plt.show()

if __name__ == "__main__":
    idf_lst = extract_idf("small_idf.txt")
    plot_idf(idf_lst)