# from django.urls import reverse
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard
from jet.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        request = context.get('request', {'user': None})
        user = request.user

        # available
        self.available_children.append(modules.LinkList)
        self.available_children.append(modules.Feed)
        self.available_children.append(modules.RecentActions)
        self.available_children.append(modules.AppList)

        site_name = get_admin_site_name(context)

        # col 0
        self.children.append(modules.LinkList(
            "Applications",
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                {
                    'title': "Resumes",
                    'url': '/admin/cv/resume/',
                },
            ],
            column=0,
            order=0
        ))
        self.children.append(modules.ModelList(
            "Users",
            models=('auth.User', 'auth.Group'),
            column=0,
            order=1
        ))

        # col 1
        self.children.append(modules.RecentActions(
            "Recent actions",
            10,
            column=1,
            order=0,
        ))

        # col 2
        self.children.append(modules.LinkList(
            'Quick links',
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                ['Return to site', '/'],
                ['Change password', '/admin/password_change/'],
                ['Logout', '/admin/logout/'],
            ],
            column=2,
            order=0,
        ))

        self.children.append(modules.LinkList(
            "Documentation APIs",
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                {
                    'title': "APIs",
                    'url': '/api/',
                },
                {
                    'title': "Swagger",
                    'url': '/api/swagger/',
                },
                {
                    'title': "Redoc",
                    'url': '/api/redoc/',
                },
            ],
            column=2,
            order=1,
        ))

        self.children.append(modules.LinkList(
            'Developer website',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                {
                    'title': 'Nask.io',
                    'url': 'http://nask.io/',
                    'external': True,
                },
            ],
            column=2,
            order=2
        ))
