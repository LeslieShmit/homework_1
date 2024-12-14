import pytest


@pytest.fixture
def list_of_dicts():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dicts_wrong_date_format():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "201-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-15-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "201812-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-99T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dicts_same_dates():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2018-06-30T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T08:21:33.419441"},
    ]
