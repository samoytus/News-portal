from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def censored_title(self):
        # Your custom censor filter logic goes here
        # This is just a placeholder, you should implement your own logic
        unwanted_words = ['блять', 'badword2']
        censored_title = self.title
        for word in unwanted_words:
            censored_title = censored_title.replace(word, '*' * len(word))
        return censored_title

    def censored_text(self):
        # Similar to the censored_title method, implement your censor filter logic for text
        # This is just a placeholder
        unwanted_words = ['badword1', 'badword2']
        censored_text = self.text
        for word in unwanted_words:
            censored_text = censored_text.replace(word, '*' * len(word))
        return censored_text