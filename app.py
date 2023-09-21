# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
  
from gpt import generator
from pipeline import splitter, cleaner
import json

# creating a Flask app
app = Flask(__name__)
  

# returns Message when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "Welcome To Replicates Generator,\nPlease use post method to get results!"
        return jsonify({'data': data})
    
    elif request.method == 'POST':
        if request.json:
            try:
                sections = splitter.split_sections(request.json['text'])
            except ValueError:
                return jsonify({'error' : f"No text sent!\n{ValueError}"})
            
            try:
                text = cleaner.clean_english_text(sections[1])
                res = generator.generate_item(text)
            except:
                if len(text) > 4097:
                    return jsonify({'error' : f"Text has more than 4097 token"})
                else:
                    return jsonify({'error' : f"Bad predictions with generated list!"})
            
            try:
                items = res.choices[0].message.content
                items = json.loads(items)
            except:
                return jsonify({'error' : f"Failed to convert string to json!"})

            try:
                res = generator.suggest_item(res.choices[0].message.content)
                items['Suggested'] = json.loads(res.choices[0].message.content)['Suggested']
                return jsonify(items)
            
            except:
                return jsonify({'error' : f"Bad predictions with Suggested list!"})

        else:
            return jsonify({'error' : f"Bad request! No json file!"})



  

if __name__ == '__main__':
  
    app.run(debug = True, host='0.0.0.0', port=5000)