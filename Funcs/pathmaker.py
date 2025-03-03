import os
import sys

def pathmaker(relative_path):
    """
    Adds the specified relative path to sys.path and changes the working directory.
    """
    # Calculate absolute path relative to the caller's directory
    caller_dir = os.getcwd()
    target_path = os.path.abspath(os.path.join(caller_dir, relative_path))

    # Add the calculated path to sys.path if not already added
    if target_path not in sys.path:
        sys.path.append(target_path)
    
    # Change the working directory to the target path
    os.chdir(target_path)

    return target_path
