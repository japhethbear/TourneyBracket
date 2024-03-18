from flask import Flask, render_template

app = Flask(__name__)

# Route to render the bracket template
@app.route('/')
def index():
    # Pass the matchups data to the template
    firstFourMatchups = [
        ('Howard(16)', 'Wagner(16)'),
        ('Texas A&M(16)', 'Longwood(16)'),
        ('Virginia(11)', 'Colorado St(11)'),
        ('Boise St(11)', 'Colorado(11)'),
    ]
    matchups = {
        'East': [
            ('UConn(1)', 'Stetson(16)'),
            ('FAU(8)', 'Northwestern(9)'),
            ('San Diego St(5)', 'UAB(12)'),
            ('Auburn(4)', 'Yale(13)'),
            ('BYU(6)', 'Duquesne(11)'),
            ('Illinois(3)', 'Morehead St(14)'),
            ('Washington St(7)', 'Drake(10)'),
            ('Iowa State(2)', 'S Dakota St(15)'),
        ],
        'West': [
            ('North Carolina(1)', 'Howard/Wagner(16)'),
            ('Mississippi St(8)', 'Michigan St(9)'),
            ('Saint Marys(5)', 'Grand Canyon(12)'),
            ('Alabama(4)', 'Charleston(13)'),
            ('Clemson(6)', 'New Mexico(11)'),
            ('Baylor(3)', 'Colgate(14)'),
            ('Dayton(7)', 'Nevada(10)'),
            ('Arizona(2)', 'Long Beach St(15)'),
        ],
        'South': [
            ('Houston(1)', 'Longwood(16)'),
            ('Nebraska(8)', 'Texas A&M(9)'),
            ('Wisconsin(5)', 'James Madison(12)'),
            ('Duke(4)', 'Vermont(13)'),
            ('Texas Tech(6)', 'NC State(11)'),
            ('Kentucky(3)', 'Oakland(14)'),
            ('Florida(7)', 'Boise St/Colorado(10)'),
            ('Marquette(2)', 'Western KY(15)'),
        ],
        'Midwest': [
            ('Purdue(1)', 'Montana St/Grambling(16)'),
            ('Utah State(8)', 'TCU(9)'),
            ('Gonzaga(5)', 'McNeese(12)'),
            ('Kansas(4)', 'Samford(13)'),
            ('South Carolina(6)', 'Oregon(11)'),
            ('Creighton(3)', 'Akron(14)'),
            ('Texas(7)', 'Virginia/Colorado St(10)'),
            ('Tennessee(2)', 'Saint Peters(15)'),

        ]
    }
    return render_template('bracket.html', matchups=matchups)

if __name__ == '__main__':
    app.run(debug=True)