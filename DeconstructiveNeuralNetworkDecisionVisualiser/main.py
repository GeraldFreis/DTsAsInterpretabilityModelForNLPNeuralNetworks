from visualising_paragraphs import *
from visualising_sentences import *
import keras 
import pandas

# reading in our DF and CNN
CNN = keras.models.load_model("../CNN_Non_Dense/")
paragraphs = pandas.read_csv("../Datasets/IMDB.csv")
sentences = pandas.read_csv("../Datasets/IMDB_sentences.csv")


TreeVisualiser_sentences(3, sentences, 23, CNN)
# TreeVisualiser_paragraphs(4, paragraphs, 2, CNN)