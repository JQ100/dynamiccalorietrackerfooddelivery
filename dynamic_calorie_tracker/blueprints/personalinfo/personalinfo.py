from flask import Blueprint, render_template, request, redirect
from ...models.personal_info import PersonalInfo
from ...extensions import db

personalinfo_bp = Blueprint("personalinfo", __name__, template_folder="templates")

@personalinfo_bp.route("/personalinfo", methods=['POST', 'GET'])
def personalinfo():
    if request.method == 'POST':
        name = request.form['name']
        new_personal_info = PersonalInfo(name=name)

        try:
            db.session.add(new_personal_info)
            db.session.commit()
            return redirect('/personalinfo')
        except:
            return 'There was an issue adding your task'

    else:
        personal_info = PersonalInfo.query.order_by(PersonalInfo.date_created).all()
        # todo: use render_template
        # return render_template('index.html', tasks=tasks)
        return "This is the Personal Information page"


