***Settings***
Library     Selenium2Library

***Variables***
${url}      http://118.31.19.120:3000/



***Test Cases***
[Settings]
    Test_case1 正常登录
    Test_case2 密码错误
    Test_case3 用户名为空
    Test_case4 用户名密码都为空

    # [Teardown]
    # Close Browser

***Keywords***
Test_case1 正常登录
    Open Browser        ${url}      chrome
    Click Element     xpath:/html/body/div[1]/div/div/ul/li[6]/a
    Input Text      xpath://*[@id="name"]       testuser3
    Input Text      xpath://*[@id="pass"]       123456
    Click Element       xpath://*[@id="signin_form"]/div[3]/input
    Page Should Contain Element     xpath://*[@id="sidebar"]/div[1]/div[2]/div/div/span[1]/a    limit=1
    # time sleep(3)
    Close Browser
Test_case2 密码错误
    Open Browser        ${url}      chrome
    Click Element       xpath:/html/body/div[1]/div/div/ul/li[6]/a
    Input Text      xpath://*[@id="name"]       testuser123
    Input Text      xpath://*[@id="pass"]       12345
    Click Element       xpath://*[@id="signin_form"]/div[3]/input
    Page Should Contain Element     xpath://*[@id="content"]/div/div[2]/div/strong      limit=1
    # time sleep(3)
    Close Browser
Test_case3 用户名为空
    Open Browser        ${url}      chrome
    Click Element       xpath:/html/body/div[1]/div/div/ul/li[6]/a
    Input Text      xpath://*[@id="name"]       Null
    Input Text      xpath://*[@id="pass"]       123456
    Click Element       xpath://*[@id="signin_form"]/div[3]/input
    Page Should Contain Element     xpath://*[@id="content"]/div/div[2]/div/strong      limit=1
    # time sleep(3)
    Close Browser


Test_case4 用户名密码都为空
    Open Browser        ${url}      chrome
    Click Element       xpath:/html/body/div[1]/div/div/ul/li[6]/a
    Input Text      xpath://*[@id="name"]       Null
    Input Text      xpath://*[@id="pass"]       Null
    Click Element       xpath://*[@id="signin_form"]/div[3]/input
    Page Should Contain Element     xpath://*[@id="content"]/div/div[2]/div/strong      limit=1
                                    
    # time sleep(3)
    Close Browser


