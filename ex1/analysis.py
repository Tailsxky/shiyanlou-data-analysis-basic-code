import json

def analysis(file, user_id):
    times = 0
    minutes = 0

    # check if the file exists, if yes save as json data.
    if(not file):
        return 0
    else:
        with open(file) as f:
            jsonData = json.load(f)

    #loop the json file if the user_id exists, times+1, minutes added. 
    for i in jsonData:
        if(i['user_id'] == user_id):
            times += 1
            minutes += i['minutes']
            

    if(times!=0):
        return times, minutes
    else:
        return 0
    
        
#print(analysis('../user_study.json', 199071))