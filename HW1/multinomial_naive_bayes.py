import numpy as np
from linear_classifier import LinearClassifier


class MultinomialNaiveBayes(LinearClassifier):

    def __init__(self):
        LinearClassifier.__init__(self)
        self.trained = False
        self.likelihood = 0
        self.prior = 0
        self.smooth = True
        self.smooth_param = 1
        
    def train(self, x, y):
        # n_docs = no. of documents
        # n_words = no. of unique words    
        n_docs, n_words = x.shape
        
        # classes = a list of possible classes
        classes = np.unique(y)
        
        # n_classes = no. of classes
        n_classes = np.unique(y).shape[0]
        
        # initialization of the prior and likelihood variables
        prior = np.zeros(n_classes)
        likelihood = np.zeros((n_words,n_classes))

        # TODO: This is where you have to write your code!
        # You need to compute the values of the prior and likelihood parameters
        # and place them in the variables called "prior" and "likelihood".
        # Examples:
            # prior[0] is the prior probability of a document being of class 0
            # likelihood[4, 0] is the likelihood of the fifth(*) feature being 
            # active, given that the document is of class 0
            # (*) recall that Python starts indices at 0, so an index of 4 
            # corresponds to the fifth feature!
        
        ###########################


        # YOUR CODE HERE
        total_documents = np.zeros(n_classes) #number of documents per class
        word0 = np.zeros(n_words) #number of words for class o
        word1 = np.zeros(n_words) #number of words for class 1
        for i in range(n_docs):
            if y[i]==0: #check if document belongs to class 0
                total_documents[0] +=1 #increase the counter of class 0
                for j in range(n_words): 
                    word0[j]+=x[i][j] #creates a arrray of all words in class 0
            else:  #check if document belongs to class 1
                total_documents[1] +=1 #increase the counter of class 1
                for j in range(n_words):
                    word1[j]+=x[i][j]    #creates a arrray of all words in class 1
                    
   
         #prior is
        prior[0] = 1.0 * total_documents[0]/ n_docs
        prior[1] = 1.0 * total_documents[1]/ n_docs
        
        #likelihood
        for i in range(n_words):
            likelihood[i][0]= (word0[i]+self.smooth_param)/(word0.sum()+self.smooth_param*n_words)
            likelihood[i][1]= (word1[i]+self.smooth_param)/(word1.sum()+self.smooth_param*n_words)


        ###########################

        params = np.zeros((n_words+1,n_classes))
        for i in range(n_classes): 
            # log probabilities
            params[0,i] = np.log(prior[i])
            with np.errstate(divide='ignore'): # ignore warnings
                params[1:,i] = np.nan_to_num(np.log(likelihood[:,i]))
        self.likelihood = likelihood
        self.prior = prior
        self.trained = True
        return params
