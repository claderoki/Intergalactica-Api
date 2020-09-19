import os
import argparse
import json

from flask import Flask, request
# from flask_admin import Admin
# from flask_admin.contrib.peewee import ModelView

import src.config as config

app = Flask(__name__)

from src.models import Poll, Vote, Option

"""
{
  "id": 13,
  "question": "hello there?",
  "guild_id": "123",
  "author_id": "123",
  "type": "single",
  "message_id": "123",
  "channel_id": "123",
  "options": [
    {
      "id": null,
      "value": "",
      "reaction" : ""
    }
  ]
}

"""

@app.route("/")
def index():
    return json.dumps({"name": "alice",
                       "email": "alice@outlook.com"})


@app.route("/poll")
def poll():
    id = int(request.args.get("id"))
    return json.dumps({"id" : id})


@app.route("/poll/save", methods = ["POST"])
def poll_save():
    post = json.loads(request.data)

    new = not bool(post["id"])

    with db:
        if not new:
            poll = Poll.get(id = int(post["id"]))
        else:
            poll = Poll()

        for attr_name, attr_value in post.items():
            if attr_name not in ("id", "options"):
                setattr(poll, attr_name, attr_value)

        poll.save()

        for data in post["options"]:
            if data["id"]:
                option = Option.get(id = data["id"])
            else:
                option = Option()

            option.value    = data["value"]
            option.reaction = data["reaction"]

            option.save()

    return json.dumps(post)




app.run()












# class OptionAdmin(ModelView):
#     inline_models = (Option,)

# class PollAdmin(ModelView):
    # Visible columns in the list view
    # column_exclude_list = ["question"]

    # List of columns that can be sorted. For "user" column, use User.email as
    # a column.
    # column_sortable_list = ("question", "due_date" )

    # Full text search
    # column_searchable_list = ("question", )

    # Column filters
    # column_filters = ("title",
    #                   "date",
    #                   User.username)

    # form_ajax_refs = {
    #     "option": {
    #         "fields": (Option.value,)
    #     }
    # }

# set optional bootswatch theme
# app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
# app.config["SECRET_KEY"] = os.environ["discord_token"]


# admin = Admin(app, name="microblog", template_mode="bootstrap3")
# Add administrative views here


# admin.add_view(PollAdmin(Poll))
# admin.add_view(OptionAdmin(Option))
