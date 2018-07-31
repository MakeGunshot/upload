***Settings***
Library     Selenium2Library
Test Teardown       Close Browser


***Variables***
${username}     testuser3
${psw}      123456
${URL}      http://118.31.19.120:3000/

***Test Cases***
打开网址
    [Setup]
        打开网址
        点击登录
        输入正确账号
        输入正确密码
        登录
        验证登录是否成功
        # 退出登录
        # 验证是否退出成功
    
    [Teardown]
        # 关闭浏览器
        Close Browser

***Keywords***
打开网址
    Open Browser        ${URL}      chrome
点击登录
    Click Element     xpath:/html/body/div[1]/div/div/ul/li[6]/a
输入正确账号
    Input Text      xpath://*[@id="name"]       ${username}
输入正确密码
    Input Text      xpath://*[@id="pass"]       ${psw}
登录
    Click Element       xpath://*[@id="signin_form"]/div[3]/input
验证登录是否成功   
    Page Should Contain Element     xpath://*[@id="sidebar"]/div[1]/div[2]/div/div/span[1]/a        message=testuser3



time sleep(3)
[Teardown]
    Close Browser