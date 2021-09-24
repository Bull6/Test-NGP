from selenium.webdriver.common.by import By


class SpaceCheckTestsLocators:
    # For_login
    login_surname = (By.ID, 'candidates-surname')
    login_name = (By.ID, 'candidates-name')
    login_patronymic = (By.ID, 'candidates-patronymic')
    login_phone = (By.ID, 'candidates-phone')
    login_email = (By.ID, 'candidates-email')

    # For_tests
    instruction_button = (By.CSS_SELECTOR, '.instruction-button')

    check_type = (By.CSS_SELECTOR, '.question-view-instruction-item')

    start_btn = (By.CSS_SELECTOR, '.btn.btn-blue')

    next_btn = (By.CSS_SELECTOR, '.btn.btn-blue.btn-next')

    answers = (By.CSS_SELECTOR, '.autotest')

    priority = (By.CSS_SELECTOR, '.answer-options')

    radio_btn = (By.CSS_SELECTOR, '.question-radio.radio-wrapper')

    upload_file = (By.ID, "uploading-question-file")

    upload_text = (By.ID, 'uploading-question')

    open_question = (By.ID, 'open-question')

    # Get ID
    id_question = (By.ID, 'questions-type')
    id_test = (By.ID, 'testing-id')
