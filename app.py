from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Import your assignments
try:
    from questions import get_all_assignments, get_assignment, calculate_score
except ImportError:
    # Fallback if questions.py doesn't exist
    def get_all_assignments():
        return {"assignment1": {"title": "Test Assignment", "questions": []}}
    
    def get_assignment(assignment_id):
        return {"title": "Test", "questions": []}
    
    def calculate_score(assignment_id, user_answers):
        return 0, 0

@app.route('/')
def index():
    try:
        assignments = get_all_assignments()
        return render_template('index.html', assignments=assignments)
    except Exception as e:
        return f"Error loading assignments: {str(e)}", 500

@app.route('/assignment/<assignment_id>')
def show_assignment(assignment_id):
    try:
        assignment = get_assignment(assignment_id)
        if not assignment:
            return "Assignment not found", 404
        return render_template('assignment.html', assignment=assignment, assignment_id=assignment_id)
    except Exception as e:
        return f"Error loading assignment: {str(e)}", 500

@app.route('/submit_assignment/<assignment_id>', methods=['POST'])
def submit_assignment(assignment_id):
    try:
        user_answers = {}
        for key, value in request.form.items():
            if key.startswith('q'):
                user_answers[key[1:]] = int(value)
        
        correct_count, total_questions = calculate_score(assignment_id, user_answers)
        
        return redirect(url_for('show_results', 
                              assignment_id=assignment_id,
                              correct=correct_count, 
                              total=total_questions))
    except Exception as e:
        return f"Error processing submission: {str(e)}", 500

@app.route('/results/<assignment_id>')
def show_results(assignment_id):
    try:
        assignment = get_assignment(assignment_id)
        if not assignment:
            return "Assignment not found", 404
        
        correct = request.args.get('correct', 0, type=int)
        total = request.args.get('total', 0, type=int)
        
        score = {
            'correct': correct,
            'total': total,
            'assignment_id': assignment_id
        }
        
        return render_template('results.html', 
                             assignment=assignment,
                             assignment_id=assignment_id,
                             score=score)
    except Exception as e:
        return f"Error showing results: {str(e)}", 500

@app.route('/health')
def health():
    return 'OK'

@app.route('/debug')
def debug():
    info = {
        'python_version': os.sys.version,
        'working_directory': os.getcwd(),
        'files_in_directory': os.listdir('.'),
        'templates_exists': os.path.exists('templates'),
        'static_exists': os.path.exists('static'),
    }
    return f"""
    <h1>Debug Information</h1>
    <pre>{info}</pre>
    <a href="/">Home</a>
    """

if __name__ == '__main__':
    print("Starting Flask application...")
    print(f"Current directory: {os.getcwd()}")
    print(f"Templates folder: {os.path.exists('templates')}")
    print(f"Static folder: {os.path.exists('static')}")
    app.run(debug=True, host='0.0.0.0', port=5000)