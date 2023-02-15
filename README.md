<!---:lai-name: Slack Messenger--->

# Lightning component template

Template for creating a lightning component.
Implements a component to send a slack message for demo purposes.

## Use the component

<!---:lai-use:--->
```python
import lightning as L
from slack import SlackMessenger

class YourComponent(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.slack_messenger = SlackMessenger(token='a-long-token', channel_id='A03CB4A6AK7')

    def run(self):
        self.slack_messenger.run('hello from ⚡ lit slack ⚡')
```

## install
Use these instructions to install:

<!---:lai-install:--->
```bash
git clone https://github.com/PyTorchLightning/LAI-slack-messenger.git
cd LAI-slack-messenger
pip install -r requirements.txt
pip install -e .
```
