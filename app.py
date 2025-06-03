from flask import Flask, render_template
import pandas as pd
from datetime import date

app = Flask(__name__)
csv_path = 'data/daily_texts.csv'
daily_cache = {}

def get_today_texts():
    today = date.today().isoformat()
    if today not in daily_cache:
        df = pd.read_csv(csv_path)
        df['date'] = df['date'].astype(str).str.strip()  # Strip whitespace & convert to string
        print("Available dates in CSV:", df['date'].tolist())  # Debug print
        row = df[df['date'] == today]
        if row.empty:
            print(f"No entry found for date: {today}")
            return None
        daily_cache[today] = row.iloc[0]
    return daily_cache[today]


@app.route('/fortune')
def fortune():
    data = get_today_texts()
    print(data)
    return render_template('fortune.html', title='Daily Fortune', text="Unexpected blessings await you.")#data['fortune'])

@app.route('/motivation')
def motivation():
    data = get_today_texts()
    return render_template('motivation.html', title='Daily Motivation', text=data['motivation'])

@app.route('/kuran')
def kuran():
    data = get_today_texts()
    return render_template('kuran.html', title='Kuran Ayet', text=data['kuran'])

@app.route('/meditation')
def meditation():
    data = get_today_texts()
    return render_template('meditation.html', title='Meditation Prompt', text=data['meditation'])

if __name__ == '__main__':
    app.run(debug=True)
