from atelier.tasks import ns, setup_from_tasks

setup_from_tasks(globals(), "commondata.ee")
ns.configure({
    'revision_control_system': 'git',
    'docs': [],
})
