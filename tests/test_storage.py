import pytest
from storage import load_task, save_tasks

def test_save_and_load_tasks(tmp_path):
    # Temporary file path
    file = tmp_path / "tasks.json"

    tasks = [
        {"title": "Buy milk", "created_at": "2025-01-01 10:00:00"},
        {"title": "Study Python", "created_at": "2025-01-01 11:00:00"},
    ]

    # Save tasks
    save_tasks(file, tasks)

    # Load tasks back
    loaded = load_task(file)

    # They should match exactly
    assert loaded == tasks


def test_load_missing_file(tmp_path):
    # File does not exist
    fake_file = tmp_path / "missing.json"

    result = load_task(fake_file)

    # Missing file should return empty list
    assert result == []
