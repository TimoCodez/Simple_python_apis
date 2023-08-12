from flask import Flask

app = Flask(__name__)

@app.route('/items', methods=['GET'])
def get_items():
    return {'items': ['item1', 'item2']}

if __name__ == '__main__':
    app.run()