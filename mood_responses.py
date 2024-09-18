def mood_response(mood):
    mood_response = {"happy": "I'm glad that you are happy today!", 
                     "mad": "I'm sorry that you are mad.", 
                     "sad": "I am sorry that you are sad.", 
                     "excited": "That is great that you are excited!"}
    if mood in mood_response.keys():
        return mood_response[mood]
    else:
        return f"You say that you are feeling {mood}...I'm not sure how to respond to that. Have a good day!"