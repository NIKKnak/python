
# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
# (добавление, поиск, удаление, редактирование)
# Id // Имя Фамилия // номер телефона // должность // e-mail
# (работа с csv файлом)



def Welcome():
    from logger import write_data
    from logger import get_base
    from logger import search_contact
    from logger import search_result
    from logger import update
    from logger import delete




    print("Welcome to Umbrella Corporation\n\
    select an action\n\
    ###################\n\
    1 - поиск агента\n\
    2 - добавление нового агента\n\
    3 - удаление агента\n\
    4 - редактировать данные агента")
    action = input()
    s = input("Введите данные для поиска ")
    base = get_base()
    if action == '1':   
        result = search_contact(base, s)  
        search_result(result)   
    elif action == '2':
        write_data(input_data())
    elif action == '3':
        result = search_contact(base, s)  
        delete(s)        
    else:
        action == '4'
        a = search_contact(base, input_data) 
        update(result())            



def input_data():
    id_number = input("Введите уникальный номер агента: ")
    last_name = input("Введите позывной агента: ")
    phone_number = input("Введите номер связи с агентом: ")
    brith_name = input("Введите уровень доступа агента: ")
    note = input("Введите адрес для отправки данных: ")
    return [id_number, last_name, phone_number, brith_name, note]
