from orca.main import main


def test_main_output(capfd):
    main()
    out, err = capfd.readouterr()
    assert out.strip() == "Hello from orca!"
