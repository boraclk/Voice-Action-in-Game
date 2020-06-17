import azure.cognitiveservices.speech as speechsdk
import keyboard
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials
import time

speech_key, service_region = "YourSubscriptionKey", "YourServiceRegion"
speech_config = speechsdk.SpeechConfig(subscription="bc480babbcec4a32a9acdb461c84e606", region="westeurope")


LUIS_RUNTIME_KEY="efddc02669c14fe8b5a1ad046848803b"
LUIS_RUNTIME_ENDPOINT="https://voiceluis.cognitiveservices.azure.com/"
LUIS_APP_ID="73ac9d1d-e73f-486d-b660-b37b70dace34"
LUIS_APP_SLOT_NAME="staging"
clientruntime=LUISRuntimeClient(LUIS_RUNTIME_ENDPOINT,CognitiveServicesCredentials(LUIS_RUNTIME_KEY))

def predict(text):

    request  = {"query" : text}
    response = clientruntime.prediction.get_slot_prediction(app_id=LUIS_APP_ID,slot_name=LUIS_APP_SLOT_NAME,prediction_request=request)

    print("luis result: {}".format(response.prediction.top_intent))
    outluis=response.prediction.top_intent
    action(outluis)

troops=["Cavalry","Infantry","Archers","All"]
commands=["Attack","Follow","Wait","Back","Move"]

def action(action):
    
    for var in troops:
        if var==action:
            troop(action)     
    for var in commands:
        if var==action:
            keyboard.press_and_release('f1')
            time.sleep(0.1)
            command(action)

def listen():

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    print("Say something...")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print(format(result.text))
            predict(format(result.text))
    elif result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))

def troop(troop):

    if(troop=="Cavalry"):
        keyboard.press_and_release('3')
    elif(troop=="Infantry"):
        keyboard.press_and_release('1')
    elif(troop=="Archers"): 
        keyboard.press_and_release('2')
    elif(troop=="All"):
        keyboard.press_and_release('0')
        
    listen()

def command(command):    

    if(command=="Attack"):
        keyboard.press_and_release('f3')
    elif(command=="Follow"):
        keyboard.press_and_release('f2')
    elif(command=="Move"):
        keyboard.press_and_release('f1')
    elif(command=="Wait"):  
        keyboard.press_and_release('f6')
    elif(command=="Back"):
        keyboard.press_and_release('f5')
    
       
        

while(1):
    if keyboard.is_pressed("r"):        
       listen()
    elif keyboard.is_pressed("k"):
        break   
                
                
        