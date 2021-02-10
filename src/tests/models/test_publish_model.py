import sys
sys.path.append('.')

from src.models.publish import Publish
from datetime import datetime
import pytest


@pytest.mark.parametrize('initial_date, final_date',
                        [('2021-02-11 13:30:30', '2021-02-1213:30:30'),
                        (1, ''),
                        ('', 2), 
                        ])
def test_publish_date_type_error(initial_date, final_date):
    with pytest.raises(TypeError):
        publish_date = Publish(1, 1, initial_date, final_date, True)


@pytest.mark.parametrize('id_pool',
                        [('test'),
                        (12.0),
                        (None), 
                        ])
def test_id_pool_type(id_pool):
    with pytest.raises(TypeError):
        id_pool = Publish(id_pool, 1, datetime.today(), datetime.today(), True)


@pytest.mark.parametrize('id_channel',
                        [('test'),
                        (12.0),
                        (None), 
                        ])
def test_id_channel_type(id_channel):
    with pytest.raises(TypeError):
        id_channel = Publish(1, id_channel, datetime.today(), datetime.today(), True)
