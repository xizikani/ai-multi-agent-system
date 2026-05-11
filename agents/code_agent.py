
def run(state):
    arch = state["architecture"]
    code = {
        "Application.java": "public class Application {}",
        "Controller.java": "public class DemoController {}",
        "Service.java": "public class DemoService {}"
    }
    state["code"] = code
    return state
