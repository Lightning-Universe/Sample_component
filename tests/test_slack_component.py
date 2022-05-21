import os
import pytest
import subprocess
from lit_slack.component import SlackMessenger


def test_send_message():
    token = os.environ['SLACK_TOKEN']
    channel_id = os.environ['SLACK_CHANNEL_ID']

    messenger = SlackMessenger(token=token, channel_id=channel_id)
    result = messenger.run('test from CI/CD')
    assert result.status_code == 200


@pytest.mark.parametrize(
    "real_component, test_component_pip_name",
    [
        (
            f"git+https://{os.environ['GH_TOKEN']}@github.com/PyTorchLightning/LAI-slack-messenger.git@14f333456ffb6758bd19458e6fa0bf12cf5575e1",
            "lit-slack",
        ),
    ],
)
def test_install(real_component, test_component_pip_name):
    """Tests both published and unpublished component installs."""
    # uninstall component just in case and verify it's not in the pip output
    env_output = subprocess.check_output(f"pip uninstall {test_component_pip_name} --yes && pip freeze", shell=True)
    assert test_component_pip_name not in str(env_output), f"{test_component_pip_name} should not be in the env"

    # install component and verify it's in the env
    new_env_output = subprocess.check_output(
        f"lightning install component {real_component} --yes && pip freeze", shell=True
    )
    assert test_component_pip_name in str(new_env_output), f"{test_component_pip_name} should be in the env"

    # clean up for test
    subprocess.run(f"pip uninstall {test_component_pip_name} --yes", shell=True)
    env_output = subprocess.check_output("pip freeze", shell=True)
    assert test_component_pip_name not in str(
        env_output
    ), f"{test_component_pip_name} should not be in the env after cleanup"
