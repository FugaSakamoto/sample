from flask import Flask
from flask import request
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/update/<sound>/<reverb>/<volume>')
def update_sound(sound,reverb,volume):
    # show the user profile for that user
    sound_str = str(sound)
    reverb_float = float(reverb)
    volume_str = str(volume)
    save_file(sound_str,reverb_float,volume_str)
    return 'User %s%d%s' % (sound_str,reverb_float,volume_str)

@app.route('/post', methods=['POST'])
def save_post():
    print request.form[0]
    # show the post with the given id, the id is an integer
    sound = request.form['sound']
    reverb = request.form['reverb']
    volume = request.form['volume']
    sound_str = str(sound)
    reverb_float = float(reverb)
    volume_str = str(volume)
    save_file(sound_str,reverb_float,volume_str)
    return "Come!"

def save_file(sound_str,reverb_float,volume_str):
    f = open('fuga.json','w')
    d = {'sound_str': sound_str, 'reverb_float': reverb_float, 'volume_str': volume_str}
    json.dump(d,f)
    f.close()

# save_file("test1","test2")

@app.route("/get")
def get():
    d3 = get_file()
    return d3

def get_file():
    f2 = open('fuga.json','r')
    d2 = json.load(f2)
    print "Here!"
    str1 = json.dumps(d2)
    return str1

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
