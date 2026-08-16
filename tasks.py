from extensions import celery
from google.genai.errors import ServerError
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@celery.task(
    bind=True,
    retry_backoff=True,
    retry_backoff_max=60,
    max_retries=3,
)
def generate_ai_content(self, post_id):
    #lazy imports to avoid loop
    from main import app, generate_post_insights, generate_similar_destinations
    from extensions import db
    from models import BlogPost

    with app.app_context():
        post = db.session.get(BlogPost, post_id)

        if not post:
            logger.warning("Post %s does not exist.", post_id)
            print("Post does not exist.")
            return

        try:
            post.ai_insights = generate_post_insights(post.body)
            post.ai_similar_destinations = generate_similar_destinations(post.body)
            post.ai_status = "ready"
            db.session.commit()
            logger.info("AI content ready for post %s", post_id)
            print("Post insights and similar destinations ready.")
        except ServerError as e:
            try:
                raise self.retry(exc=e)
            except self.MaxRetriesExceededError:
                post.ai_status = "failed"
                db.session.commit()
                logger.exception("AI generation permanently failed for post %s", post_id)
                print(f"AI generation permanently failed for post {post_id}: {e}")