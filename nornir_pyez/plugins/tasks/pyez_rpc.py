from typing import Dict
from nornir.core.task import Result, Task
from nornir_pyez.plugins.connections import CONNECTION_NAME


def pyez_rpc(
    task: Task,
    func: str,
    extras: Dict = None,
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    function = getattr(device.rpc, func)
    if extras:
        data = function(**extras)
    else:
        data = function()
    return Result(host=task.host, result=data)
