from suds.client import Client
from suds import WebFault
from model.project import Project



class SoapHelper:
    def __init__(self,app):
        self.app = app


    def get_project_list(self):
        project_list = []
        username = "administrator"
        password = "root"
        client = Client("http://localhost/mantisbt-1.2.19/api/soap/mantisconnect.php?wsdl")
        try:
            a = client.service.mc_projects_get_user_accessible(username,password)
            for element in range(len(a)):
                id = a[element].id
                name = a[element].name
                status = a[element].status
                view_state = a[element].view_state
                project_list.append(Project(id=id, name=name))
            return list(project_list)
        except WebFault as ex:
            print(ex)
            return False
