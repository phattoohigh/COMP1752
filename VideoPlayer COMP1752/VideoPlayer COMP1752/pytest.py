import pytest
from video_player import LibraryItem  # Adjust the import based on your module name

def test_library_item_initialization():
    item = LibraryItem("Test Movie", "Test Director", 3)
    assert item.name == "Test Movie"
    assert item.director == "Test Director"
    assert item.rating == 3
    assert item.play_count == 0

def test_library_item_info():
    item = LibraryItem("Test Movie", "Test Director", 4)
    assert item.info() == "Test Movie - Test Director ****"

def test_library_item_stars():
    item = LibraryItem("Test Movie", "Test Director", 2)
    assert item.stars() == "**"

def test_increment_play_count():
    item = LibraryItem("Test Movie", "Test Director", 2)
    assert item.play_count == 0
    item.increment_play_count()
    assert item.play_count == 1

def test_set_rating_valid():
    item = LibraryItem("Test Movie", "Test Director")
    item.set_rating(7)
    assert item.rating == 7

def test_set_rating_invalid_string():
    item = LibraryItem("Test Movie", "Test Director")
    with pytest.raises(ValueError):
        item.set_rating('four')

def test_set_rating_invalid_range():
    item = LibraryItem("Test Movie", "Test Director")
    with pytest.raises(ValueError):
        item.set_rating(15)
