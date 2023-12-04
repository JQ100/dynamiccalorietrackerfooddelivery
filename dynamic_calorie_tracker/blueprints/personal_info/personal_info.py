from flask import Blueprint, render_template, request, redirect
from ...models.personal_info import PersonalInfo
from ...extensions import db

personal_info_bp = Blueprint("personal_info", __name__, template_folder="templates")

@personal_info_bp.route("/personal_info", methods=['POST', 'GET'])
def personal_info():
    if request.method == 'POST':
        # todo
        name = request.form['name']
        new_personal_info = PersonalInfo(name=name)

        try:
            db.session.add(new_personal_info)
            db.session.commit()
            return redirect('/personal_info')
        except:
            return 'There was an issue adding your task'

    else:
        personal_info = PersonalInfo.query.order_by(PersonalInfo.date_created).all()
        # todo: use render_template
        # return render_template('index.html', tasks=tasks)
        return "This is the Personal Information page"
