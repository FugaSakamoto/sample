from flask import Flask
from flask import request
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/update/<inst>/<reverb>/<volume>')
def update_sound(inst,reverb,volume):
    # show the user profile for that user
    inst_str = str(inst)
    reverb_int = int(reverb)
    volume_str = str(volume)
    save_file(inst_str,reverb_int,volume_str)
    return 'User %s%d%2.1f' % (inst_str,reverb_int,volume_str)

@app.route('/post', methods=['POST'])
def save_post():
    # show the post with the given id, the id is an integer
    inst = request.form['inst']
    reverb = request.form['reverb']
    volume = request.form['volume']
    inst_str = str(inst)
    reverb_int = int(reverb)
    volume_str = str(volume)
    save_file(inst_str,reverb_int,volume_str)
    return "Come!"

def save_file(inst_str,reverb_int,volume_str):
    f = open('fuga.json','w')
    d = {'inst_str': inst, 'reverb_int': reverb, 'volume_str': volume}
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
