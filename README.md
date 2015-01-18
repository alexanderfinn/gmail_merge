# gmail_merge
This is a small library that allow sending bulk mails based on templates using user's gmail account.

## Usage
### Set up Message to send out:

    from gmail_merge.messages import Message
    subject = 'Test Mail for {{first_name}}'
    text = '''
        Hi {{first_name}} {{last_name}}!
        
        This is an example text of mail for {{company}}.
        Best Regards,
        John Doe, {{my_company}}
    '''
    message = Message(subject, text)

Note that you can use mustache notation ({{ }}) to define substrings that will be replaced

### Set up recipients list

    from gmail_merge.messages import Recipient
    recipients = [
        Recipient('test1@test.com', {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'company': 'Test Company'
            'my_company': 'Gmail Merge Inc'
        }),
        Recipient('test2@test.com', {
            'first_name': 'Jack',
            'last_name': 'Doe',
            'company': 'Another Company'
            'my_company': 'Gmail Merge Inc'
        }),
    ]

### Send bulk mails:

    from gmail_merge import GmailMerge
    # set up gmail_service first
    # see https://developers.google.com/gmail/api/quickstart/quickstart-python
    merge = GmailMerge(gmail_service)
    merge.send_message(message, recipients)
