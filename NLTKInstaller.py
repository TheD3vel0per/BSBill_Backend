import nltk
import os

DOWNLOAD_DIR = "/home/appuser/nltk_data"

if __name__ == "__main__":
    # os.mkdir("/home/appuser/nltk_data")
    os.mkdir("/home/appuser")
    os.mkdir("/home/appuser/nltk_data")
    nltk.download(info_or_id="averaged_perceptron_tagger", download_dir=DOWNLOAD_DIR)
    nltk.download(info_or_id="punkt", download_dir=DOWNLOAD_DIR)