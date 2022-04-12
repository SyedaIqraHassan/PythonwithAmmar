import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
titanic=sns.load_dataset("titanic")
p1=sns.countplot(x="sex",hue="class",data=titanic)
plt.suptitle("Plot for counting")
plt.show()