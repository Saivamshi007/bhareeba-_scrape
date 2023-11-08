import requests

cookies = {
    'language': 'en',
    'region': 'NA',
    'BIGipServerCZ6NZvQvvNILIJWByLy9bA': '^!Ee/VodkXNsageNKY9IYH/yhXYGfVskNWUv4n6UncV+EVkuumRAnoiixtOZw4Gf9Kwz15/aoFUAHcziI=',
    'sap-usercontext': 'sap-language=EN&sap-client=100',
    'MYSAPSSO2': 'AjQxMDMBABhVADAAMAAwADAAMAAwADIANgA3ADQAMAACAAYxADAAMAADABBGAFMAUAAgACAAIAAgACAABAAYMgAwADIAMwAxADEAMAA3ADEAMgAzADYABQAEAAAACAkAAkUA^%^2fwD7MIH4BgkqhkiG9w0BBwKggeowgecCAQExCzAJBgUrDgMCGgUAMAsGCSqGSIb3DQEHATGBxzCBxAIBATAaMA4xDDAKBgNVBAMTA0ZTUAIICiAZAyQWQAEwCQYFKw4DAhoFAKBdMBgGCSqGSIb3DQEJAzELBgkqhkiG9w0BBwEwHAYJKoZIhvcNAQkFMQ8XDTIzMTEwNzEyMzY1OFowIwYJKoZIhvcNAQkEMRYEFEPZdbISEi^%^2fNh1RdT2M859BmrQgBMAkGByqGSM44BAMELjAsAhQGG7iG5FQ4lOAH5^%^2fBfN5CV6r^%^2f7HgIUfer2WKCXUL^%^2fRT4t^%^217kXsUndBuY4^%^3d',
    'SAP_SESSIONID_FSP_100': 'OYOybmh_6i0WbJP6gI-1xFcKeY59ahHujOPReeI0vos^%^3d',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'language=en; region=NA; BIGipServerCZ6NZvQvvNILIJWByLy9bA=^!Ee/VodkXNsageNKY9IYH/yhXYGfVskNWUv4n6UncV+EVkuumRAnoiixtOZw4Gf9Kwz15/aoFUAHcziI=; sap-usercontext=sap-language=EN&sap-client=100; MYSAPSSO2=AjQxMDMBABhVADAAMAAwADAAMAAwADIANgA3ADQAMAACAAYxADAAMAADABBGAFMAUAAgACAAIAAgACAABAAYMgAwADIAMwAxADEAMAA3ADEAMgAzADYABQAEAAAACAkAAkUA^%^2fwD7MIH4BgkqhkiG9w0BBwKggeowgecCAQExCzAJBgUrDgMCGgUAMAsGCSqGSIb3DQEHATGBxzCBxAIBATAaMA4xDDAKBgNVBAMTA0ZTUAIICiAZAyQWQAEwCQYFKw4DAhoFAKBdMBgGCSqGSIb3DQEJAzELBgkqhkiG9w0BBwEwHAYJKoZIhvcNAQkFMQ8XDTIzMTEwNzEyMzY1OFowIwYJKoZIhvcNAQkEMRYEFEPZdbISEi^%^2fNh1RdT2M859BmrQgBMAkGByqGSM44BAMELjAsAhQGG7iG5FQ4lOAH5^%^2fBfN5CV6r^%^2f7HgIUfer2WKCXUL^%^2fRT4t^%^217kXsUndBuY4^%^3d; SAP_SESSIONID_FSP_100=OYOybmh_6i0WbJP6gI-1xFcKeY59ahHujOPReeI0vos^%^3d',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}

response = requests.get(
    'https://dhareeba.gov.qa/sap/bc/ui5_ui5/sap/zmcf_fmca/index.html?saml2idp=https://www.nas.gov.qa/idp&lang=en&sap-client=100&sap-language=EN^#/notificationmanagement',
    cookies=cookies,
    headers=headers,
)

print(response)