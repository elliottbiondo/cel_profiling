import matplotlib as mpl
import matplotlib.pyplot as plt

# Times font everywhere
mpl.rcParams["font.family"] = "serif"
mpl.rcParams["font.serif"] = ["Times New Roman", "Times", "Nimbus Roman", "DejaVu Serif"]
mpl.rcParams["mathtext.fontset"] = "stix"

# Data taken from the bih_metadata section 
num_finite_bboxes = [
534, 1, 416, 17, 16, 16, 6, 9, 9, 64, 3, 15,
1536, 1536, 1536, 1536, 1536, 1536, 1536, 1536, 1536, 1536, 1536, 1536, 1536,
1536, 1536, 1536, 1536, 1536, 1536, 1536, 1536, 2, 2, 0, 0, 1, 1, 1, 1, 1, 2,
2, 0, 0, 9, 30, 7, 7, 30, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 5, 5, 12276, 10216, 8248, 512,
512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 512, 2, 2, 2,
2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 9, 9, 8, 8,
8, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 30, 7, 7]

num_infinite_bboxes = [
15, 1, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 8, 8, 1, 1, 1, 1, 1, 1, 1, 8, 8, 1, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
96, 32, 32, 96, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 0, 0, 0]


fig, ax = plt.subplots()

ax.hist(num_finite_bboxes, bins=100) 
ax.set_xlabel("Number of finite bounding boxes")
ax.set_ylabel("Number of universes")

ax.set_yscale("log")

plt.savefig("num_bboxes.pdf", bbox_inches="tight")
