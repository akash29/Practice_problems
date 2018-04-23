from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
docs = ["I'd like an apple","An apple a day keeps the doctor away","Never compare an apple to an orange",
        "I prefer scikit-learn to orange"]

tfidf = TfidfVectorizer().fit_transform(docs)

val = (tfidf*tfidf.T).A[0][1:]
print(val)
print(np.argmax(val)+2)
