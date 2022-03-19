from sqlalchemy import exc
from src.api.service import create_battle

class TestAPIService:
    '''
    create_battle
    '''
    def test_create_battle(self, mocker):
        mock_session = mocker.MagicMock()
        mocker.patch('src.api.service.Battle')
        dummy_args = [''] * 10
        assert create_battle(mock_session, *dummy_args)

    def test_create_battle_sql_error(self, mocker):
        mock_session = mocker.MagicMock()
        mock_error = mocker.MagicMock(side_effect=exc.SQLAlchemyError)
        mocker.patch('src.api.service.Battle', mock_error)
        dummy_args = [''] * 10
        assert not create_battle(mock_session, *dummy_args)
    
    # '''
    # get_shuffled_list_of_battles
    # '''
    # def test_get_shuffled_list_of_battles_multiple_results(self, mocker):
    #     pass
    
    # def test_get_shuffled_list_of_battles_no_results(self, mocker):
    #     pass
    
    # def test_get_shuffled_list_of_battles_sql_error(self, mocker):
    #     pass


    # def test_get_battle_by_id_found(self, mocker):
    #     pass
    
    # def test_get_battle_by_id_not_found(self, mocker):
    #     pass
    
    # def test_get_battle_by_id_sql_error(self, mocker):
    #     pass