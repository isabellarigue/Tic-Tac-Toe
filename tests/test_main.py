import pytest
from unittest.mock import Mock
from tkinter import Canvas

@pytest.fixture
def tic_tac_toe_instance():
    from my_project import TicTacToe
    return TicTacToe()

def test_initialize_board(tic_tac_toe_instance):
    canvas_mock = Mock(spec=Canvas)
    tic_tac_toe_instance.canvas = canvas_mock
    tic_tac_toe_instance.initialize_board()
    assert canvas_mock.create_line.call_count == 4

def test_convert_logical_to_grid_position(tic_tac_toe_instance):
    logical_position = [1, 1]
    grid_position = tic_tac_toe_instance.convert_logical_to_grid_position(logical_position)
    assert grid_position == pytest.approx([300, 300])

def test_convert_grid_to_logical_position(tic_tac_toe_instance):
    grid_position = [350, 350]
    logical_position = tic_tac_toe_instance.convert_grid_to_logical_position(grid_position)
    assert (logical_position == [1, 1]).all()

def test_is_grid_occupied(tic_tac_toe_instance):
    tic_tac_toe_instance.board_status[1][1] = -1
    assert tic_tac_toe_instance.is_grid_occupied([1, 1]) is True
    assert tic_tac_toe_instance.is_grid_occupied([0, 0]) is False

def test_is_winner(tic_tac_toe_instance):
    tic_tac_toe_instance.board_status[0] = [-1, -1, -1]
    assert tic_tac_toe_instance.is_winner('X') is True
    tic_tac_toe_instance.board_status[0] = [1, 1, 1]
    assert tic_tac_toe_instance.is_winner('O') is True
    tic_tac_toe_instance.board_status[0] = [0, 0, 0]
    assert tic_tac_toe_instance.is_winner('X') is False

def test_is_tie(tic_tac_toe_instance):
    tic_tac_toe_instance.board_status = [[-1, 1, -1], [1, -1, 1], [1, -1, 1]]
    assert tic_tac_toe_instance.is_tie() is True
    tic_tac_toe_instance.board_status[0][0] = 0
    assert tic_tac_toe_instance.is_tie() is False

def test_is_gameover(tic_tac_toe_instance):
    tic_tac_toe_instance.board_status[0] = [-1, -1, -1]
    assert tic_tac_toe_instance.is_gameover() is True
    tic_tac_toe_instance.board_status[0] = [0, 0, 0]
    tic_tac_toe_instance.board_status[2] = [1, 1, 1]
    assert tic_tac_toe_instance.is_gameover() is True
    tic_tac_toe_instance.board_status = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert tic_tac_toe_instance.is_gameover() is False

def test_draw_O(tic_tac_toe_instance):
    canvas_mock = Mock(spec=Canvas)
    tic_tac_toe_instance.canvas = canvas_mock
    tic_tac_toe_instance.draw_O([1, 1])
    assert canvas_mock.create_oval.call_count == 1

def test_draw_X(tic_tac_toe_instance):
    canvas_mock = Mock(spec=Canvas)
    tic_tac_toe_instance.canvas = canvas_mock
    tic_tac_toe_instance.draw_X([1, 1])
    assert canvas_mock.create_line.call_count == 2

def test_display_gameover_X_win(tic_tac_toe_instance):
    canvas_mock = Mock(spec=Canvas)
    tic_tac_toe_instance.canvas = canvas_mock
    tic_tac_toe_instance.X_wins = True
    tic_tac_toe_instance.display_gameover()
    assert canvas_mock.create_text.call_count > 0
    assert tic_tac_toe_instance.X_score == 1

def test_display_gameover_tie(tic_tac_toe_instance):
    canvas_mock = Mock(spec=Canvas)
    tic_tac_toe_instance.canvas = canvas_mock
    tic_tac_toe_instance.tie = True
    tic_tac_toe_instance.display_gameover()
    assert canvas_mock.create_text.call_count > 0
    assert tic_tac_toe_instance.tie_score == 1