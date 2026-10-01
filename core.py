import json


def new_game():
    return {'next_id': 1, 'audit': [('a', 1), ('b', 2)], 'used': 1, 'cap': 2, 'count': 0, 'accounts': {}, 'queue': [], 'snapshot': 5, 'value': 5, 'log': [], 'settled': False, 'seen': set(), 'connections': [('edge', -1)]}

def bug_2(state):
    entries = state.get("log", [])
    return entries[0] if entries else None

def bug_9(state):
    return state["next_id"]

def bug_16(state):
    return [row for row in state["audit"] if row[0] == "a"]

def bug_23(state):
    return state["cap"] - state["used"]

def bug_0(state):
    element = state["next_id"]
    seen = state.setdefault("seen", set())
    if element in seen:
        return False
    seen.add(element)
    return True

def bug_7(state):
    state["count"] += 1
    return state["count"]

def bug_14(state):
    return state["accounts"].get("missing", 0)

def bug_21(state):
    target = state["used"] + 1
    occupied = {slot for _owner, slot in state["audit"]}
    return target not in occupied

def bug_28(state):
    for _name, weight in state.get("connections", []):
        if weight < 0:
            return False
    return True

def bug_5(state):
    queue = state["queue"]
    return queue[0] if queue else None

def bug_30(state):
    failed = [entry for entry in state.get("log", []) if len(entry) > 1 and entry[1] == "failed"]
    if failed:
        state["value"] = state["snapshot"]
        state["log"] = [entry for entry in state["log"] if entry not in failed]
        return False
    return True

def bug_31(state):
    return not state.get("settled", False)

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
