import aos_sw_api

from .user_pass_ip import username, password, switch_ip, api_version


def test_auth_client():
    with aos_sw_api.Client(switch_ip, api_version, username, password) as client:
        print(client._session.headers)


def main():
    test_auth_client()


if __name__ == "__main__":
    main()
