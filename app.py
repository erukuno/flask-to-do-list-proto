from flask import render_template, request, redirect
from models import create_app, init_db, Todo, db  # Import the db object

app = create_app()

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding this"
    else:
        return render_template('index.html')

# Initialize the database
init_db(app)

if __name__ == "__main__":
    app.run(debug=True)
