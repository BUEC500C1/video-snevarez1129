import pytest
import stubFunctions

def test_stubFunctions():
    assert stubFunctions.getTweets("realDonaldTrump") == ["realDonaldTrump", "Big Rally in the Great State of South Carolina on Friday. See you there!", "Feb 26, 2020", "89.9K"]
    assert stubFunctions.getTweets("cnni") == ["cnni", "A flat bed in economy? This airline wants to make it happen: https://cnn.it/2VsAqIg", "Feb 27, 2020", 134]
    assert stubFunctions.getTweets("CNN") == ["CNN", "Researchers have discovered a new type of lion, the size of a domestic cat, with powerful flesh-cutting teeth, which roamed the earth around 24 million years ago.", "Feb 28, 2020", 739]
    assert stubFunctions.getTweets("busnowtm") == ["busnowtm", "Are you all ready for a great season? Make sure you check out our table at Splash this Saturday to get information about the upcoming season! See you then!", "Sep 5, 2018", 2]
