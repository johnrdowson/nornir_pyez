from jnpr.junos.utils.config import Config
from nornir.core.task import Result, Task

from nornir_pyez.plugins.connections import CONNECTION_NAME


def pyez_commit(
    task: Task,
) -> Result:
    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    device.timeout = 300
    config = Config(device)
    if config.commit_check() == True:
        config.commit()
    else:
        config.rollback()
    config.unlock()
    return Result(host=task.host, result=f"Successfully committed")
