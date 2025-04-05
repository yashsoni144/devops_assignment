import requests

testcases = [
    {"url": "http://localhost:8000/add/2/2", "expected": 4},
    {"url": "http://localhost:8000/subtract/5/3", "expected": 2},
    {"url": "http://localhost:8000/multiply/2/3", "expected": 6}
]

def test():
    for case in testcases:
        response = requests.get(case["url"])
        result = response.json()["result"]
        assert result == case["expected"]
        print(f"Test passed for {case['url']}")

test()
