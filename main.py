from sentiment_analysis import sentiment_analysis
from sentiment_text import customer_reviews

clients = sentiment_analysis()
responses = clients.analyze_sentiment(customer_reviews, 
                                   language = "en-US",
                                   show_opinion_mining = True)


reviews = [review for review in responses if not review.is_error]

positive_count = 0
neutral_count = 0
negative_count = 0

for review in reviews:
    print("Sentiment Analysis Output: {}".format(review.sentiment))
    print("Overall Review Score: positive_reviews = {}; neutral = {}; negative = {}".format(review.confidence_scores.positive,
                                                                                     review.confidence_scores.neutral,
                                                                                     review.confidence_scores.negative))
    
    # Performing Sentence Analysis
    sentences = review.sentences
    for i, sentence in enumerate(sentences):
        print("Sentence #{}".format(i + 1))
        print("{}".format(sentence.text))
        # print("{}".format(customer_reviews[i]))
        print("Sentence Score: positive = {}; neutral = {}; negative = {}".format(sentence.confidence_scores.positive,
                          sentence.confidence_scores.neutral,
                          sentence.confidence_scores.negative))
        

        for count in sentences:
            if sentence.confidence_scores.positive > 0.5:
                positive_count  += 1
            if sentence.confidence_scores.neutral > 0.5:
                neutral_count += 1
            if sentence.confidence_scores.negative > 0.5:
                negative_count += 1
      

    
    # Opinion mining results
        for mined_opinion in sentence.mined_opinions:  
            target = mined_opinion.target
            print("\t '{}'; target text: {}".format(target.sentiment, target.text))
            print("\t Target Score: \n\t Positive = {}\n\t Neutral = {} \n\t Negative = {}".format(target.confidence_scores.positive,
                                                                                target.confidence_scores.neutral,
                                                                                target.confidence_scores.negative))
            
            for assessment in mined_opinion.assessments:
                # eval = assessment.assessments
                print("\t'{}'; assessment text = {}".format(assessment.sentiment, assessment.text))
                print("Assessment Score: Positive = {} \n\t Neutral = {} \n\t Negative = {}".format(assessment.confidence_scores.positive,
                                                                                                    assessment.confidence_scores.neutral,
                                                                                                    assessment.confidence_scores.negative))




sum = positive_count + neutral_count + negative_count

positive = (positive_count / sum) * 100

neutral = (neutral_count / sum) * 100

negative = (negative_count / sum) * 100
    
print("Positive sentences(%): {:.2f}, Neutral sentences(%): {:.2f}, Negative sentences(%): {:.2f}".format(positive,
                                                                                              neutral, 
                                                                                              negative))
