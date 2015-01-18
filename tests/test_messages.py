from nose.tools import assert_equals
from gmail_merge.messages import Message, Recipient


def test_message_rendering():
    """
        Tests message rendering
    """
    subject = 'Hello, {{first_name}}'
    text = 'Example text for {{last_name}}'
    message = Message(subject, text)
    rs, rb = message.get_message(Recipient('test@test.com', 
        {'first_name': 'FIRST', 'last_name': 'LAST'}))
    assert_equals(rs, 'Hello, FIRST')
    assert_equals(rb, 'Example text for LAST')