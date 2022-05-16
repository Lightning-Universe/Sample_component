# Lightning component template

Template for creating a lightning component

## Use the component

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