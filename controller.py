from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/')
def Home():
    return render_template('register.html')


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    if request.method == 'POST':
        # Collect all submitted answers
        submitted_answers = request.form.to_dict()
        
        # Example: Predefined correct answers for validation
        correct_answers = {
             'python_q1': 'c',
        'python_q2': 'a',
        'python_q3': 'a',
        'python_q4': 'c',
        'python_q5': 'b',
        'python_q6': 'b',
        'python_q7': 'b',
        'python_q8': 'c',
        'python_q9': 'a',
        'python_q10': 'c',
        'computing_q1': 'b',
        'computing_q2': 'c',
        'computing_q3': 'b',
        'computing_q4': 'c',
        'computing_q5': 'a',
        'computing_q6': 'b',
        'computing_q7': 'c',
        'computing_q8': 'b',
        'computing_q9': 'b',
        'computing_q10': 'b',
        'linear_q1': 'c',
        'linear_q2': 'b',
        'linear_q3': 'b',
        'linear_q4': 'a',
        'linear_q5': 'b',
        'linear_q6': 'a',
        'linear_q7': 'a',
        'linear_q8': 'c',
        'linear_q9': 'a',
        'linear_q10': 'c',
        }
        
        # Calculate score
        score = 0
        for question, correct_answer in correct_answers.items():
            if submitted_answers.get(question) == correct_answer:
                score += 1
        
        # Pass the score and total questions to the result page
        return render_template('result.html', score=score, total=len(correct_answers))

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=8050)


