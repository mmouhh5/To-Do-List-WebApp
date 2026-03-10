from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

task_list = []


@app.route("/")
def index():

    current_tasks = task_list
    return render_template("index.html", current_tasks=current_tasks)


@app.route("/add", methods=["POST"])
def add_task():
    # I learnt how to use POST requests to send data from HTML forms to Python

    new_item = request.form.get("task_input", "").strip()

    if new_item:
        task_list.append({"text": new_item, "done": False})

    return redirect(url_for("index"))




@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):

    if 0 <= task_id < len(task_list):

        task_list[task_id]["done"] = not task_list[task_id]["done"]
    return redirect(url_for("index"))

if __name__ == "__main__":

    app.run(debug=True)

# TODO: Add a delete button to delete finished tasks
# Add a database to store tasks

