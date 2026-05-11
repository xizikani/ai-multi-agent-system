
def run(state):
    analysis = state["analysis"]
    arch = {
        "framework": "Spring Boot",
        "modules": ["controller", "service", "repository", "entity"],
        "structure": {
            "controller": "REST API层",
            "service": "业务逻辑层",
            "repository": "数据访问层",
            "entity": "实体模型"
        }
    }
    state["architecture"] = arch
    return state
