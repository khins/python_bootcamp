import pytest
from bootcamp_catalog.cli import main
from bootcamp_catalog.storage import load

@pytest.mark.integration
def test_add_and_list(tmp_path, capsys):
    path = tmp_path / "catalog.json"
    assert main(["--catalog", str(path), "add", "Signals", "Rush", "1982"]) == 0
    assert "Added 1 album" in capsys.readouterr().out
    assert main(["--catalog", str(path), "list"]) == 0
    assert "Signals by Rush (1982)" in capsys.readouterr().out
    assert len(load(path)) == 1

@pytest.mark.integration
def test_corrupt_data_is_reported_and_preserved(tmp_path, capsys):
    path = tmp_path / "catalog.json"
    path.write_text("not JSON", encoding="utf-8")
    assert main(["--catalog", str(path), "add", "Blue", "Joni Mitchell", "1971"]) == 1
    assert "Error:" in capsys.readouterr().err
    assert path.read_text(encoding="utf-8") == "not JSON"

def test_bad_year_argument(tmp_path):
    with pytest.raises(SystemExit) as error:
        main(["--catalog", str(tmp_path / "data.json"), "add", "A", "B", "oops"])
    assert error.value.code == 2
