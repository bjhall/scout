from pprint import pprint as pp

from scout.update.panel import update_panel
from scout.utils.date import get_date

def test_update_panel_version(panel_database, case_obj):
    adapter = panel_database
    adapter._add_case(case_obj)
    
    ## GIVEN an adapter with a case with gene panels
    case_obj = adapter.case_collection.find_one()
    panel_obj = adapter.panel_collection.find_one()
    
    case_id = case_obj['_id']
    
    # There is infirmation about a panel both in the panel collection
    # and on the case object. This is fine until one starts to manipulate the objects
    panel = case_obj['panels'][0]
    
    panel_version = panel['version']
    panel_name = panel['panel_name']
    panel_id = panel['panel_id']

    new_panel_version = panel_version + 1
    
    ## WHEN updating the panel version
    
    updated_panel = update_panel(adapter, panel_name, panel_version, new_panel_version)
    
    ## THEN assert that the panel version was updated both in panel and case
    
    panel_obj = adapter.panel_collection.find_one({'_id': panel_id})
    
    assert panel_obj['version'] == new_panel_version
    
    case_obj = adapter.case_collection.find_one({'_id': case_id})
    
    for panel in case_obj['panels']:
        assert panel['version'] == new_panel_version
    

def test_update_panel_date(panel_database, case_obj):
    adapter = panel_database
    adapter._add_case(case_obj)
    
    ## GIVEN an adapter with a case with gene panels
    new_date_obj = get_date('2015-03-12')
    
    case_obj = adapter.case_collection.find_one()
    panel_obj = adapter.panel_collection.find_one()
    
    case_id = case_obj['_id']
    
    # There is infirmation about a panel both in the panel collection
    # and on the case object. This is fine until one starts to manipulate the objects
    panel = case_obj['panels'][0]
    
    panel_version = panel['version']
    panel_name = panel['panel_name']
    panel_id = panel['panel_id']

    new_panel_version = panel_version + 1
    
    ## WHEN updating the panel version
    
    updated_panel = update_panel(adapter, panel_name, panel_version, new_date=new_date_obj)
    
    ## THEN assert that the panel version was updated both in panel and case
    
    panel_obj = adapter.panel_collection.find_one({'_id': panel_id})
    
    assert panel_obj['date'] == new_date_obj
    
    case_obj = adapter.case_collection.find_one({'_id': case_id})
    
    for panel in case_obj['panels']:
        assert panel['updated_at'] == new_date_obj
    