from flask import Flask, render_template, request, session, redirect, url_for
from questions import get_all_assignments, get_assignment, calculate_score
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this in production

@app.route('/')
def index():
    assignments = get_all_assignments()
    return render_template('index.html', assignments=assignments)

@app.route('/assignment/<assignment_id>')
def show_assignment(assignment_id):
    assignment = get_assignment(assignment_id)
    if not assignment:
        return "Assignment not found", 404
    
    return render_template('assignment.html', assignment=assignment, assignment_id=assignment_id)

@app.route('/submit_assignment/<assignment_id>', methods=['POST'])
def submit_assignment(assignment_id):
    user_answers = {}
    for key, value in request.form.items():
        if key.startswith('q'):
            user_answers[key[1:]] = int(value)
    
    correct_count, total_questions = calculate_score(assignment_id, user_answers)
    
    # Store results in session
    session['last_score'] = {
        'correct': correct_count,
        'total': total_questions,
        'assignment_id': assignment_id
    }
    
    return redirect(url_for('show_results', assignment_id=assignment_id))

@app.route('/results/<assignment_id>')
def show_results(assignment_id):
    assignment = get_assignment(assignment_id)
    if not assignment:
        return "Assignment not found", 404
    
    last_score = session.get('last_score', {})
    
    return render_template('results.html', 
                         assignment=assignment,
                         assignment_id=assignment_id,
                         score=last_score)

if __name__ == '__main__':
    app.run(debug=True, port=5000)