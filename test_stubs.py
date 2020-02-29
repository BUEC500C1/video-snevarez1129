import pytest
import stubFunctions

def test_stubFunctions():
    assert stubFunctions.getTweets("realDonaldTrump") == ["realDonaldTrump", "Big Rally in the Great State of South Carolina on Friday. See you there!", "Feb 26, 2020", "89.9K"]
