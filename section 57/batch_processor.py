"""Collect expected record errors while preserving their causes and notes."""
class RecordError(Exception):
    pass

class BatchError(ExceptionGroup):
    pass

def parse_record(index, raw):
    try:
        value = int(raw)
        if value < 0:
            raise ValueError("negative counts are invalid")
        return value
    except (ValueError, TypeError) as cause:
        error = RecordError("record could not be parsed")
        error.add_note(f"record index: {index}")
        raise error from cause

def process_batch(records):
    results, failures = [], []
    for index, raw in enumerate(records):
        try:
            results.append(parse_record(index, raw))
        except RecordError as error:
            failures.append(error)
    if failures:
        raise BatchError("batch rejected; no result returned", failures)
    return results

if __name__ == "__main__":
    print(process_batch(["1", "2"]))
    try:
        process_batch(["1", "bad", "-3"])
    except* RecordError as errors:
        for error in errors.exceptions:
            print(error.__notes__, type(error.__cause__).__name__)
