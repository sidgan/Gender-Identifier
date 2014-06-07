#!/usr/bin/python



def gender_features(word):
	return { 'last_letter' : word[-1] }
#end

 

 
import random
import nltk 


names = ([(name,'male') for name in ('C:\Users\ANMOL\Desktop\male.txt')] + [(name,'female') for name in ('C:\Users\ANMOL\Desktop\female.txt')])




random.shuffle(names)
featuresets = [(gender_features(n),g) for (n,g) in names]
from nltk.classify import apply_features 
train_set = apply_features(gender_features,names[86:])
test_set = apply_features(gender_features, names[:85])
classifier = nltk.NaiveBayesClassifier.train(train_set)

print classifier.classify(gender_features('ravi'))


print nltk.classify.accuracy(classifier, test_set)

classifier.show_most_informative_features(5)

