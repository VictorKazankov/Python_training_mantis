from model.project import Project
from selenium.webdriver.support.ui import Select


class ProjectHelper:
    def __init__(self,app):
        self.app = app

    #project_cache = None

    def get_project_list(self):
            wd = self.app.wd
            self.open_project_page()
            project = []
            for element in wd.find_elements_by_css_selector('.row-1 td a,.row-2 td a'):
                name = element.text
                href = element.get_attribute("href")
                href.startswith("http://localhost/mantisbt-1.2.19/manage_proj_edit_page.php?project_id=")
                id = href[70:]
                project.append(Project(name=name, id=id))
            return project


    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()


    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

        select_status = Select(wd.find_element_by_name('status'))
        select_status.select_by_visible_text("%s" % project.status)

        category = wd.find_element_by_name('inherit_global')
        category.send_keys("%s" % project.categories)

        select_view_status = Select(wd.find_element_by_name('view_state'))
        select_view_status.select_by_visible_text("%s" % project.view_status)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)