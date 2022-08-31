from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def display(boxes = 3, color='blue'):
    return render_template('play.html')

@app.route('/play/<int:boxes>')
def display_change(boxes, color='blue'):
    return render_template('play.html', boxes=boxes)

@app.route('/play/<int:boxes>/<color>')
def display_color_change(boxes, color):
    return render_template('play.html', boxes=boxes, color=color)

if __name__ == '__main__':
    app.run(debug=True, port=5001)