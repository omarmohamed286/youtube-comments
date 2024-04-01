# youtube-comments

![Screenshot_227](https://github.com/omarmohamed286/youtube-comments/assets/125928590/0216869b-e9fc-483b-a53b-44eeccf39932)

In this project i used streamlit for UI, i take from the user a link of a youtube video, i do web scraping using selenium to get the comments of the video then i do text classification
to all the comments using roberta model from huggingface
and then return a barplot that shows people sentiment about the video.

## Usage

``` streamlit run src/main.py ```
