import json


def new_game():
    return {'next_id': 1, 'audit': [('a', 1), ('b', 2)], 'used': 1, 'cap': 2, 'count': 0, 'accounts': {}, 'queue': [], 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_2(state):
    return None

def bug_9(state):
    new_id = state["next_id"]
    state["next_id"] += 1
    return new_id

def bug_16(state, owner=None):
    if owner is None:
        owner = state.get("owner", "a")
    return [row for row in state["audit"] if row[0] == owner]

def bug_23(state):
    return state["cap"] - state["used"]

def bug_0(state, element=None):
    processed = state.setdefault("processed", set())
    if element in processed:
        return False
    processed.add(element)
    return True

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state, key="missing"):
    return state["accounts"].get(key, 0)

def bug_21(state, slot=0):
    if slot < state["used"] or slot >= state["cap"]:
        return False
    state["used"] += 1
    return True

def bug_28(state, weight=-1):
    if weight < 0:
        return False
    state.setdefault("edges", []).append(weight)
    return True

def bug_5(state):
    if not state["queue"]:
        return None
    return state["queue"][0]

def bug_30(state):
    if any(status == "failed" for _, status in state["log"]):
        state["value"] = state["snapshot"]
        state["log"] = []
        return False
    state["snapshot"] = state["value"]
    state["log"] = []
    return True

def bug_31(state):
    if state["settled"]:
        return False
    state["value"] += 1
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
