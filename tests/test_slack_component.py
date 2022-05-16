import imp
import os
from slack.component import SlackMessenger


def test_send_message():
    token = os.environ['SLACK_TOKEN']
    channel_id = os.environ['SLACK_CHANNEL_ID']

    messenger = SlackMessenger(token=token, channel_id=channel_id)
    messenger.run('test from CI/CD')
