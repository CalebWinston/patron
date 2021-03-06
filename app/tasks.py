from app import scheduler, db
from app.email import send_reminder_emails
from app.models import User
from datetime import datetime, timedelta

hour = scheduler.app.config.get('SCHEDULER_HOUR')
minute = scheduler.app.config.get('SCHEDULER_MINUTE')
if hour is not None:
    hour = int(hour)
else:
    hour = 9
if minute is not None:
    minute = int(minute)


@scheduler.task('cron', id='do_renewals', hour=hour, minute=minute)
def renewals():
    yesterday = datetime.today() - timedelta(hours=24)
    tomorrow = datetime.today() + timedelta(hours=24)
    with scheduler.app.app_context():
        last_reminder = User.query.filter(
            User.expiration < tomorrow,
            User.expiration > yesterday
        ).all()
    six = datetime.today() + timedelta(hours=144)
    four = datetime.today() + timedelta(hours=96)
    with scheduler.app.app_context():
        first_reminder = User.query.filter(
            User.expiration < six,
            User.expiration > four
        ).all()
    reminder_list = first_reminder + last_reminder
    send_reminder_emails(scheduler.app, reminder_list)
