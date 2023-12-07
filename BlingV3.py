#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Set 4 2023.

@author: MatheusBruno
"""
import requests
import base64
import os
import datetime


class BlingV3():
    """Facilitate and obtain the Bling API V3 Access Token."""

    def parmentHeader(self, path: str):
        """
        Enter the path of the txt file with the client_id and client_secret.

        Example:
        -------
        client_id:sequence of numbers,
        client_secret:sequence of numbers

        :Usage:
            ::
                Bling().parmentHeader('/home/user/document/credential.txt')
        """
        global header

        credential = None

        with open(path, 'r') as file:
            credential = file.read()
            file.close()

        listCredential = credential.split(',')

        listCredential[0] = listCredential[0].replace("client_id:", "")
        listCredential[1] = listCredential[1].replace("\nclient_secret:", "")

        credentialbs4 = f"{listCredential[0]}:{listCredential[1]}"
        credentialbs4 = credentialbs4.encode('ascii')
        credentialbs4 = base64.b64encode(credentialbs4)
        credentialbs4 = bytes.decode(credentialbs4)

        header = {
            'Accept': '1.0',
            'Authorization': f'Basic {credentialbs4}'
        }

    def paramentCode(self, code: str):
        """
        Provide url code.

        :Usage:
            ::
                Bling().paramentCode("8337d4fd498508b9225b695f3bdf0ad086fb8bcc")
        """
        global dice
        dice = {
            'grant_type': 'authorization_code',
            'code': code
        }

    def tokenApi(self):
        """
        Return a list of objects containing the api data in case of right.

        [access_toke, expires_in, token_type, scope, refresh_token]
        in case of any error
        [error]
        ------------------------------------------------------------------
        If successful, a file will be created with the credentials and time.

        :Usage:
            ::

                obj = Bling().tokenApi()
        """
        api = requests.post(
            'https://www.bling.com.br/Api/v3/oauth/token',
            headers=header, json=dice)
        situationStatusCode = api.status_code
        print(api.status_code)
        api = api.json()

        if situationStatusCode == 400:
            return api
        else:
            path = os.getcwd()
            dateNow = datetime.date.today()
            apiHoursNow = ((int(api['expires_in'])/60)/60)
            systemHoursNow = datetime.datetime.now()
            hoursExpiration = (
                int(systemHoursNow.strftime("%H")) + apiHoursNow
            )

            if os.path.isdir(f"{path}/credential"):
                pass
            else:
                os.mkdir(f'{path}/credential')

            with open(f"{path}/credential/dice.txt", 'w') as file:
                file.write(f"""access_token:{api['access_token']},
                           \rexpires_in:{api['expires_in']},
                           \rhoursExpiration:{hoursExpiration},
                           \rdateExpiration:{dateNow},
                           \rrefresh_token:{api['refresh_token']}""")
                file.close()

            return {
                'access_token': api['access_token'],
                'expires_in': api['expires_in'],
                'token_type': api['token_type'],
                'scope': api['scope'],
                'refresh_token': api['refresh_token']
            }

    def refreshToken(self, refresh_token: str):
        """
        Return the new access token and update the file with the credentials.

        :Usage:
            ::
                obj = Bling().refreshToken("access_token")
        """
        dice = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }

        apiStatus = requests.post(
            'https://www.bling.com.br/Api/v3/oauth/token',
            headers=header, json=dice
        )

        api = apiStatus.json()

        if apiStatus.status_code == 400:
            return api
        else:
            path = os.getcwd()
            dateNow = datetime.date.today()
            apiHoursNow = ((int(api['expires_in'])/60)/60)
            systemHoursNow = datetime.datetime.now()
            hoursExpiration = (
                int(systemHoursNow.strftime("%H")) + apiHoursNow
            )

            if os.path.isdir(f"{path}/credential"):
                pass
            else:
                os.mkdir(f'{path}/credential')

            with open(f"{path}/credential/dice.txt", 'w') as file:
                file.write(f"""access_token:{api['access_token']},
                           \rexpires_in:{api['expires_in']},
                           \rhoursExpiration:{hoursExpiration},
                           \rdateExpiration:{dateNow},
                           \rrefresh_token:{api['refresh_token']}""")
                file.close()

            return {
                'access_token': api['access_token'],
                'expires_in': api['expires_in'],
                'token_type': api['token_type'],
                'scope': api['scope'],
                'refresh_token': api['refresh_token']
            }

