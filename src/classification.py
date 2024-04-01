from transformers import pipeline

pipe = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions")


class ClassifyComments:
    def __init__(self,comments):
        self.comments = comments

    def get_comments_labels(self):
        labels = []
        for comment in self.comments:
            labels.append(pipe(comment)[0]['label'])
        return labels