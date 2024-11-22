import sys,os
def pathmaker(path='..'):
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), path))
    if project_path not in sys.path:
        return sys.path.append(project_path)
