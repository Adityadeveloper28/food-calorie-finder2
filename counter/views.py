from django.shortcuts import render
import requests
import json

def home(request):
    if request.method == 'POST':
        query = request.POST['query']
        script_url = 'https://script.google.com/macros/s/AKfycbyBLf2cYFx5mLVmNRvXzB6veUEZaBoGXoqLwC8OYR8tx7oR2Or6XNquOIZa84cLDyYUWQ/exec'  # Replace 'your_script_id' with the actual script ID or deployment URL
        
        payload = {'query': query}
        api_request = requests.get(script_url, params=payload)
        
        try:
            api = json.loads(api_request.content)
            query_row = None
            for row in api['data']:  # Assuming the data is returned as a list of dictionaries, adjust this based on the actual structure
                if row['name'] == query:
                    query_row = row
                    break
            if query_row:
                print(query_row)
            else:
                print(f"No matching row found for query: {query}")
        except Exception as e:
            query_row = "Oops! There was an error"
            print(e)
        
        return render(request, 'home.html', {'query_row': query_row, 'content': True})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query', 'content': False})


#from django.shortcuts import render

# 4pu7O+2MUmpvgYfS4+Z0gg==PAujuMB29Am481mR
#def home(request):
  #import requests

 #import json
  
  #if request.method == 'POST':
          #query = request.POST['query']
          #api_url ='https://api.api-ninjas.com/v1/nutrition?query=' 
          #api_request = requests.get(api_url + query,headers={'X-Api-Key': '4pu7O+2MUmpvgYfS4+Z0gg==PAujuMB29Am481mR'})
         # try:
        #       api = json.loads(api_request.content)
       #        print(api_request.content)
      #    except Exception as e:
     #          api= "oops!theres was an error"
    #           print(e)
          
   #       return render(request , 'home.html',{'api':api,'content' : True} )
  #else:
  #        return render(request , 'home.html',{'query':'enter valid query','content': False} )