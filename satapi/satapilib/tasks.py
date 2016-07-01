from connection import *

class SatAPITasks(SatAPIConnection):
    TasksAPILocation='/foreman_tasks/api/'

    # Constructor
    def __init__(self, URL, User, Password, Debug=False):
        SatAPIConnection.__init__(self, URL, User, Password, Debug)
        self.TasksAPILocation='%s/foreman_tasks/api/' % URL

    # Get a task by its ID number
    def getTask(self, Id):
        Response=self.GET(self.TasksAPILocation + 'tasks/' + str(Id))
        return Response

    # Search tasks by a search criteria(s)
    def searchTask(self, Searches, Count=99):
        Response=self.GET(self.TasksAPILocation + 'tasks/',
                            {'searches': Searches, 'count': Count, 'per_page': Count})
        return Response

    # Get tasks related with a given content view
    def getContentViewTasks(self, ContentView, ActiveOnly=False):
        JSONData=json.dumps(
            {
                'searches': [
                    {
                        'type': 'resource',
                        'resource_type': 'Katello::ContentView',
                        'resource_id': ContentView['id'],
                        'active_only': ActiveOnly
                    }
                ]
            }
        )
        Response=self.POST(self.TasksAPILocation + 'tasks/bulk_search/',
                            JSONData)

        return Response

    # Get synchronization tasks related with a given content view
    def getContentViewSyncTasks(self, ContentView, ActiveOnly=False):
        JSONData=json.dumps(
            {
                'searches': [
                    {
                        'type': 'resource',
                        'resource_type': 'Katello::ContentView',
                        'resource_id': ContentView['id'],
                        'action_types': 'Actions::Katello::ContentView::CapsuleGenerateAndSync',
                        'active_only': ActiveOnly
                    }
                ]
            }
        )
        Response=self.POST(self.TasksAPILocation + 'tasks/bulk_search/',
                            JSONData)

        return Response

