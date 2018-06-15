from flask import Flask
from flask import request
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/update/<sound>/<inst>/<volume>')
def update_sound(sound,inst,volume):
    # show the user profile for that user
    inst_int = int(inst)
    volume_float = float(volume)
    save_file(sound,inst_int,volume_float)
    return 'User %s%d%2.1f' % (sound,inst_int,volume_float)

@app.route('/post', methods=['POST'])
def save_post():
    # show the post with the given id, the id is an integer
    k1 = request.form['k1']
    k2 = request.form['k2']
    k3 = request.form['k3']
    sound = str(k1)
    inst_int = int(k2)
    volume_float = float(k3)
    save_file(sound,inst_int,volume_float)
    return "Come!"

def save_file(sound,inst_int,volume_float):
    f = open('fuga.json','w')
    d = {'k1': sound, 'k2': inst_int, 'k3': volume_float}
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
