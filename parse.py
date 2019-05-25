import json
import pretty_print as pp
import random

class Activity(object):
    """ Class for activity as parsed from JSON file

    Attributes:
        in_progress : a list of ids of projects in progress
        not_started : a list of ids of projects that have not started
        complete : a list of ids of projects that are complete
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

    def write_json(self):
        new_json = {}
        projects = []
        for p in self.projects.values():
            projects.append(p.to_dict())
        new_json["projects"] = projects
        with open(r"proj.json", "w") as j:
            json.dump(new_json, j, indent=4)

    def config_as_choices(self):
        choices = []
        for p in self.projects.values():
            choice = {}
            choice["name"] = p.get_title()
            choice["value"] = p.get_id()
            choices.append(choice)
        return choices

    def add_project(self, new_proj):
        # TODO : generate random unqiue id
        # new_proj already has title, desc, skills
        id = "p0"
        while id in self.projects:
            id = "p"+str(random.randrange(100))
        new_proj["id"] = id
        new_proj["status"] = "not started"
        p = Project(new_proj)
        self.projects[id] = p
        self.not_started[id] = p
        self.write_json()

    def delete_project(self, id):
        del self.projects[id]
        if id in self.in_progress:
            del self.in_progress[id]
        if id in self.not_started:
            del self.not_started[id]
        if id in self.complete:
            del self.complete[id]
        self.write_json()    

    def print_projects(self, mode):
        """ mode  - list, all, status"""
        if mode == "list":
            pp.pprint_headings("\nList of projects:")
            for p in self.projects.values():
                pp.pprint_text(" > "+p.get_title() + " - " + p.get_desc())
            # print("\n")
        elif mode == "all":
            pp.pprint_headings("\nAll project details:")
            for p in self.projects.values():
                pp.pprint_text(" > "+p.get_title() + " - " + p.get_desc())
        elif mode == "status":
            pp.pprint_headings("\nProjects by status:")
            pp.pprint_headings("In progress:")
            for p in self.in_progress.values():
                pp.pprint_text(" > "+p.get_title())
            pp.pprint_headings("Not started:")
            for p in self.not_started.values():
                pp.pprint_text(" > "+p.get_title())
            pp.pprint_headings("Complete:")
            for p in self.complete.values():
                pp.pprint_text(" > "+p.get_title())
        else:
            print("Invalid mode")


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

    def to_dict(self):
        return {"id": self.id, "title":self.title, "desc": self.desc,
        "status": self.status, "skills": self.skills}


# act = Activity()
# print(act.in_progress, act.not_started, act.complete, act.projects)
