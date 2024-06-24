import requests
import pytest


@pytest.mark.parametrize(
    'folder_path, folder_name, status_code',
    (['pth', '123', 400],
     ['path', '123', 201],
     ['path', '123', 409]
    ))
def test_creat_new_ya_folder(folder_path, folder_name, status_code):

    url ='https://cloud-api.yandex.net/v1/disk/resources'
    token = 'OAuth y0_AgAAAAAbCvbwAADLWwAAAAD_Tc55AABw4ab9gFVKQLjzqBvOxfxZ9JpdWw'

    headers = {'Authorization': token
               }

    params = {folder_path: folder_name,
              }
    response = requests.put(url, headers=headers, params=params).status_code
    assert response == status_code