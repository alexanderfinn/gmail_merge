from apiclient.discovery import build
from apiclient import errors


class GmailMerge(object):
    """
        Implements GMail bulk mail functionality
    """

    def __init__(self, service):
        """
            service -- Authorized Google API service
            https://developers.google.com/gmail/api/quickstart/quickstart-python
        """
        self.service = service

    def send_message(self, message, recipients):
        """
            message -- an instance of messages.Message
            recipients -- a list of messages.Recipient instances 
        """
        for recipient in recipients:
            return service.users().messages().send(userId='me', body=message.get_gmail_message(recipient)).execute()
