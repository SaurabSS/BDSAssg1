import matplotlib.pyplot as plt
## Uncomment for WordCountPlot 
# x = [3, 6, 9, 12]
# y1 = [23328, 56345, 86295,102106]
# y2 = [3019, 5224, 5787, 10909]

# plt.bar(x, y1, color='r')
# plt.bar(x, y2, bottom=y1, color='b')
# plt.legend(["Mapper Time", "Reducer Time"], loc='upper left')
# plt.xlabel('thousand words')
# plt.ylabel('milliseconds')
# plt.title('WordCount Runtime Scaling')
# plt.show()

#Currently set to display TopN Runtimes

x = [4, 8, 12, 16]
y1 = [28335, 54939, 85551, 110659]
y2 = [3329, 4773, 5411, 11860]

plt.bar(x, y1, color='r')
plt.bar(x, y2, bottom=y1, color='b')
plt.legend(["Mapper Time", "Reducer Time"], loc='upper left')
plt.xlabel('twenty thousand words')
plt.ylabel('milliseconds')
plt.title('TopN Runtime Scaling')
plt.show()