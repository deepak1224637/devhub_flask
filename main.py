from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/languages")
def languages():
    return render_template("languages.html", title="Languages")

@app.route("/competitions")
def competitions():
    return render_template("competitions.html", title="Competitions")

@app.route("/resources")
def resources():
    return render_template("resources.html", title="Resources")

@app.route("/demand")
def demand():
    return render_template("demand.html", title="In-Demand Skills")

@app.route("/jobs")
def jobs():
    return render_template("jobs.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")

@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/blog")
def blog():
    # Example blog posts - You can replace with database later
    posts = [
        {
            "title": "How to Prepare for Coding Interviews in 2025",
            "link": "#"
        },
        {
            "title": "Top 5 Python Libraries You Must Know",
            "link": "#"
        },
        {
            "title": "Getting Started with Machine Learning",
            "link": "#"
        },
    ]
    return render_template("blog.html", title="Blog", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
