from flask import Flask, render_template, url_for

application = Flask(__name__)

# Sample team data
team_members = [
    {"name": "Chris Vinod Kurian", "role": "Front-End Developer", "bio": "An expert in web development and Team Leader", "image": "chris.png", "email":"chris.kurian.btech2022@sitpune.edu.in", "skills":['Frontend-Developmment','Backend-Development','ML', 'Deep Learning'], "linkedin":"https://www.linkedin.com/in/chris-vinod-kurian/", "github":"https://github.com/cvkchris"},
    {"name": "Gaurav Prakash", "role": "Back-End Developer", "bio": "Works passionately in developing the backend with strong cooperation.", "image": "gaurav.png", "email":"gaurav.prakash.btech2022@sitpune.edu.in", "skills":['Frontend-Developmment','Backend-Development','ML', 'Deep Learning'], "linkedin":"https://www.linkedin.com/in/gaurav-prakash-16bb9624a/"},
    {"name": "Drishtti Narwal", "role": "Front-End Developer", "bio": "An expert in backend and frontend integration and team management.", "image": "drishtti.png", "email":"drishtti.narwal.btech2022@sitpune.edu.in", "skills":['Frontend-Developmment','Backend-Development','ML', 'Deep Learning'], "linkedin":"https://www.linkedin.com/in/drishtti03/", "github":"https://github.com/DrishttiNarwal"},
    {"name": "Ananya Mehta", "role": "Backend-End Developer", "bio": "An expert in Machine Learning and Deep Learning and works to keep the team engaging", "image": "ananya.png", "email":"ananya.mehta.btech2022@sitpune.edu.in", "skills":['Frontend-Developmment','Backend-Development','ML', 'Deep Learning'], "linkedin":"https://www.linkedin.com/in/ananya-mehta-77229725a/", "github":"https://github.com/ananya39mehta"}
]

@application.route('/')
def index():
    return render_template('index.html', members=team_members)

@application.route('/member/<string:name>')
def member(name):
    member_data = next((m for m in team_members if m["name"] == name), None)
    return render_template('member.html', member=member_data)

if __name__ == "__main__":
    application.run(debug=True)
