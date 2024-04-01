import streamlit as st
from classification import ClassifyComments
from scraping import CommentScraping
from analysis import CommentsAnalysis
from pathlib import Path



def main():
    st.title("Youtube Comments Analysis")

    st.markdown('Visualize what people are saying about your video!')

    st.text_input("Youtube Video Link", key="video_link")

    if st.button("Visualize"):     

        video_url = st.session_state.video_link

        comments = CommentScraping(video_url).get_comments()

        labels = ClassifyComments(comments).get_comments_labels()

        CommentsAnalysis(comments,labels).save_barplot()

        st.image(Path("src/image.png").as_posix(),use_column_width='auto')
    
if __name__ == "__main__":
    main()