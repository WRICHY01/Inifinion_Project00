from azure.core.credentials import  AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from api_and_endpoint import API_KEY, END_POINT

# Function to analyze sentiment
def sentiment_analysis():
    """ Creating a client object using the end point and api key for access """
    try:
        response = TextAnalyticsClient(endpoint = END_POINT, 
                                                credential = AzureKeyCredential(API_KEY))
        print("client created successfully")
        return response
    except Exception as e:
        print(e)


sentiment_analysis()
