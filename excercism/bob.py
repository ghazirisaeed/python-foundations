def response(hey_bob):


    if (hey_bob.strip() == "" or hey_bob == ""):
        response = 'Fine. Be that way!'
        return response 
    
    elif (str.isupper(hey_bob) and hey_bob[-1] == '?'):
        response = "Calm down, I know what I'm doing!"
        return response 
        
    elif ((hey_bob.strip(' ')[-1] == '?')):
        response = 'Sure.'
        return response 
        
    elif str.isupper(hey_bob):
        response = 'Whoa, chill out!'
        return response 
    
    else: 
        response = 'Whatever.'
        return response