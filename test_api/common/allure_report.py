import allure


def allure_report_get(header_print, url, response_json):
    allure.attach("""
    <html>
    <body>
        <p><strong>请求体：</strong><br>{}</p><br>
        <p>{}</p><br>
        <p><strong>返回体：</strong><br>{}</p><br>
    </body>
    </html>""".format(header_print, url, response_json), 'Attach with HTML', allure.attachment_type.HTML)
    allure.dynamic.description_html("""
    <html>
    <body>
        <p><strong>请求体：</strong><br>{}</p><br>
        <p>{}</p><br>
        <p><strong>返回体：</strong><br>{}</p><br>
    </body>
    </html>""".format(header_print, url, response_json))


def allure_report_delete(header_print, url, response_json):
    allure.dynamic.description("""
    <body>
        <p><strong>请求体：</strong><br>{}</p><br>
        <p>{}</p><br>
        <p><strong>返回体：</strong><br>{}</p><br>
    </body>
    </html>""".format(header_print, url, response_json))
    allure.attach("""
    <html>
    <body>
        <p><strong>请求体：</strong><br>{}</p><br>
        <p>{}</p><br>
        <p><strong>返回体：</strong><br>{}</p><br>
    </body>
    </html>""".format(header_print, url, response_json), 'Attach with HTML', allure.attachment_type.HTML)


def allure_report_post(header_print, url, data, response_json):
    allure.dynamic.description("""
    <body>
        <p><strong>请求体：</strong><br>{}</p><br>
        <p>{}</p><br>
        <p>{}</p><br>
        <p><strong>返回体：</strong><br>{}</p><br>
    </body>
    </html>""".format(header_print, url, data, response_json))
    allure.attach("""
    <html>
    <body>
        <p><strong>请求体：</strong><br>{}</p><br>
        <p>{}</p><br>
        <p><strong>返回体：</strong><br>{}</p><br>
    </body>
    </html>""".format(header_print, url, response_json), 'Attach with HTML', allure.attachment_type.HTML)


def allure_report_put(header_print, url, data, response_json):
    allure.dynamic.description("""
    <body>
        <p>请求体<br>{}</p><br>
        <p>{}</p><br>
        <p>{}</p><br>
        <p>返回体：<br>{}</p><br>
    </body>
    </html>""".format(header_print, url, data, response_json))
    allure.attach("""
    <html>
    <body>
        <p><strong>请求体：</strong><br>{}</p><br>
        <p>{}</p><br>
        <p><strong>返回体：</strong><br>{}</p><br>
    </body>
    </html>""".format(header_print, url, response_json), 'Attach with HTML', allure.attachment_type.HTML)
