import matplotlib.pyplot as plt
def extract_idf(filename):
    idf = []
    index = []
    i = 1
    with open(filename,"r") as f:
        lines = f.readlines()
        for line in lines:
            index.append(i)
            i += 1
            idf.append(line.split()[1])
    return idf, index

def plot_idf(idf_lst, index):
    idf_lst.sort(reverse=True)
    plt.scatter(index, idf_lst, s=0.01)
    plt.ylabel('freq')
    plt.gca().invert_yaxis()
    plt.show()

if __name__ == "__main__":
    idf_lst, index = extract_idf("static/idf/chi_small_idf.txt")
    plot_idf(idf_lst, index)