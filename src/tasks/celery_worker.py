from src.app import create_app


app = create_app()
app.app_context().push()


from src.tasks import celery