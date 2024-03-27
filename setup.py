from cx_Freeze import setup, Executable

setup(
    name="IdeaTracker",
    version="1.0",
    description="A simple idea tracking application",
    executables=[Executable("main.py")],
)