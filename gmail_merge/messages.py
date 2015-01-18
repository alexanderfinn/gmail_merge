import base64
from email.mime.text import MIMEText


class Recipient(object):
    """
        Contains e-mail address and 
        recipient-specific attributes
    """

    def __init__(self, email, attributes):
        """
            email -- email address string
            attributes -- dict of attributes 
            used with template rendering
        """
        assert isinstance(email, str)
        assert isinstance(attributes, dict)
        self.email = email
        self.attributes = attributes


class Message(object):
    """
        Message that will be sent out
    """

    def __init__(self, subject, text):
        self.subject = subject
        self.text = text

    def _render(self, what, attributes):
        for k, v in attributes.iteritems():
            what = what.replace('{{%s}}' % k, v)
        return what

    def get_message(self, recipient):
        subject = self._render(self.subject, recipient.attributes)
        body = self._render(self.text, recipient.attributes)
        return subject, body

    def get_gmail_message(self, recipient):
        subject, body = self.get_message(recipient)
        message = MIMEText(body)
        message['to'] = recipient.email
        # this is a special value indicating currently authenticated user
        message['from'] = "me" 
        message['subject'] = subject
        return {'raw': base64.b64encode(message.as_string())}
