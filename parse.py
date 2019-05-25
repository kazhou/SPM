import json

class Activity(object):
    """ Class for activity as parsed from JSON file

    Attributes:
        current : a list of ids of current projects
        projects : a dictionary of projects, key = id, value = Project object

    """

    def __init__(self):
        self.in_progress= {}
        self.not_started = {}
        self.complete = {}
        self.projects = {}
        self.load_json()

    def load_json(self):
        with open(r"proj.json") as j:
            proj = json.load(j)

        # self.current = proj["current"] # TODO don't need this

        for p in proj["projects"]:
            key = p["id"]
            self.projects[key] = Project(p)
            if p["status"] == "in progress":
                self.in_progress[key] = self.projects[key]
            elif p["status"] == "not started":
                self.not_started[key] = self.projects[key]
            elif p["status"] == "complete":
                self.complete[key] = self.projects[key]
            else:
                print("Invalid status")

    def print_projects(self):
        pass


class Project(object):
    """ Class for projects as parsed from JSON file

    Attributes:
        id : a unique string identifying project
        title : a string for title of project
        desc : a string decribing the project details
        status : a string denoting "not started", "in progress", or "complete"
        skills : a list of strings denoting tags of the project

    """

    def __init__(self, src):
        self.id = src["id"]
        self.title = src["title"]
        self.desc = src["desc"]
        self.status = src["status"]
        self.skills = src["skills"]

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_desc(self):
        return self.desc

    def get_status(self):
        return self.status

    def get_skills(self):
        return self.skills


# act = Activity()
# print(act.in_progress, act.not_started, act.complete, act.projects)
