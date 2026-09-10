from clipper_ai.runtime.api_service import RuntimeService
from clipper_ai.gpu.worker_manager import GPUWorkerManager
from clipper_ai.deployment.hybrid import deployment_mode
from clipper_ai.release.version import release_info

def test_phase7_10():
    assert RuntimeService().health()["status"] == "READY"
    assert GPUWorkerManager().status()["worker"] == "READY"
    assert deployment_mode()["hybrid"] == "READY"
    assert release_info()["version"] == "1.0.0"
