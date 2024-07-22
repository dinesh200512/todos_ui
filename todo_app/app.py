from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
completed_tasks = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tasks')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/view_tasks')
def view_tasks():
    return render_template('view_tasks.html', tasks=tasks)

@app.route('/view_completed_tasks')
def view_completed_tasks():
    return render_template('view_completed_tasks.html', tasks=completed_tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        due_date = request.form['due_date']
        priority = request.form['priority']
        tasks.append({'name': task_name, 'due_date': due_date, 'priority': priority})
        return redirect(url_for('view_tasks'))
    return render_template('add_task.html')

@app.route('/edit_task', methods=['GET', 'POST'])
def edit_task():
    if request.method == 'POST':
        old_task_name = request.form['old_task_name']
        new_task_name = request.form['new_task_name']
        for task in tasks:
            if task['name'] == old_task_name:
                task['name'] = new_task_name
                break
        return redirect(url_for('view_tasks'))
    return render_template('edit_tasks.html')

@app.route('/delete_task', methods=['GET', 'POST'])
def delete_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        global tasks
        tasks = [task for task in tasks if task['name'] != task_name]
        return redirect(url_for('view_tasks'))
    return render_template('delete_task.html')

@app.route('/mark_completed', methods=['POST'])
def mark_completed():
    task_name = request.form['task_name']
    global tasks, completed_tasks
    for task in tasks:
        if task['name'] == task_name:
            completed_tasks.append(task)
            tasks.remove(task)
            break
    return redirect(url_for('view_tasks'))

if __name__ == '__main__':
    app.run(debug=True)
