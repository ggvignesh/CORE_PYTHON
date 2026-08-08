#1. Call the function send_email(to, subject, body) using keyword arguments in any order.
def send_email(to, subject, body):
    print("To      :", to)
    print("Subject :", subject)
    print("Body    :", body)

send_email(
    body="Your interview is scheduled for tomorrow.",
    to="student@gmail.com",
    subject="Interview Notification"
)