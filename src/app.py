import matplotlib.pyplot as plt
from readit_all import readit_all
from process import process

data = readit_all("data/penguins.csv")
X, Y, Z = process(data)
z_label = "species"
species = set([d[z_label] for d in data])


for s in species:
  X_subset=[x_sub for x_sub,z_sub in zip(X,Z) if z_sub==s]
  Y_subset=[y_sub for y_sub,z_sub in zip(Y,Z) if z_sub==s]

  # another way that does the same thing as 2 lines above
  X_subset = [d for i, d in enumerate(X) if s == Z[i]]
  Y_subset = [d for i, d in enumerate(Y) if s == Z[i]]

  plt.scatter(X_subset, Y_subset, label=s)

plt.xlabel('Bill Length (mm)')
plt.ylabel('Flipper Length (mm)')
plt.title('Species by Bill and Flipper Length')
plt.legend()


plt.savefig("figs/penguin.png")
plt.show()