##src models 
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, hamming_loss, f1_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


import pickle

def build_pipeline(model_name):
    if model_name == 'LogisticRegression':
        return Pipeline([
                ('tfidf', TfidfVectorizer(stop_words=stop_words)),
                ('clf', OneVsRestClassifier(LogisticRegression(solver='sag'), n_jobs=1)),
            ])
    elif model_name == 'MultinomialNB':
        return Pipeline([
                ('tfidf', TfidfVectorizer(stop_words=stop_words)),
                ('clf', OneVsRestClassifier(MultinomialNB(
                    fit_prior=True, class_prior=None))),
            ])
    else:
        raise RuntimeError('Current OnevsRest pipeline supported only for Logstic and NB')

def save_model(model,filename):
    pickle.dump(model, open(filename, 'wb'))

def build_model_eval(X_train, X_test, train, test, model_name, labels,model_filepath):
    '''Builds OneVsRest strategy based models and generate eval report'''
    prediction_labels = []
    validation_df = []
    for label in labels:
        print('{0} Classifier running for: {1}'.format(model_name,label))
        # train the model using X_dtm & y
        model_pipeline = build_pipeline(model_name)
        model_pipeline.fit(X_train, train[label])
        #save model
        save_model(model_pipeline,model_filepath + '_' + label + '.pkl')
        print('Saved model onto path {}'.format(model_filepath))
        # compute the testing accuracy
        prediction = model_pipeline.predict(X_test)
        test[label+ '_' + model_name + '_prediction'] = prediction
        prediction_labels.append(label+ '_' + model_name + '_prediction')
        accuracy_ = accuracy_score(test[label], prediction)
        f1_score_ = f1_score(test[label], prediction)
        print('Test accuracy is {}'.format(accuracy_))
        print('Test f1-score is {}'.format(f1_score_))
        validation_df.append([model_name,label,accuracy_,f1_score_])
    hamming_loss_ = hamming_loss(test[labels],test[prediction_labels])
    return test, validation_df, hamming_loss_