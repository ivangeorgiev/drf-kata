def hello():
    print("Hello, world!")

def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"
    