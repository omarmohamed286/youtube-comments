#import pandas as pd
import seaborn as sns
from pathlib import Path

class CommentsAnalysis:
    def __init__(self,comments,labels):
        self.comments = comments
        self.labels = labels

    # def get_textual_analysis(self):
    #     texts = []
    #     labels_df = pd.DataFrame(self.labels)
    #     comments_counts = dict(labels_df.value_counts())
    #     for key,value in comments_counts.items():
    #         noun = "People" if value > 1 else "Person"
    #         verb = "have" if value > 1 else "has"
    #         texts.append(f"{value}  {noun} {verb} {key} feeling towards the video")
    #     return texts

    def save_barplot(self):
        sns.set_palette("Set1")
        barplot = sns.barplot(self.labels)
        fig = barplot.get_figure()
        fig.savefig(Path("src/image.png").as_posix())



