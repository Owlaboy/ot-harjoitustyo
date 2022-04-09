from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/calculator.py", pty=True)
    ctx.run("python3 src/personcreation.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)