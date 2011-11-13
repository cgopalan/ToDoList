from myproject.models import DBSession
from myproject.models import Task
from pyramid.httpexceptions import HTTPFound

def list_view(request):
    session = DBSession()
    tasks = session.query(Task).filter_by(closed=0).all()
    #rs = session.execute("select id, name from tasks where closed = 0")
    tasks = [dict(id=row.id, name=row.name) for row in tasks]
    return {'tasks':tasks}
    
def new_view(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            task = Task(request.POST['name'], 0)
            session = DBSession()
            session.add(task)
            request.session.flash('New task was succesfully added!')
            return HTTPFound(location=request.route_url('list'))
        else:
            request.session.flash('Please enter a name for the task!')
    return {}
    
def close_view(request):
    session = DBSession()
    task_id = int(request.matchdict['id'])
    task = session.query(Task).filter_by(id=task_id).first()
    task.closed = 1
    session.add(task)
    request.session.flash('Task was successfully closed!')
    return HTTPFound(location=request.route_url('list'))
    
#def notfound_view(self):
#    return {}
