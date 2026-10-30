"""BFCL structural oracle checks; NOT semantic intent evaluation or full BFCL scorer."""

def reference_action(calls):
    if not isinstance(calls, list):
        raise TypeError("reference turn must be a list")
    if not all(isinstance(c, str) for c in calls):
        raise TypeError("reference calls must be strings")
    return "REFERENCE_CALL" if calls else "REFERENCE_NO_CALL"

def validate_record_pair(entry, answer):
    if not isinstance(entry.get("question"), list):
        raise ValueError("question must be a list of turn slots")
    if len(entry["question"]) != len(answer.get("ground_truth", [])):
        raise ValueError("turn count mismatch")
    return [reference_action(calls) for calls in answer["ground_truth"]]

def test_checks():
    assert reference_action([]) == "REFERENCE_NO_CALL"
    assert reference_action(['sort(file_name="x")']) == "REFERENCE_CALL"
    try:
        reference_action("sort()")
    except TypeError:
        pass
    else:
        raise AssertionError("non-list accepted")
    try:
        validate_record_pair({"question": [[{"role":"user","content":"hi"}]]},
                             {"ground_truth": [[], []]})
    except ValueError:
        pass
    else:
        raise AssertionError("mismatched turns accepted")
    assert validate_record_pair({"question": [[], []]},
                                {"ground_truth": [[], ["ls()"]]}) == [
                                    "REFERENCE_NO_CALL", "REFERENCE_CALL"
                                ]

if __name__ == "__main__":
    test_checks()
    print("5 structural oracle checks passed; no BFCL model execution or semantic label validation")
