import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS

def show_barplot(x,y,title,xlabel,ylabel):
    '''creates barplot for specified x,y'''
    sns.set(font_scale = 1.5)
    sns.set_style('whitegrid') 
    plt.figure(figsize=(10,6))
    sns.barplot(x, y)
    plt.title(title, fontsize=24)
    plt.ylabel(ylabel, fontsize=18)
    plt.xlabel(xlabel, fontsize=18)
    plt.show()
    

def show_wordcloud(text):
    '''creates wordcloud for input text'''
    plt.figure(figsize=(40,25))
    cloud = WordCloud(
                              stopwords=STOPWORDS,
                              background_color='black',
                              collocations=False,
                              width=2500,
                              height=1800
                             ).generate(" ".join(text))
    plt.axis('off')
    plt.title("Word cloud representation",fontsize=40)
    plt.imshow(cloud)