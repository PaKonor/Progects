#
# class TestMain():

def test_run(driver):
    driver.get("http://localhost/")
    print(driver.title)
    assert driver.title  == "Your Store" # убедимся, что находимся на той страгице, сравниваем title

# driver.title сравнение title (заголовок страници)
# assert driver.title == "OTUS - Онлайн-образование"