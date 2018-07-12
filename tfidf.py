from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

document = re.sub(‘[^A-Za-z .-]+’, ‘ ‘, document)
document = document.replace(‘-’, ‘’)
document = document.replace(‘…’, ‘’)
document = document.replace(‘Mr.’, ‘Mr’).replace(‘Mrs.’, ‘Mrs’

count_vect = count_vect.fit(train_data)
freq_term_matrix = count_vect.transform(train_data)

