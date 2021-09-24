from SearchHelper import SearchHelper
from datetime import datetime
import time
import pytest


def test_Run(browser):
    # report_file = open('report.txt', 'w')
    test_page = SearchHelper(browser)
    starting = str(datetime.now())
    # report_file.write('Start testing: ' + str(datetime.now()))
    test_page.go_to_site()

    test_page.startbtn()
    # test_page.login('test', 'test', 'test', '9177474278', 'test@test.test')
    report_file = open('./Reports/report test ' + test_page.Get_ID_Test() + '.txt', 'w')
    report_file.write('Start testing: ' + starting)

    while not ('/finish' in test_page.current_URL()):

        time.sleep(0.19)

        if '/finish' in test_page.current_URL():
            report_file.write('\n\nEnd testing: ' + str(datetime.now()))
            report_file.close()
            break

        check_type = test_page.Check_Type()

        if 'Открытый вопрос.' in check_type:

            '''start = datetime.now()
            test_page.Open_Question()
            end = datetime.now()
            ft = end - start
            report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                              + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                              + '\nОткрытый вопрос: ' + str(ft))

            # assert True'''
            Open(test_page,report_file)
            continue

        elif 'Загрузка файлов.' in check_type:

            '''start = datetime.now()
            test_page.Upload_Question()
            end = datetime.now()
            report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                              + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                              + '\nЗагрузка файлов: ' + str(end - start))'''
            Upload(test_page, report_file)
            continue

        elif 'Мировой.' in check_type:

            '''start = datetime.now()
            test_page.World_Question()
            end = datetime.now()
            report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                              + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                              + '\nМировой: ' + str(end - start))'''
            World(test_page, report_file)
            continue

        elif 'Приоритет.' in check_type:

            '''start = datetime.now()
            test_page.Priority_Question()
            end = datetime.now()
            report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                              + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                              + '\nПриоритет: ' + str(end - start))'''
            Priority(test_page, report_file)

            continue

        elif 'Один из списка.' in check_type:
            '''start = datetime.now()
            test_page.Choose_Single()
            end = datetime.now()
            report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                              + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                              + '\nОдин из списка: ' + str(end - start))
            # assert True'''
            Single(test_page,report_file)
            continue

        elif 'Несколько из списка.' in check_type:
            '''start = datetime.now()
            test_page.Choose_Many()
            end = datetime.now()
            report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                              + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                              + '\nНесколько из списка: ' + str(end - start))
            # assert True'''
            Many(test_page, report_file)
            continue

        elif 'Шкала.' in check_type:
            '''start = datetime.now()
            test_page.Scale_Question()
            end = datetime.now()
            report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                              + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                              + '\nШкала: ' + str(end - start))
            # assert True'''
            Scale(test_page, report_file)
            continue
        pass

def Scale(test_page, report_file):
    start = datetime.now()
    test_page.Scale_Question()
    end = datetime.now()
    report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                      + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                      + '\nШкала: ' + str(end - start))
    assert True


def Many(test_page, report_file):
    start = datetime.now()
    test_page.Choose_Many()
    end = datetime.now()
    report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                      + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                      + '\nНесколько из списка: ' + str(end - start))
    assert True

def Single(test_page, report_file):
    start = datetime.now()
    test_page.Choose_Single()
    end = datetime.now()
    report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                      + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                      + '\nОдин из списка: ' + str(end - start))
    assert True

def Priority(test_page, report_file):
    start = datetime.now()
    test_page.Priority_Question()
    end = datetime.now()
    report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                      + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                      + '\nПриоритет: ' + str(end - start))
    assert True
def World(test_page, report_file):
    start = datetime.now()
    test_page.World_Question()
    end = datetime.now()
    report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                      + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                      + '\nМировой: ' + str(end - start))
    assert True
def Upload(test_page, report_file):
    start = datetime.now()
    test_page.Upload_Question()
    end = datetime.now()
    report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                      + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                      + '\nЗагрузка файлов: ' + str(end - start))
    assert True
def Open(test_page, report_file):
    start = datetime.now()
    test_page.Open_Question()
    end = datetime.now()
    ft = end - start
    report_file.write('\n\nID testing: ' + test_page.Get_ID_Test() + '   |   '
                      + 'ID Question: ' + test_page.Get_ID_Question() + '   |   '
                      + '\nОткрытый вопрос: ' + str(ft))

    assert True