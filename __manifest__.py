{
    'name': 'To-Do Application',
    'description': 'Manage your personal To-Do tasks.',
    'summary': '--',
    'author': 'Ievgen Synchyshyn',
    'version': '1.0',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/todo_menu.xml',
        'views/todo_view.xml',
    ],
    'application': True,
}
