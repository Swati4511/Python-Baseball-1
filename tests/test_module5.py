import pytest
import matplotlib
matplotlib.use('Agg')

from .utils import *

from stats import defense

@pytest.mark.test_import_existing_dataframes_module5
def test_import_existing_dataframes_module5():
    assert 'games' in dir(defense), 'Have you imported `games` from `.data`?'
    assert 'info' in dir(defense), 'Have you imported `games` from `.data`?'
    assert 'events' in dir(defense), 'Have you imported `games` from `.data`?'

@pytest.mark.test_query_function_module5
def test_query_function_module5():
    assert "plays:games:query:type == 'play' & event != 'NP'" in get_assignments(defense), ''

@pytest.mark.test_column_labels_module5
def test_column_labels_module5():
    assert 'plays:columns:type:inning:team:player:count:pitches:event:game_id:year' in get_assignments(defense), ''

@pytest.mark.test_shift_dataframe_module5
def test_shift_dataframe_module5():
    assert 'pa:plays:loc:plays:player:shift:plays:player:year:game_id:inning:team:player' in get_assignments(defense), ''

@pytest.mark.test_group_plate_appearances_module5
def test_group_plate_appearances_module5():
    assert 'pa:pa:groupby:year:game_id:team:size:reset_index:name:PA' in get_assignments(defense), ''

@pytest.mark.test_unstack_the_dataframe_module5
def test_unstack_the_dataframe_module5():
    assert 'events:events:set_index:year:game_id:team:event_type' in get_assignments(defense), ''
    assert 'events:events:unstack:fillna:0:reset_index' in get_assignments(defense), ''

@pytest.mark.test_manage_column_labels_module5
def test_manage_column_labels_module5():
    assert 'events:columns:events:columns:droplevel' in get_assignments(defense), ''
    assert 'events:columns:year:game_id:team:BB:E:H:HBP:HR:ROE:SO' in get_assignments(defense), ''
    assert 'events:events:rename_axis:None:axis:columns' in get_assignments(defense), ''

@pytest.mark.test_merge_plate_appearances_module5
def test_merge_plate_appearances_module5():
    assert 'events_plus_pa:pd:merge:events:pa:how:outer:left_on:year:game_id:team:right_on:year:game_id:team' in get_assignments(defense), ''

@pytest.mark.test_merge_team_module5
def test_merge_team_module5():
    assert 'defense:pd:merge:events_plus_pa:info' in get_assignments(defense), ''

@pytest.mark.test_calculate_der_module5
def test_calculate_der_module5():
    assert 'defense:loc:None:None:None:DER:1:defense:H:defense:ROE:defense:PA:defense:BB:defense:SO:defense:HBP:defense:HR' in get_assignments(defense), ''
    assert 'defense:loc:None:None:None:year:pd:to_numeric:defense:year' in get_assignments(defense), ''

@pytest.mark.test_reshape_with_pivot_module5
def test_reshape_with_pivot_module5():
    assert 'der:Name:defense:Name:loc:Attribute:defense:Name:year:Str:Index:Subscript:GtE:1978:Num:Compare:year:Str:defense:Str:DER:Str:List:Tuple:Index:Subscript:Assign' in get_assignments(defense, include_type=True), ''

@pytest.mark.test_plot_formatting_xticks_module5
def test_plot_formatting_xticks_module5():
    assert 'der:plot:x_compat:True:xticks:range:1978:2018:4:rot:45' in get_calls(defense), ''
    assert 'plt:show' in get_calls(defense), ''
